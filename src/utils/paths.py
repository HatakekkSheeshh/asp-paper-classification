from __future__ import annotations

from pathlib import Path

import yaml


def project_root() -> Path:
    """Return the repository root based on the current file location."""
    return Path(__file__).resolve().parents[2]


def resolve_project_path(relative_path: str | Path) -> Path:
    """Resolve a project-relative path."""
    return project_root() / Path(relative_path)


def load_config(config_path: str | Path = "configs/experiment_config.yaml") -> dict:
    """Load the shared YAML config."""
    full_path = resolve_project_path(config_path)
    with full_path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)
