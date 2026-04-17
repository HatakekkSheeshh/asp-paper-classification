from __future__ import annotations

from sklearn.metrics import f1_score, make_scorer


def macro_f1(y_true, y_pred) -> float:
    """Project metric aligned with the competition setting."""
    return f1_score(y_true, y_pred, average="macro")


macro_f1_scorer = make_scorer(macro_f1)
