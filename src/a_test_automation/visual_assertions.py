from pathlib import Path
import os
import shutil


async def assert_page_matches_baseline(page, baseline_path: Path, actual_path: Path) -> None:
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    actual_path.parent.mkdir(parents=True, exist_ok=True)

    await page.screenshot(path=str(actual_path), full_page=True)

    update_snapshots = os.getenv("UPDATE_SNAPSHOTS", "0") == "1"
    if update_snapshots or not baseline_path.exists():
        shutil.copyfile(actual_path, baseline_path)

    baseline_bytes = baseline_path.read_bytes()
    actual_bytes = actual_path.read_bytes()
    assert actual_bytes == baseline_bytes, (
        "Visual mismatch detected. "
        f"Baseline: {baseline_path}. Actual: {actual_path}. "
        "Re-run with UPDATE_SNAPSHOTS=1 to update baseline if change is expected."
    )
