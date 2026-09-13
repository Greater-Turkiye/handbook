#!/usr/bin/env python3
"""Check that English mirror pages keep up with their Turkish originals.

Rules (see issue #5):

* Every ``en/*.md`` page must start with ``> translation_of: tr/<file>.md``
  and that Turkish page must exist.                                -> error
* Every ``tr/*.md`` page must have at least one English mirror.     -> error
* If the Turkish page's last commit is newer than the English
  page's last commit, the English page may be stale.               -> warning

Findings are printed as GitHub Actions workflow commands, so they appear as
annotations on the PR. The script exits 1 if there is any error; warnings
alone do not fail the check.

Needs full git history (``actions/checkout`` with ``fetch-depth: 0``);
in a shallow clone, commit times are not meaningful.

Usage: python scripts/check_translation_drift.py
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER_RE = re.compile(r"^>\s*translation_of:\s*(\S+)\s*$")
TARGET_RE = re.compile(r"^tr/[^/]+\.md$")


def annotate(level: str, path: str, message: str, line: int | None = None) -> None:
    loc = f"file={path}" + (f",line={line}" if line else "")
    print(f"::{level} {loc}::{message}")


def last_commit_time(path: str) -> int | None:
    """Committer timestamp of the last commit touching ``path`` (None if uncommitted)."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", path],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    return int(out) if out else None


def read_header(path: Path) -> str | None:
    """Return the translation_of target from the first non-empty line, if present."""
    with path.open(encoding="utf-8-sig") as fh:
        for raw in fh:
            line = raw.strip()
            if not line:
                continue
            match = HEADER_RE.match(line)
            return match.group(1) if match else None
    return None


def main() -> int:
    if subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.strip() == "true":
        annotate("warning", "scripts/check_translation_drift.py",
                 "Shallow clone: commit times may be wrong. Use fetch-depth: 0.")

    errors = warnings = 0
    mirrored: set[str] = set()

    for en_path in sorted((ROOT / "en").glob("*.md")):
        en_rel = en_path.relative_to(ROOT).as_posix()
        target = read_header(en_path)

        if target is None:
            annotate("error", en_rel,
                     "Missing header: the first line must be '> translation_of: tr/<file>.md'.", 1)
            errors += 1
            continue
        if not TARGET_RE.match(target):
            annotate("error", en_rel,
                     f"translation_of must point to a page directly under tr/, got '{target}'.", 1)
            errors += 1
            continue
        if not (ROOT / target).is_file():
            annotate("error", en_rel,
                     f"translation_of points to '{target}', which does not exist.", 1)
            errors += 1
            continue

        mirrored.add(target)
        tr_time, en_time = last_commit_time(target), last_commit_time(en_rel)
        if tr_time is None or en_time is None:
            # Uncommitted local changes: nothing meaningful to compare yet.
            continue
        if tr_time > en_time:
            annotate("warning", en_rel,
                     f"{target} changed after this translation "
                     f"(tr: {tr_time}, en: {en_time}). Review and update the English page.", 1)
            warnings += 1

    for tr_path in sorted((ROOT / "tr").glob("*.md")):
        tr_rel = tr_path.relative_to(ROOT).as_posix()
        if tr_rel not in mirrored:
            annotate("error", tr_rel,
                     "No English mirror: add en/<file>.md starting with "
                     f"'> translation_of: {tr_rel}'.")
            errors += 1

    summary = (f"Translation drift check: {len(mirrored)} mirrored page(s), "
               f"{warnings} warning(s), {errors} error(s).")
    print(summary)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write(summary + "\n")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
