from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.paths import load_config, resolve_project_path


def _get_config(config_path: str | Path = "configs/experiment_config.yaml") -> dict:
    return load_config(config_path)


def load_train_data(config_path: str | Path = "configs/experiment_config.yaml") -> pd.DataFrame:
    """Load the configured training dataset."""
    config = _get_config(config_path)
    train_path = resolve_project_path(config["paths"]["train_raw"])
    return pd.read_csv(train_path)


def load_test_data(config_path: str | Path = "configs/experiment_config.yaml") -> pd.DataFrame:
    """Load the configured test dataset."""
    config = _get_config(config_path)
    test_path = resolve_project_path(config["paths"]["test_raw"])
    return pd.read_csv(test_path)


def load_train_and_test(config_path: str | Path = "configs/experiment_config.yaml") -> tuple[pd.DataFrame, pd.DataFrame]:
    """Convenience wrapper used by notebooks and quick scripts."""
    return load_train_data(config_path), load_test_data(config_path)
