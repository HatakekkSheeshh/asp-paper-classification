from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from src.features.preprocess import normalize_text_series


def build_text_series(frame: pd.DataFrame, text_column: str = "title") -> pd.Series:
    """Return a cleaned text series for modeling."""
    return normalize_text_series(frame[text_column]).fillna("")


def build_tfidf_vectorizer(
    analyzer: str = "word",
    ngram_range: tuple[int, int] = (1, 2),
    min_df: int | float = 1,
    max_df: int | float = 1.0,
    sublinear_tf: bool = True,
    extra_params: dict[str, Any] | None = None,
) -> TfidfVectorizer:
    """Create a TF-IDF vectorizer with sensible defaults for small text datasets."""
    params: dict[str, Any] = {
        "analyzer": analyzer,
        "ngram_range": ngram_range,
        "min_df": min_df,
        "max_df": max_df,
        "sublinear_tf": sublinear_tf,
    }
    if extra_params:
        params.update(extra_params)

    return TfidfVectorizer(**params)
