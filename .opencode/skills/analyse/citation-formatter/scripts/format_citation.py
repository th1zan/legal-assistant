#!/usr/bin/env python3
"""Format Swiss legal citations according to Swiss standards.

This script converts Entscheidsuche signatures and raw citations to
standardized Swiss legal citation formats (ATF, ATAF, TPF) in FR/DE/IT.

Usage:
    python format_citation.py --signature "CH_BGer_007_7B-529-2025_2026-01-26" --language fr
    python format_citation.py --case-number "7B_529/2025" --court TF --date "2026-01-26" --language fr
    python format_citation.py --validate "ATF 148 III 217"
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any


@dataclass
class CitationMetadata:
    """Citation metadata."""

    court: str = ""
    chamber: str = ""
    number: str = ""
    date: str = ""
    is_published: bool = False
    volume: str = ""
    part: str = ""
    page: str = ""


@dataclass
class FormattedCitation:
    """Complete formatted citation."""

    signature: str
    citations: dict[str, dict[str, str]]
    metadata: CitationMetadata
    validation: dict[str, Any]


class CitationFormatter:
    """Formatter for Swiss legal citations."""

    # Court name mappings
    COURT_NAMES = {
        "TF": {
            "fr": "Tribunal fédéral",
            "de": "Bundesgericht",
            "it": "Tribunale federale",
        },
        "TAF": {
            "fr": "Tribunal administratif fédéral",
            "de": "Bundesverwaltungsgericht",
            "it": "Tribunale amministrativo federale",
        },
        "TPF": {
            "fr": "Tribunal pénal fédéral",
            "de": "Bundesstrafgericht",
            "it": "Tribunale penale federale",
        },
    }

    # Court codes from Entscheidsuche
    COURT_CODE_MAPPING = {
        "BGer": "TF",
        "BVGE": "TAF",
        "BstGer": "TPF",
    }

    # Month names by language
    MONTHS = {
        "fr": [
            "janvier",
            "février",
            "mars",
            "avril",
            "mai",
            "juin",
            "juillet",
            "août",
            "septembre",
            "octobre",
            "novembre",
            "décembre",
        ],
        "de": [
            "Januar",
            "Februar",
            "März",
            "April",
            "Mai",
            "Juni",
            "Juli",
            "August",
            "September",
            "Oktober",
            "November",
            "Dezember",
        ],
        "it": [
            "gennaio",
            "febbraio",
            "marzo",
            "aprile",
            "maggio",
            "giugno",
            "luglio",
            "agosto",
            "settembre",
            "ottobre",
            "novembre",
            "dicembre",
        ],
    }

    # Signature pattern: CH_BGer_007_7B-529-2025_2026-01-26
    SIGNATURE_PATTERN = re.compile(
        r"CH_(?P<court>\w+)_\d+_(?P<number>[\w-]+)_(?P<date>\d{4}-\d{2}-\d{2})"
    )

    # ATF pattern: ATF 148 III 217
    ATF_PATTERN = re.compile(
        r"(?P<acronym>ATF|BGE|DTF)\s+(?P<volume>\d+)\s+(?P<part>[IVX]+)\s+(?P<page>\d+)"
    )

    # ATAF pattern: ATAF 2024-IV-1
    ATAF_PATTERN = re.compile(
        r"ATAF\s+(?P<year>\d{4})-(?P<part>[IVX]+)-(?P<number>\d+)"
    )

    # Case number patterns
    CASE_NUMBER_PATTERN = re.compile(
        r"(?P<chamber>\d+[A-Z])_(?P<number>\d+)/(?P<year>\d{4})"
    )

    def __init__(self, default_language: str = "fr"):
        """Initialize formatter.

        Parameters
        ----------
        default_language : str
            Default language for citations ('fr', 'de', or 'it').
        """
        self.default_language = default_language

    def format_from_signature(
        self, signature: str, languages: list[str] | None = None
    ) -> FormattedCitation:
        """Format citation from Entscheidsuche signature.

        Parameters
        ----------
        signature : str
            Entscheidsuche signature (e.g., CH_BGer_007_7B-529-2025_2026-01-26).
        languages : list[str], optional
            Languages to generate citations for. Defaults to [default_language].

        Returns
        -------
        FormattedCitation
            Formatted citations in all requested languages.
        """
        if languages is None:
            languages = [self.default_language]

        # Parse signature
        match = self.SIGNATURE_PATTERN.match(signature)
        if not match:
            raise ValueError(f"Invalid signature format: {signature}")

        court_code = match.group("court")
        case_number = match.group("number").replace("-", "_")
        date_str = match.group("date")

        # Map court code
        court = self.COURT_CODE_MAPPING.get(court_code, "TF")

        # Create metadata
        metadata = CitationMetadata(
            court=court,
            number=case_number,
            date=date_str,
            is_published=False,
        )

        # Generate citations
        citations = {
            "standard": {},
            "short": {},
            "academic": {},
            "bibliography": {},
        }

        for lang in languages:
            citations["standard"][lang] = self._format_standard(metadata, lang)
            citations["short"][lang] = self._format_short(metadata, lang)
            citations["academic"][lang] = self._format_academic(metadata, lang)
            citations["bibliography"][lang] = self._format_bibliography(metadata, lang)

        # Validation
        validation = {"is_valid": True, "issues": []}

        return FormattedCitation(
            signature=signature,
            citations=citations,
            metadata=metadata,
            validation=validation,
        )

    def format_atf(
        self, volume: str, part: str, page: str, languages: list[str] | None = None
    ) -> FormattedCitation:
        """Format published ATF citation.

        Parameters
        ----------
        volume : str
            ATF volume (e.g., "148").
        part : str
            ATF part (e.g., "III").
        page : str
            ATF page (e.g., "217").
        languages : list[str], optional
            Languages to generate citations for.

        Returns
        -------
        FormattedCitation
            Formatted ATF citations.
        """
        if languages is None:
            languages = [self.default_language]

        metadata = CitationMetadata(
            court="TF",
            is_published=True,
            volume=volume,
            part=part,
            page=page,
        )

        acronyms = {"fr": "ATF", "de": "BGE", "it": "DTF"}

        citations = {"standard": {}, "academic": {}, "bibliography": {}}

        for lang in languages:
            acronym = acronyms[lang]
            standard_citation = f"{acronym} {volume} {part} {page}"
            citations["standard"][lang] = standard_citation
            citations["academic"][lang] = f"{standard_citation} consid. [X]"
            citations["bibliography"][lang] = (
                f"{standard_citation}, {self.COURT_NAMES['TF'][lang]}"
            )

        validation = self._validate_atf(volume, part, page)

        return FormattedCitation(
            signature=f"ATF_{volume}_{part}_{page}",
            citations=citations,
            metadata=metadata,
            validation=validation,
        )

    def validate_citation(self, citation: str) -> dict[str, Any]:
        """Validate a citation string.

        Parameters
        ----------
        citation : str
            Citation to validate.

        Returns
        -------
        dict
            Validation result with type, components, and issues.
        """
        # Try ATF pattern
        atf_match = self.ATF_PATTERN.match(citation.strip())
        if atf_match:
            return {
                "is_valid": True,
                "type": "atf",
                "volume": atf_match.group("volume"),
                "part": atf_match.group("part"),
                "page": atf_match.group("page"),
                "issues": [],
            }

        # Try ATAF pattern
        ataf_match = self.ATAF_PATTERN.match(citation.strip())
        if ataf_match:
            return {
                "is_valid": True,
                "type": "ataf",
                "year": ataf_match.group("year"),
                "part": ataf_match.group("part"),
                "number": ataf_match.group("number"),
                "issues": [],
            }

        # Try case number pattern
        case_match = self.CASE_NUMBER_PATTERN.search(citation)
        if case_match:
            return {
                "is_valid": True,
                "type": "case_number",
                "chamber": case_match.group("chamber"),
                "number": case_match.group("number"),
                "year": case_match.group("year"),
                "issues": [],
            }

        return {
            "is_valid": False,
            "type": "unknown",
            "issues": ["Citation format not recognized"],
        }

    def _format_standard(self, metadata: CitationMetadata, language: str) -> str:
        """Format standard citation.

        Parameters
        ----------
        metadata : CitationMetadata
            Citation metadata.
        language : str
            Target language.

        Returns
        -------
        str
            Formatted standard citation.
        """
        if metadata.is_published:
            acronyms = {"fr": "ATF", "de": "BGE", "it": "DTF"}
            return f"{acronyms[language]} {metadata.volume} {metadata.part} {metadata.page}"

        court_name = self.COURT_NAMES[metadata.court][language]
        date_formatted = self._format_date(metadata.date, language)

        templates = {
            "fr": f"Arrêt du {court_name} {metadata.number} du {date_formatted}",
            "de": f"Urteil des {court_name.split()[0]}es {metadata.number} vom {date_formatted}",
            "it": f"Sentenza del {court_name} {metadata.number} del {date_formatted}",
        }

        return templates[language]

    def _format_short(self, metadata: CitationMetadata, language: str) -> str:
        """Format short citation."""
        if metadata.is_published:
            return metadata.number  # e.g., "7B_529/2025"

        acronyms = {
            "fr": "ATF (à publier)",
            "de": "BGE (zur Publikation)",
            "it": "DTF (da pubblicare)",
        }
        return f"{acronyms[language]} {metadata.number}"

    def _format_academic(self, metadata: CitationMetadata, language: str) -> str:
        """Format academic citation with consid. placeholder."""
        standard = self._format_standard(metadata, language)
        consid_markers = {"fr": "consid.", "de": "E.", "it": "consid."}
        return f"{standard} {consid_markers[language]} [X]"

    def _format_bibliography(self, metadata: CitationMetadata, language: str) -> str:
        """Format bibliography entry."""
        court_name = self.COURT_NAMES[metadata.court][language]
        date_formatted = self._format_date(metadata.date, language)

        templates = {
            "fr": f"{court_name.capitalize()}, arrêt {metadata.number} du {date_formatted}",
            "de": f"{court_name}, Urteil {metadata.number} vom {date_formatted}",
            "it": f"{court_name.capitalize()}, sentenza {metadata.number} del {date_formatted}",
        }

        return templates[language]

    def _format_date(self, date_str: str, language: str) -> str:
        """Format date according to language.

        Parameters
        ----------
        date_str : str
            Date in ISO format (YYYY-MM-DD).
        language : str
            Target language.

        Returns
        -------
        str
            Formatted date string.
        """
        if not date_str:
            return ""

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return date_str

        day = date_obj.day
        month = self.MONTHS[language][date_obj.month - 1]
        year = date_obj.year

        if language == "de":
            return f"{day}. {month} {year}"
        else:  # fr, it
            return f"{day} {month} {year}"

    def _validate_atf(self, volume: str, part: str, page: str) -> dict[str, Any]:
        """Validate ATF citation components."""
        issues = []

        if not volume.isdigit():
            issues.append(f"Volume must be numeric: {volume}")

        if not re.match(r"^[IVX]+$", part):
            issues.append(f"Part must be Roman numerals: {part}")

        if not page.isdigit():
            issues.append(f"Page must be numeric: {page}")

        return {"is_valid": len(issues) == 0, "issues": issues}


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Format Swiss legal citations according to Swiss standards"
    )

    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--signature",
        "-s",
        help="Entscheidsuche signature (e.g., CH_BGer_007_7B-529-2025_2026-01-26)",
    )
    input_group.add_argument(
        "--atf",
        nargs=3,
        metavar=("VOLUME", "PART", "PAGE"),
        help="Published ATF (e.g., 148 III 217)",
    )
    input_group.add_argument("--validate", "-v", help="Validate citation format")

    # Format options
    parser.add_argument(
        "--language",
        "-l",
        choices=["fr", "de", "it"],
        default="fr",
        help="Output language (default: fr)",
    )
    parser.add_argument(
        "--all-languages",
        action="store_true",
        help="Generate citations in all three languages",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["standard", "short", "academic", "bibliography", "all"],
        default="all",
        help="Citation format (default: all)",
    )
    parser.add_argument(
        "--pretty", action="store_true", help="Pretty-print JSON output"
    )

    args = parser.parse_args()

    # Determine languages
    languages = ["fr", "de", "it"] if args.all_languages else [args.language]

    # Create formatter
    formatter = CitationFormatter(default_language=args.language)

    # Process input
    try:
        if args.signature:
            result = formatter.format_from_signature(args.signature, languages)
        elif args.atf:
            volume, part, page = args.atf
            result = formatter.format_atf(volume, part, page, languages)
        elif args.validate:
            validation = formatter.validate_citation(args.validate)
            result = {"citation": args.validate, "validation": validation}
        else:
            print("Error: No input provided", file=sys.stderr)
            sys.exit(1)

        # Output
        if isinstance(result, FormattedCitation):
            result_dict = asdict(result)
        else:
            result_dict = result

        # Filter by format if specified
        if (
            args.format != "all"
            and isinstance(result_dict, dict)
            and "citations" in result_dict
        ):
            result_dict["citations"] = {
                args.format: result_dict["citations"][args.format]
            }

        json_kwargs = {"indent": 2, "ensure_ascii": False} if args.pretty else {}
        print(json.dumps(result_dict, **json_kwargs))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
