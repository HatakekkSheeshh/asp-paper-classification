from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.paths import resolve_project_path


def append_experiment_row(row: dict, tracker_path: str | Path = "experiments/experiment_tracker.csv") -> None:
    """Append one experiment row while keeping the CSV header stable."""
    full_path = resolve_project_path(tracker_path)
    frame = pd.read_csv(full_path)
    updated = pd.concat([frame, pd.DataFrame([row])], ignore_index=True)
    updated.to_csv(full_path, index=False)
