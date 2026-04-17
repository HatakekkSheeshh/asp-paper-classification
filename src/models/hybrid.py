from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_hybrid_preprocessor(
    text_column: str,
    categorical_columns: list[str],
    numeric_columns: list[str],
    text_vectorizer: TfidfVectorizer | None = None,
) -> ColumnTransformer:
    """Create a reusable preprocessor for hybrid text + metadata models."""
    if text_vectorizer is None:
        text_vectorizer = TfidfVectorizer(
            analyzer="word",
            ngram_range=(1, 2),
            sublinear_tf=True,
        )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler(with_mean=False)),
        ]
    )

    transformers = [("text", text_vectorizer, text_column)]
    if categorical_columns:
        transformers.append(("categorical", categorical_pipeline, categorical_columns))
    if numeric_columns:
        transformers.append(("numeric", numeric_pipeline, numeric_columns))

    return ColumnTransformer(transformers=transformers, remainder="drop")
