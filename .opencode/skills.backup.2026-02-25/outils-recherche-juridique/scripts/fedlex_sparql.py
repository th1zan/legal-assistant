#!/usr/bin/env python3
"""CLI pour interroger Fedlex via SPARQL.

Ce script permet de rechercher et récupérer des textes législatifs fédéraux
suisses depuis le endpoint SPARQL de Fedlex.

Examples
--------
Générer le mapping complet RS → ELI (à faire une fois) :
    $ python fedlex_sparql.py generate-mapping

Rechercher une loi par numéro RS :
    $ python fedlex_sparql.py url 210

Rechercher par mots-clés :
    $ python fedlex_sparql.py search "Code civil"

Télécharger le HTML d'une loi :
    $ python fedlex_sparql.py get 210

Télécharger en texte brut (sans balises HTML) :
    $ python fedlex_sparql.py get 210 --text

Sauvegarder dans un fichier :
    $ python fedlex_sparql.py get 210 --output code_civil.html
    $ python fedlex_sparql.py get 210 --format pdf --output code_civil.pdf

Télécharger en PDF :
    $ python fedlex_sparql.py get 210 --format pdf

Lister les lois disponibles :
    $ python fedlex_sparql.py list

Notes
-----
Endpoint SPARQL : https://fedlex.data.admin.ch/sparqlendpoint
Documentation : https://www.fedlex.admin.ch/fr/opendata
Repo officiel : https://github.com/swiss/fedlex-sparql
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import Optional

try:
    from SPARQLWrapper import JSON, SPARQLWrapper
except ImportError:
    print("Error: SPARQLWrapper not installed. Run: pip install sparqlwrapper")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests")
    sys.exit(1)

# Optional: BeautifulSoup for better HTML parsing
try:
    from bs4 import BeautifulSoup

    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


SPARQL_ENDPOINT = "https://fedlex.data.admin.ch/sparqlendpoint"
FEDLEX_BASE_URL = "https://www.fedlex.admin.ch"

# Path to the full RS → ELI mapping file
SCRIPT_DIR = Path(__file__).parent
MAPPING_FILE = SCRIPT_DIR / "rs_to_eli_full.json"

# Language URIs for SPARQL queries
LANG_URIS = {
    "fr": "http://publications.europa.eu/resource/authority/language/FRA",
    "de": "http://publications.europa.eu/resource/authority/language/DEU",
    "it": "http://publications.europa.eu/resource/authority/language/ITA",
}

# File format URIs for SPARQL queries
FORMAT_URIS = {
    "html": "http://publications.europa.eu/resource/authority/file-type/HTML",
    "pdf": "http://publications.europa.eu/resource/authority/file-type/PDF",
    "pdf-a": "http://publications.europa.eu/resource/authority/file-type/PDF",  # Same as PDF
    "xml": "http://publications.europa.eu/resource/authority/file-type/XML",
    "docx": "http://publications.europa.eu/resource/authority/file-type/DOCX",
}

# Fallback mapping for most common laws (used if MAPPING_FILE doesn't exist)
RS_TO_ELI_FALLBACK = {
    # Droit constitutionnel (1)
    "101": {
        "eli": "cc/1999/404",
        "title": "Constitution fédérale",
        "abbreviation": "Cst.",
    },
    # Droit privé (2)
    "210": {"eli": "cc/24/233_245_233", "title": "Code civil", "abbreviation": "CC"},
    "220": {
        "eli": "cc/27/317_321_377",
        "title": "Code des obligations",
        "abbreviation": "CO",
    },
    "235.1": {
        "eli": "cc/2022/491",
        "title": "Loi sur la protection des données",
        "abbreviation": "LPD",
    },
    # Droit pénal (3)
    "311.0": {"eli": "cc/54/757_781_799", "title": "Code pénal", "abbreviation": "CP"},
    "312.0": {
        "eli": "cc/2010/661",
        "title": "Code de procédure pénale",
        "abbreviation": "CPP",
    },
    # Procédure civile (27)
    "272": {
        "eli": "cc/2010/262",
        "title": "Code de procédure civile",
        "abbreviation": "CPC",
    },
    # Droit des poursuites (28)
    "281.1": {
        "eli": "cc/11/529_556_547",
        "title": "Loi sur la poursuite pour dettes et la faillite",
        "abbreviation": "LP",
    },
    # Droit administratif
    "142.20": {
        "eli": "cc/2007/758",
        "title": "Loi sur les étrangers et l'intégration",
        "abbreviation": "LEI",
    },
    "172.021": {
        "eli": "cc/68/864",
        "title": "Loi sur la procédure administrative",
        "abbreviation": "PA",
    },
    "173.110": {
        "eli": "cc/2005/564",
        "title": "Loi sur le Tribunal fédéral",
        "abbreviation": "LTF",
    },
    # Assurances sociales
    "830.1": {
        "eli": "cc/2000/218",
        "title": "Loi sur la partie générale du droit des assurances sociales",
        "abbreviation": "LPGA",
    },
    "831.10": {
        "eli": "cc/2024/837",
        "title": "Loi sur l'assurance-invalidité",
        "abbreviation": "LAI",
    },
    "831.20": {"eli": "cc/69/328", "title": "Loi sur l'AVS", "abbreviation": "LAVS"},
    "832.10": {
        "eli": "cc/95/1328",
        "title": "Loi sur l'assurance-maladie",
        "abbreviation": "LAMal",
    },
}

# Common SPARQL prefixes (based on official swiss/fedlex-sparql repo)
PREFIXES = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
"""


