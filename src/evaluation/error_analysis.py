from __future__ import annotations

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


def build_confusion_matrix_df(y_true, y_pred, labels: list[int] | None = None) -> pd.DataFrame:
    """Return a DataFrame version of the confusion matrix for easier plotting."""
    matrix = confusion_matrix(y_true, y_pred, labels=labels)
    if labels is None:
        labels = sorted(pd.Series(y_true).dropna().unique().tolist())

    index = [f"true_{label}" for label in labels]
    columns = [f"pred_{label}" for label in labels]
    return pd.DataFrame(matrix, index=index, columns=columns)


def per_class_report_df(y_true, y_pred) -> pd.DataFrame:
    """Convert scikit-learn's classification report into a DataFrame."""
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    return pd.DataFrame(report).transpose()
