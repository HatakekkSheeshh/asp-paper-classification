from __future__ import annotations

from sklearn.ensemble import VotingClassifier


def build_soft_voting_classifier(
    estimators: list[tuple[str, object]],
    weights: list[float] | None = None,
) -> VotingClassifier:
    """Build a soft-voting ensemble for probabilistic base models."""
    return VotingClassifier(
        estimators=estimators,
        voting="soft",
        weights=weights,
    )