# ==============================================================================
# HTML/Text Processing Functions
# ==============================================================================


def html_to_text(html_content: str) -> str:
    """Extract plain text from HTML content.

    Uses BeautifulSoup if available, otherwise falls back to regex-based extraction.

    Parameters
    ----------
    html_content : str
        Raw HTML content.

    Returns
    -------
    str
        Plain text with proper spacing and paragraph breaks.
    """
    if HAS_BS4:
        return _html_to_text_bs4(html_content)
    else:
        return _html_to_text_regex(html_content)


def _html_to_text_bs4(html_content: str) -> str:
    """Extract text using BeautifulSoup (preferred method).

    Parameters
    ----------
    html_content : str
        Raw HTML content.

    Returns
    -------
    str
        Cleaned plain text.
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove script and style elements
    for element in soup(["script", "style", "head", "meta", "link"]):
        element.decompose()

    # Get text with proper spacing
    text = soup.get_text(separator="\n")

    # Clean up whitespace
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)

    # Join with double newlines for paragraph breaks
    return "\n\n".join(lines)


def _html_to_text_regex(html_content: str) -> str:
    """Extract text using regex (fallback if BeautifulSoup not available).

    Parameters
    ----------
    html_content : str
        Raw HTML content.

    Returns
    -------
    str
        Cleaned plain text.
    """
    # Remove script and style content
    text = re.sub(
        r"<script[^>]*>.*?</script>", "", html_content, flags=re.DOTALL | re.IGNORECASE
    )
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)

    # Replace block elements with newlines
    block_tags = r"</?(div|p|br|h[1-6]|li|tr|td|th|article|section|header|footer|nav|table|ul|ol)[^>]*>"
    text = re.sub(block_tags, "\n", text, flags=re.IGNORECASE)

    # Remove all other HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Decode HTML entities
    text = html.unescape(text)

    # Clean up whitespace
    lines = []
    for line in text.splitlines():
        line = " ".join(line.split())  # Normalize internal whitespace
        if line:
            lines.append(line)

    # Join with double newlines
    return "\n\n".join(lines)


# ==============================================================================
# Mapping Management Functions
# ==============================================================================


def load_mapping() -> dict:
    """Load RS → ELI mapping from JSON file or fallback.

    Returns
    -------
    dict
        Dictionary mapping RS numbers to law info (eli, title, abbreviation).
    """
    if MAPPING_FILE.exists():
        with open(MAPPING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return RS_TO_ELI_FALLBACK


def save_mapping(mapping: dict) -> None:
    """Save RS → ELI mapping to JSON file.

    Parameters
    ----------
    mapping : dict
        Dictionary mapping RS numbers to law info.
    """
    with open(MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2, sort_keys=True)


def generate_full_mapping(lang: str = "fr") -> dict:
    """Generate complete RS → ELI mapping via SPARQL.

    Uses the official query from swiss/fedlex-sparql repo to fetch all laws
    from the Systematische Rechtssammlung (SR).

    Parameters
    ----------
    lang : str, optional
        Language for titles (fr, de, it). Defaults to "fr".

    Returns
    -------
    dict
        Complete mapping of RS numbers to law info.

    Notes
    -----
    This query may take 10-30 seconds to complete. Run once and save the result.
    """
    lang_uri = LANG_URIS.get(lang, LANG_URIS["fr"])

    # Official query from swiss/fedlex-sparql notebook
    query = f"""
    SELECT DISTINCT ?SR_Nummer ?Titel ?Abkuerzung ?SR_URI WHERE {{
        ?SR_URI rdf:type jolux:ConsolidationAbstract .
        ?SR_URI jolux:classifiedByTaxonomyEntry ?TaxonomyEntry ;
                jolux:isRealizedBy ?Expression .
        ?TaxonomyEntry skos:notation ?SR_Nummer .
        ?Expression jolux:language <{lang_uri}> .
        ?Expression jolux:title ?Titel .
        OPTIONAL {{ ?Expression jolux:titleShort ?Abkuerzung . }}
    }}
    ORDER BY ?SR_Nummer
    """

    print(f"Fetching all laws from Fedlex SPARQL endpoint...")
    print(f"Language: {lang}, this may take 10-30 seconds...")

    results = execute_sparql(query)
    bindings = results.get("results", {}).get("bindings", [])

    mapping = {}
    for binding in bindings:
        rs = binding.get("SR_Nummer", {}).get("value", "")
        if not rs:
            continue

        uri = binding.get("SR_URI", {}).get("value", "")
        # Extract ELI path from full URI
        # https://fedlex.data.admin.ch/eli/cc/1999/404 -> cc/1999/404
        eli = uri.replace("https://fedlex.data.admin.ch/eli/", "") if uri else ""

        mapping[rs] = {
            "eli": eli,
            "title": binding.get("Titel", {}).get("value", ""),
            "abbreviation": binding.get("Abkuerzung", {}).get("value", ""),
            "uri": uri,
        }

    print(f"Found {len(mapping)} laws.")

    # Save to file
    save_mapping(mapping)
    print(f"Mapping saved to: {MAPPING_FILE}")

    return mapping


# ==============================================================================
# SPARQL Query Functions
# ==============================================================================


def execute_sparql(query: str) -> dict:
    """Execute a SPARQL query against Fedlex endpoint.

    Parameters
    ----------
    query : str
        SPARQL query to execute.

    Returns
    -------
    dict
        JSON response from the SPARQL endpoint.

    Raises
    ------
    Exception
        If the query fails.
    """
    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setQuery(PREFIXES + query)
    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()
        return results
    except Exception as e:
        raise Exception(f"SPARQL query failed: {e}")


def get_file_download_url(
    eli: str, lang: str = "fr", fmt: str = "html"
) -> Optional[str]:
    """Get the actual file download URL for a law via SPARQL.

    This function queries Fedlex SPARQL to find the latest version of a law
    and returns the direct download URL for the specified format.

    Parameters
    ----------
    eli : str
        ELI path of the law (e.g., "cc/24/233_245_233").
    lang : str, optional
        Language code (fr, de, it). Defaults to "fr".
    fmt : str, optional
        Format: html, pdf, xml, docx. Defaults to "html".

    Returns
    -------
    str or None
        Direct download URL from fedlex.data.admin.ch/filestore, or None if not found.

    Notes
    -----
    The query finds the most recent version (Consolidation) and its file manifestation.
    """
    lang_uri = LANG_URIS.get(lang, LANG_URIS["fr"])
    format_uri = FORMAT_URIS.get(fmt, FORMAT_URIS["html"])
    law_uri = f"https://fedlex.data.admin.ch/eli/{eli}"

    query = f"""
    SELECT ?downloadUrl ?date WHERE {{
        # Find versions (Consolidations) of this law
        ?consolidation jolux:isMemberOf <{law_uri}> ;
                       jolux:dateApplicability ?date ;
                       jolux:isRealizedBy ?expression .

        # Filter by language
        ?expression jolux:language <{lang_uri}> ;
                    jolux:isEmbodiedBy ?manifestation .

        # Filter by format and get download URL
        ?manifestation jolux:format <{format_uri}> ;
                       jolux:isExemplifiedBy ?downloadUrl .
    }}
    ORDER BY DESC(?date)
    LIMIT 1
    """

    try:
        results = execute_sparql(query)
        bindings = results.get("results", {}).get("bindings", [])

        if bindings:
            return bindings[0].get("downloadUrl", {}).get("value")
        return None
    except Exception:
        return None


def search_by_rs(rs_number: str, lang: str = "fr", limit: int = 10) -> list[dict]:
    """Search for a law by its RS (Recueil Systématique) number.

    Parameters
    ----------
    rs_number : str
        RS number (e.g., "210" for Code civil, "220" for CO).
    lang : str, optional
        Language code (fr, de, it). Defaults to "fr".
    limit : int, optional
        Maximum number of results. Defaults to 10.

    Returns
    -------
    list of dict
        List of matching laws with title, URI, and date.
    """
    query = f"""
    SELECT ?act ?title ?dateInForce ?sr WHERE {{
      ?act a jolux:ConsolidationAbstract ;
           skos:prefLabel ?title ;
           jolux:classifiedByTaxonomyEntry ?sr .
      
      OPTIONAL {{ ?act jolux:dateEntryInForce ?dateInForce . }}
      
      FILTER(CONTAINS(STR(?sr), "/{rs_number}"))
      FILTER(LANG(?title) = "{lang}")
    }}
    ORDER BY ?sr
    LIMIT {limit}
    """

    results = execute_sparql(query)
    laws = []

    for binding in results.get("results", {}).get("bindings", []):
        laws.append(
            {
                "uri": binding.get("act", {}).get("value", ""),
                "title": binding.get("title", {}).get("value", ""),
                "rs": binding.get("sr", {}).get("value", "").split("/")[-1],
                "date_in_force": binding.get("dateInForce", {}).get("value", ""),
            }
        )

    return laws


def search_by_title(title_query: str, lang: str = "fr", limit: int = 20) -> list[dict]:
    """Search for laws by title keywords in local mapping.

    First searches the local mapping file. Falls back to SPARQL if mapping
    doesn't exist.

    Parameters
    ----------
    title_query : str
        Keywords to search in titles (case-insensitive).
    lang : str, optional
        Language code (fr, de, it). Defaults to "fr" (only used for SPARQL fallback).
    limit : int, optional
        Maximum number of results. Defaults to 20.

    Returns
    -------
    list of dict
        List of matching laws with title, abbreviation, RS number, and ELI.
    """
    # Search in local mapping first (fast)
    mapping = load_mapping()
    query_lower = title_query.lower()

    laws = []
    for rs, info in mapping.items():
        title = info.get("title", "").lower()
        abbr = info.get("abbreviation", "").lower()

        # Search in title and abbreviation
        if query_lower in title or query_lower in abbr:
            laws.append(
                {
                    "rs": rs,
                    "title": info.get("title", ""),
                    "abbreviation": info.get("abbreviation", ""),
                    "eli": info.get("eli", ""),
                }
            )

            if len(laws) >= limit:
                break

    # Sort by RS number
    laws.sort(key=lambda x: x["rs"])

    return laws


def get_law_metadata(rs_number: str, lang: str = "fr") -> Optional[dict]:
    """Get metadata for a specific law from local mapping.

    Parameters
    ----------
    rs_number : str
        RS number of the law.
    lang : str, optional
        Language code (for URL generation). Defaults to "fr".

    Returns
    -------
    dict or None
        Law metadata including title, abbreviation, ELI, and URLs.
    """
    mapping = load_mapping()

    if rs_number not in mapping:
        return None

    info = mapping[rs_number]
    eli = info.get("eli", "")

    return {
        "rs": rs_number,
        "title": info.get("title", ""),
        "abbreviation": info.get("abbreviation", ""),
        "eli": eli,
        "uri": info.get("uri", ""),
        "url_html": f"{FEDLEX_BASE_URL}/eli/{eli}/{lang}/html" if eli else "",
        "url_pdf": f"{FEDLEX_BASE_URL}/eli/{eli}/{lang}/pdf-a" if eli else "",
    }


def get_historical_versions(rs_number: str, limit: int = 50) -> list[dict]:
    """Get historical versions of a law.

    Parameters
    ----------
    rs_number : str
        RS number of the law.
    limit : int, optional
        Maximum number of versions. Defaults to 50.

    Returns
    -------
    list of dict
        List of versions with date and URI.
    """
    # First, find the law URI
    laws = search_by_rs(rs_number, limit=1)
    if not laws:
        return []

    law_uri = laws[0]["uri"]

    query = f"""
    SELECT ?version ?dateApplicable WHERE {{
      <{law_uri}> jolux:isRealizedBy ?version .
      
      OPTIONAL {{ ?version eli:date_applicability ?dateApplicable . }}
    }}
    ORDER BY DESC(?dateApplicable)
    LIMIT {limit}
    """

    results = execute_sparql(query)
    versions = []

    for binding in results.get("results", {}).get("bindings", []):
        versions.append(
            {
                "uri": binding.get("version", {}).get("value", ""),
                "date": binding.get("dateApplicable", {}).get("value", ""),
            }
        )

    return versions


def list_laws() -> list[dict]:
    """List all laws with known RS → ELI mapping.

    Returns
    -------
    list of dict
        List of laws with rs, title, abbreviation, and eli.
    """
    mapping = load_mapping()
    laws = []
    for rs, info in sorted(mapping.items(), key=lambda x: x[0]):
        laws.append(
            {
                "rs": rs,
                "title": info.get("title", ""),
                "abbreviation": info.get("abbreviation", ""),
                "eli": info.get("eli", ""),
            }
        )
    return laws


def get_download_url(
    rs_number: str, lang: str = "fr", fmt: str = "html"
) -> tuple[str, bool]:
    """Generate direct download URL for a law.

    Parameters
    ----------
    rs_number : str
        RS number of the law.
    lang : str, optional
        Language code. Defaults to "fr".
    fmt : str, optional
        Format: html, pdf, pdf-a, docx, xml. Defaults to "html".

    Returns
    -------
    tuple[str, bool]
        (URL, found_in_mapping) - the URL and whether RS was found in mapping.
    """
    mapping = load_mapping()
    if rs_number in mapping:
        eli = mapping[rs_number].get("eli", "")
        return f"{FEDLEX_BASE_URL}/eli/{eli}/{lang}/{fmt}", True
    else:
        # Generic pattern (may not work for all laws)
        return f"{FEDLEX_BASE_URL}/eli/cc/{rs_number}/{lang}/{fmt}", False


def download_law(
    rs_number: str,
    lang: str = "fr",
    fmt: str = "html",
    as_text: bool = False,
    output_path: Optional[Path] = None,
) -> str:
    """Download the text of a law.

    This function first tries to get the actual file URL via SPARQL,
    then falls back to the generic URL pattern if SPARQL fails.

    Parameters
    ----------
    rs_number : str
        RS number of the law.
    lang : str, optional
        Language code. Defaults to "fr".
    fmt : str, optional
        Format: html, pdf, xml, docx. Defaults to "html".
    as_text : bool, optional
        If True and format is HTML, extract plain text (no HTML tags).
        Defaults to False.
    output_path : Path, optional
        If provided, save content to this file. Defaults to None.

    Returns
    -------
    str
        Content of the law (for text formats), download info (for binary),
        or confirmation message if saved to file.
    """
    # Get ELI from mapping
    mapping = load_mapping()
    eli = mapping.get(rs_number, {}).get("eli", "")

    url = None
    source = "unknown"

    # Try to get the actual file URL via SPARQL
    if eli:
        url = get_file_download_url(eli, lang, fmt)
        if url:
            source = "SPARQL"

    # Fallback to generic URL pattern
    if not url:
        url, _ = get_download_url(rs_number, lang, fmt)
        source = "fallback"

    print(f"Downloading from: {url} (source: {source})", file=sys.stderr)

    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()

        # Handle text formats (HTML, XML)
        if fmt in ("html", "xml"):
            # Force UTF-8 encoding (Fedlex uses UTF-8)
            response.encoding = "utf-8"
            content = response.text

            # Convert HTML to plain text if requested
            if as_text and fmt == "html":
                content = html_to_text(content)

            # Save to file if output path provided
            if output_path:
                output_path.write_text(content, encoding="utf-8")
                return f"Content saved to: {output_path} ({len(content):,} characters)"

            return content

        # Handle binary formats (PDF, DOCX)
        else:
            binary_content = response.content

            # Save to file if output path provided
            if output_path:
                output_path.write_bytes(binary_content)
                return f"File saved to: {output_path} ({len(binary_content):,} bytes)"

            # Otherwise return info about the binary content
            return (
                f"Binary content downloaded ({len(binary_content):,} bytes).\n"
                f"URL: {url}\n"
                f"Content-Type: {response.headers.get('Content-Type', 'unknown')}\n"
                f"\nUse --output to save to a file."
            )

    except requests.RequestException as e:
        return f"Error downloading: {e}\nTry URL directly: {url}"


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="CLI pour interroger Fedlex via SPARQL et URLs ELI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  %(prog)s generate-mapping            Générer le mapping complet RS → ELI (~9000 lois)
  %(prog)s list                        Lister les lois disponibles (mapping local)
  %(prog)s url 210                     Obtenir l'URL du Code civil
  %(prog)s url 311.0 --format pdf      Obtenir l'URL PDF du Code pénal
  %(prog)s search "protection données" Rechercher par mots-clés
  %(prog)s get 210                     Télécharger le HTML du Code civil
  %(prog)s get 210 --text              Extraire le texte brut (sans HTML)
  %(prog)s get 210 --output cc.html    Sauvegarder dans un fichier
  %(prog)s get 210 -f pdf -o cc.pdf    Télécharger le PDF
  %(prog)s metadata 220                Métadonnées du CO
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Commande à exécuter")

    # Generate mapping command
    gen_parser = subparsers.add_parser(
        "generate-mapping",
        help="Générer le mapping complet RS → ELI (prend 10-30 secondes)",
    )
    gen_parser.add_argument(
        "--lang",
        default="fr",
        choices=["fr", "de", "it"],
        help="Langue pour les titres (défaut: fr)",
    )

    # List command
    subparsers.add_parser("list", help="Lister les lois avec mapping RS → ELI connu")

    # URL command (with positional argument)
    url_parser = subparsers.add_parser("url", help="Obtenir l'URL directe d'une loi")
    url_parser.add_argument("rs", help="Numéro RS (ex: 210, 220, 311.0)")
    url_parser.add_argument(
        "--lang", default="fr", choices=["fr", "de", "it"], help="Langue (défaut: fr)"
    )
    url_parser.add_argument(
        "--format",
        "-f",
        default="html",
        choices=["html", "pdf", "pdf-a", "docx", "xml"],
        help="Format (défaut: html)",
    )

    # Search command (with positional argument)
    search_parser = subparsers.add_parser(
        "search", help="Rechercher des lois par mots-clés"
    )
    search_parser.add_argument("query", help="Mots-clés à rechercher")
    search_parser.add_argument(
        "--lang", default="fr", choices=["fr", "de", "it"], help="Langue (défaut: fr)"
    )
    search_parser.add_argument(
        "--limit",
        "-n",
        type=int,
        default=20,
        help="Nombre max de résultats (défaut: 20)",
    )

    # Get command (with positional argument)
    get_parser = subparsers.add_parser("get", help="Télécharger le contenu d'une loi")
    get_parser.add_argument("rs", help="Numéro RS (ex: 210, 220, 311.0)")
    get_parser.add_argument(
        "--format",
        "-f",
        default="html",
        choices=["html", "pdf", "pdf-a", "docx", "xml"],
        help="Format (défaut: html)",
    )
    get_parser.add_argument(
        "--lang", default="fr", choices=["fr", "de", "it"], help="Langue (défaut: fr)"
    )
    get_parser.add_argument(
        "--text",
        "-t",
        action="store_true",
        help="Extraire le texte brut (sans balises HTML). Nécessite format HTML.",
    )
    get_parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Sauvegarder dans un fichier (ex: code_civil.html, loi.pdf)",
    )

    # Metadata command (with positional argument)
    meta_parser = subparsers.add_parser("metadata", help="Métadonnées d'une loi")
    meta_parser.add_argument("rs", help="Numéro RS (ex: 210, 220, 311.0)")
    meta_parser.add_argument(
        "--lang", default="fr", choices=["fr", "de", "it"], help="Langue (défaut: fr)"
    )

    # History command (with positional argument)
    history_parser = subparsers.add_parser(
        "history", help="Versions historiques d'une loi"
    )
    history_parser.add_argument("rs", help="Numéro RS (ex: 210, 220, 311.0)")
    history_parser.add_argument(
        "--limit",
        "-n",
        type=int,
        default=20,
        help="Nombre max de versions (défaut: 20)",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "generate-mapping":
            generate_full_mapping(args.lang)

        elif args.command == "list":
            laws = list_laws()
            print(f"Lois disponibles avec mapping RS → ELI ({len(laws)} lois):\n")
            for law in laws:
                abbr = f" ({law['abbreviation']})" if law["abbreviation"] else ""
                print(f"  RS {law['rs']:12} {law['title']}{abbr}")
            print(f"\nUtilisez 'url <RS>' pour obtenir l'URL directe.")

        elif args.command == "url":
            url, in_mapping = get_download_url(args.rs, args.lang, args.format)
            status = "mapping connu" if in_mapping else "pattern générique"
            print(f"RS {args.rs} ({status})")
            print(f"URL: {url}")

        elif args.command == "search":
            results = search_by_title(args.query, args.lang, args.limit)
            if results:
                print(f"Résultats pour '{args.query}' ({len(results)} trouvés):\n")
                for r in results:
                    print(f"  RS {r['rs']:12} {r['title']}")
            else:
                print(f"Aucun résultat pour '{args.query}'")

        elif args.command == "get":
            # Validate --text option
            if args.text and args.format != "html":
                print(
                    "Warning: --text only works with HTML format. Ignoring.",
                    file=sys.stderr,
                )

            # Prepare output path
            output_path = Path(args.output) if args.output else None

            content = download_law(
                args.rs,
                args.lang,
                args.format,
                as_text=args.text,
                output_path=output_path,
            )
            print(content)

        elif args.command == "history":
            versions = get_historical_versions(args.rs, args.limit)
            print(json.dumps(versions, indent=2, ensure_ascii=False))

        elif args.command == "metadata":
            metadata = get_law_metadata(args.rs, args.lang)
            if metadata:
                print(json.dumps(metadata, indent=2, ensure_ascii=False))
            else:
                print(f"Aucune loi trouvée pour RS {args.rs}", file=sys.stderr)
                sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
