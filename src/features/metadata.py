from __future__ import annotations

import pandas as pd

from src.features.preprocess import count_authors, extract_doi_prefix, normalize_text


def build_metadata_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Create lightweight metadata features that work well on small datasets."""
    result = frame.copy()

    result["venue_clean"] = result.get("venue", pd.Series(index=result.index, dtype=object)).map(normalize_text)
    result["year"] = pd.to_numeric(result.get("year"), errors="coerce")
    result["year_missing"] = result["year"].isna().astype(int)
    result["author_count"] = result.get("authors", pd.Series(index=result.index, dtype=object)).map(count_authors)
    result["doi_prefix"] = result.get("doi", pd.Series(index=result.index, dtype=object)).map(extract_doi_prefix)
    result["doi_length"] = result.get("doi", pd.Series(index=result.index, dtype=object)).fillna("").astype(str).str.len()
    result["title_length"] = result.get("title", pd.Series(index=result.index, dtype=object)).fillna("").astype(str).str.len()
    result["title_word_count"] = (
        result.get("title", pd.Series(index=result.index, dtype=object))
        .fillna("")
        .astype(str)
        .str.split()
        .map(len)
    )

    return result
