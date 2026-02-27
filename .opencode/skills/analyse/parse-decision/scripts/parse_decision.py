#!/usr/bin/env python3
"""Parse Swiss court decisions from Entscheidsuche.

This script extracts structured sections from Swiss court decisions in HTML,
JSON, or PDF format. It handles multiple court formats (TF, TAF, TPF) and
three official languages (FR, DE, IT).

Usage:
    python parse_decision.py --input decision.html --format html --output structured.json
    python parse_decision.py --input decision.json --format json --output structured.json
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

try:
    from bs4 import BeautifulSoup
except ImportError:
    print(
        "Error: BeautifulSoup4 not installed. Install with: uv add beautifulsoup4 lxml"
    )
    sys.exit(1)


@dataclass
class Metadata:
    """Decision metadata."""

    signature: str = ""
    citation: str = ""
    court: str = ""
    chamber: str = ""
    date: str = ""
    judges: list[str] = field(default_factory=list)
    language: str = ""


@dataclass
class Section:
    """Decision section content."""

    raw_html: str = ""
    text: str = ""
    subsections: list[str] = field(default_factory=list)


@dataclass
class ParsedDecision:
    """Complete parsed decision structure."""

    metadata: Metadata
    sections: dict[str, Section] = field(default_factory=dict)
    references: dict[str, list[str]] = field(
        default_factory=lambda: {"legislative": [], "case_law": [], "doctrine": []}
    )
    format: str = "html"
    parsing_issues: list[str] = field(default_factory=list)


class DecisionParser:
    """Parser for Swiss court decisions."""

    # Section headers by language
    SECTION_PATTERNS = {
        "fr": {
            "faits": [
                r"En fait",
                r"Faits?\s*:",
                r"I\.\s*Faits",
                r"A\.\s*Faits",
            ],
            "droit": [
                r"En droit",
                r"Droit\s*:",
                r"II\.\s*Droit",
            ],
            "considerants": [
                r"Consid[ée]rant en droit",
                r"Consid[ée]rations",
                r"III\.\s*Consid[ée]rant",
            ],
            "dispositif": [
                r"Par ces motifs",
                r"Dispositif",
                r"le Tribunal.*?prononce\s*:",
            ],
        },
        "de": {
            "faits": [
                r"Sachverhalt",
                r"Tatbestand",
                r"I\.\s*Sachverhalt",
            ],
            "droit": [
                r"Rechtliche W[üu]rdigung",
                r"II\.\s*Rechtliche",
            ],
            "considerants": [
                r"Erw[äa]gungen",
                r"III\.\s*Erw[äa]gungen",
            ],
            "dispositif": [
                r"Demnach erkennt",
                r"Dispositiv",
                r"erkennt.*?Bundesgericht",
            ],
        },
        "it": {
            "faits": [
                r"In fatto",
                r"Fattispecie",
                r"I\.\s*In fatto",
            ],
            "droit": [
                r"In diritto",
                r"II\.\s*In diritto",
            ],
            "considerants": [
                r"Considerando in diritto",
                r"Considerandi",
                r"III\.\s*Considerando",
            ],
            "dispositif": [
                r"Per questi motivi",
                r"Dispositivo",
                r"Tribunale federale.*?pronuncia",
            ],
        },
    }

    # Reference patterns
    LEGISLATIVE_REF_PATTERN = re.compile(
        r"\bart\.?\s+\d+[\w\s,.-]*?[A-Z]{2,}(?:\s+[A-Z]{2,})?", re.IGNORECASE
    )
    CASE_LAW_PATTERN = re.compile(
        r"\b(?:ATF|ATAF|TPF)\s+\d+[\s\w/.-]+|\b\d+[A-Z]_\d+/\d+\b"
    )

    def __init__(self, language: str = "auto"):
        """Initialize parser.

        Parameters
        ----------
        language : str
            Expected language ('fr', 'de', 'it', or 'auto' for detection).
        """
        self.language = language

    def parse_html(self, html_content: str) -> ParsedDecision:
        """Parse HTML decision content.

        Parameters
        ----------
        html_content : str
            Raw HTML content from Entscheidsuche.

        Returns
        -------
        ParsedDecision
            Structured decision with extracted sections.
        """
        soup = BeautifulSoup(html_content, "lxml")

        # Detect language if auto
        if self.language == "auto":
            detected_lang = self._detect_language(soup.get_text())
            self.language = detected_lang

        # Extract metadata
        metadata = self._extract_metadata(soup)
        metadata.language = self.language

        # Extract sections
        sections = self._extract_sections(soup)

        # Extract references
        full_text = soup.get_text()
        references = self._extract_references(full_text)

        # Check for parsing issues
        issues = []
        if not sections:
            issues.append("No standard sections detected")
        if not metadata.date:
            issues.append("Date not found in metadata")

        return ParsedDecision(
            metadata=metadata,
            sections=sections,
            references=references,
            format="html",
            parsing_issues=issues,
        )

    def parse_json(self, json_content: dict[str, Any]) -> ParsedDecision:
        """Parse JSON decision metadata.

        Parameters
        ----------
        json_content : dict
            JSON object from Entscheidsuche.

        Returns
        -------
        ParsedDecision
            Structured decision (may have limited content if HTML unavailable).
        """
        # Extract metadata from JSON
        metadata = Metadata(
            signature=json_content.get("signature", ""),
            citation=json_content.get("title", ""),
            court=json_content.get("court", ""),
            date=json_content.get("decision_date", ""),
            language=json_content.get("language", ""),
        )

        # If HTML is embedded, parse it
        sections = {}
        if "html_content" in json_content:
            html_result = self.parse_html(json_content["html_content"])
            sections = html_result.sections

        # Extract plain text if available
        elif "text_content" in json_content:
            plain_text = json_content["text_content"]
            sections = {"full_text": Section(text=plain_text)}

        issues = []
        if not sections:
            issues.append("No content available (PDF-only decision)")

        return ParsedDecision(
            metadata=metadata,
            sections=sections,
            references={"legislative": [], "case_law": [], "doctrine": []},
            format="json",
            parsing_issues=issues,
        )

    def _detect_language(self, text: str) -> str:
        """Detect document language.

        Parameters
        ----------
        text : str
            Full text content.

        Returns
        -------
        str
            Detected language code ('fr', 'de', or 'it').
        """
        # Count language-specific keywords
        indicators = {
            "fr": ["considérant", "droit", "recours", "arrêt", "tribunal"],
            "de": ["erwägungen", "recht", "beschwerde", "urteil", "gericht"],
            "it": ["considerando", "diritto", "ricorso", "sentenza", "tribunale"],
        }

        text_lower = text.lower()
        scores = {}

        for lang, keywords in indicators.items():
            scores[lang] = sum(text_lower.count(keyword) for keyword in keywords)

        # Return language with highest score
        detected = max(scores, key=scores.get)  # type: ignore
        return detected if scores[detected] > 0 else "fr"  # Default to French

    def _extract_metadata(self, soup: BeautifulSoup) -> Metadata:
        """Extract metadata from HTML.

        Parameters
        ----------
        soup : BeautifulSoup
            Parsed HTML document.

        Returns
        -------
        Metadata
            Extracted metadata.
        """
        metadata = Metadata()

        # Try to find metadata in common locations
        # This is a simplified version - real implementation would need
        # to handle multiple HTML structures from different courts

        # Look for date patterns
        date_pattern = re.compile(r"\d{1,2}\s+\w+\s+\d{4}|\d{4}-\d{2}-\d{2}")
        date_match = date_pattern.search(soup.get_text())
        if date_match:
            metadata.date = date_match.group(0)

        # Look for court name
        court_keywords = ["Tribunal fédéral", "Bundesgericht", "Tribunale federale"]
        text = soup.get_text()
        for keyword in court_keywords:
            if keyword in text:
                metadata.court = keyword
                break

        return metadata

    def _extract_sections(self, soup: BeautifulSoup) -> dict[str, Section]:
        """Extract decision sections from HTML.

        Parameters
        ----------
        soup : BeautifulSoup
            Parsed HTML document.

        Returns
        -------
        dict[str, Section]
            Dictionary of section name to Section object.
        """
        sections = {}
        full_text = soup.get_text()

        patterns = self.SECTION_PATTERNS.get(self.language, self.SECTION_PATTERNS["fr"])

        for section_name, section_patterns in patterns.items():
            for pattern in section_patterns:
                match = re.search(pattern, full_text, re.IGNORECASE | re.MULTILINE)
                if match:
                    # Found section header
                    start_pos = match.end()

                    # Find next section or end of document
                    end_pos = len(full_text)
                    for next_patterns in patterns.values():
                        for next_pattern in next_patterns:
                            next_match = re.search(
                                next_pattern,
                                full_text[start_pos:],
                                re.IGNORECASE | re.MULTILINE,
                            )
                            if next_match:
                                candidate_end = start_pos + next_match.start()
                                if candidate_end < end_pos:
                                    end_pos = candidate_end

                    # Extract section text
                    section_text = full_text[start_pos:end_pos].strip()

                    sections[section_name] = Section(
                        text=section_text,
                        raw_html="",  # Could extract HTML here if needed
                    )
                    break

        return sections

    def _extract_references(self, text: str) -> dict[str, list[str]]:
        """Extract legal references from text.

        Parameters
        ----------
        text : str
            Full text content.

        Returns
        -------
        dict[str, list[str]]
            Dictionary with 'legislative', 'case_law', and 'doctrine' references.
        """
        references = {
            "legislative": [],
            "case_law": [],
            "doctrine": [],
        }

        # Extract legislative references (art. X CC, etc.)
        legislative_matches = self.LEGISLATIVE_REF_PATTERN.findall(text)
        references["legislative"] = list(set(legislative_matches))  # Remove duplicates

        # Extract case law references (ATF, ATAF, etc.)
        case_law_matches = self.CASE_LAW_PATTERN.findall(text)
        references["case_law"] = list(set(case_law_matches))

        return references


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Parse Swiss court decisions from Entscheidsuche"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        type=Path,
        help="Input file path (HTML or JSON)",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["html", "json", "auto"],
        default="auto",
        help="Input format (default: auto-detect)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Output file path (JSON). If not specified, prints to stdout.",
    )
    parser.add_argument(
        "--language",
        "-l",
        choices=["fr", "de", "it", "auto"],
        default="auto",
        help="Document language (default: auto-detect)",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )

    args = parser.parse_args()

    # Read input file
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    content = args.input.read_text(encoding="utf-8")

    # Auto-detect format if needed
    format_type = args.format
    if format_type == "auto":
        if content.strip().startswith("{"):
            format_type = "json"
        else:
            format_type = "html"

    # Parse content
    decision_parser = DecisionParser(language=args.language)

    if format_type == "json":
        json_data = json.loads(content)
        result = decision_parser.parse_json(json_data)
    else:  # html
        result = decision_parser.parse_html(content)

    # Convert to dict
    result_dict = asdict(result)

    # Output
    json_kwargs = {"indent": 2, "ensure_ascii": False} if args.pretty else {}

    if args.output:
        args.output.write_text(json.dumps(result_dict, **json_kwargs), encoding="utf-8")
        print(f"✅ Parsed decision written to: {args.output}")
    else:
        print(json.dumps(result_dict, **json_kwargs))

    # Print warnings if any
    if result.parsing_issues:
        print("\n⚠️  Parsing issues detected:", file=sys.stderr)
        for issue in result.parsing_issues:
            print(f"  - {issue}", file=sys.stderr)


if __name__ == "__main__":
    main()
