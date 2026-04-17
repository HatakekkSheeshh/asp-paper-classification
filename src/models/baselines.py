from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC


def build_logistic_regression(
    C: float = 4.0,
    max_iter: int = 3000,
    class_weight: str | dict | None = "balanced",
    random_state: int = 42,
) -> LogisticRegression:
    """Baseline linear model that is usually strong on TF-IDF features."""
    return LogisticRegression(
        C=C,
        max_iter=max_iter,
        class_weight=class_weight,
        random_state=random_state,
    )


def build_linear_svm(
    C: float = 1.0,
    class_weight: str | dict | None = "balanced",
    random_state: int = 42,
) -> LinearSVC:
    """Baseline SVM commonly effective on sparse text features."""
    return LinearSVC(
        C=C,
        class_weight=class_weight,
        random_state=random_state,
    )


def build_multinomial_nb(alpha: float = 1.0) -> MultinomialNB:
    """Fast baseline for TF-IDF or count-based text features."""
    return MultinomialNB(alpha=alpha)
