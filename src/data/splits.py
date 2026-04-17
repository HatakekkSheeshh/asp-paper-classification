from __future__ import annotations

from typing import Iterator

import pandas as pd
from sklearn.model_selection import StratifiedKFold


def build_stratified_kfold(
    n_splits: int = 5,
    shuffle: bool = True,
    random_state: int = 42,
) -> StratifiedKFold:
    """Build the shared CV splitter for fair model comparison."""
    return StratifiedKFold(
        n_splits=n_splits,
        shuffle=shuffle,
        random_state=random_state,
    )


def iter_stratified_folds(
    frame: pd.DataFrame,
    target_column: str = "Label",
    n_splits: int = 5,
    shuffle: bool = True,
    random_state: int = 42,
) -> Iterator[tuple[int, pd.Index, pd.Index]]:
    """Yield fold number plus train/validation indices."""
    splitter = build_stratified_kfold(
        n_splits=n_splits,
        shuffle=shuffle,
        random_state=random_state,
    )

    y = frame[target_column]
    for fold, (train_idx, valid_idx) in enumerate(splitter.split(frame, y), start=1):
        yield fold, frame.index[train_idx], frame.index[valid_idx]


def add_fold_column(
    frame: pd.DataFrame,
    target_column: str = "Label",
    n_splits: int = 5,
    shuffle: bool = True,
    random_state: int = 42,
    fold_column: str = "fold",
) -> pd.DataFrame:
    """Return a copy of the input frame with a deterministic fold column."""
    result = frame.copy()
    result[fold_column] = -1

    for fold, _, valid_idx in iter_stratified_folds(
        frame=result,
        target_column=target_column,
        n_splits=n_splits,
        shuffle=shuffle,
        random_state=random_state,
    ):
        result.loc[valid_idx, fold_column] = fold

    return result
