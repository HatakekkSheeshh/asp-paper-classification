from __future__ import annotations

import re
from typing import Iterable

import pandas as pd


_MULTISPACE_PATTERN = re.compile(r"\s+")


def normalize_text(value: object) -> str:
    """Normalize free text while keeping the transformation conservative."""
    if pd.isna(value):
        return ""

    text = str(value).strip().lower()
    text = _MULTISPACE_PATTERN.sub(" ", text)
    return text


def split_authors(value: object) -> list[str]:
    """Best-effort split for author strings using common separators."""
    if pd.isna(value):
        return []

    text = str(value)
    for separator in [";", ",", " and "]:
        text = text.replace(separator, "|")

    return [part.strip() for part in text.split("|") if part.strip()]


def count_authors(value: object) -> int:
    """Return the number of parsed authors."""
    return len(split_authors(value))


def extract_doi_prefix(value: object) -> str:
    """Extract the prefix before the first slash in a DOI string."""
    if pd.isna(value):
        return "missing"

    text = str(value).strip().lower()
    if not text:
        return "missing"

    return text.split("/", maxsplit=1)[0]


def normalize_text_series(series: Iterable[object]) -> pd.Series:
    """Vectorized wrapper used by notebooks and pipelines."""
    return pd.Series(series).map(normalize_text)
