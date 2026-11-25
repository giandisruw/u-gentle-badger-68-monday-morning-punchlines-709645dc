#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one Monday-morning joke, a single line of 126 characters
(gate: 1 to 200), to /output/entry.txt. The line is chosen by a local
pairwise tournament judged against the bounty's published judge brief
(see README.md for the tournament table).

Revision (v2): ENTRY replaced with the tournament winner (#2 — the
9 a.m. Friday-meeting joke beat Swiss leader #7 in the final,
0.75-0.25). validate() gained a leading/trailing-whitespace guard:
the v1 test showed entry.txt is 133 bytes for 131 characters (the em
dash is 3 bytes in UTF-8), so the gate counts characters, not bytes,
and an invisible trailing space would silently waste gate budget and
could be trimmed by a grader — it is now rejected outright.
"""

import os

# Winning line (tournament winner #2 — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #7 led the Swiss at 3.15, #2 second at 2.75;
# the final went to #2, 0.75-0.25.
ENTRY = (
    "My Monday alarm didn't wake me up; it just introduced me to the "
    "version of myself that agreed to a 9 a.m. meeting on a Friday."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 200
    characters, not only white space". Single-line follows from the
    task itself (one joke, at most 200 characters). Returns the line
    unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    line.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(line) <= 200:
        raise ValueError(f"length {len(line)} outside 1-200")
    if not line.strip():
        raise ValueError("entry is only white space")
    if line != line.strip():
        raise ValueError("entry has leading or trailing white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Atomically write `line` to entry.txt inside `out_dir`.

    Writes to a temp file in the same directory, flushes and fsyncs
    it, then renames it into place so the grader never observes a
    half-written entry, and fsyncs the directory so the rename itself
    is durable. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(out_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return target


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly.

    Compares both the raw bytes and the decoded text; any mismatch
    raises RuntimeError so a corrupted or truncated entry fails loudly
    instead of being submitted.
    """
    expected_bytes = expected.encode("utf-8")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    if actual_bytes != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual_bytes)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    if actual_bytes.decode("utf-8") != expected:
        raise RuntimeError(f"verification failed: {path} content mismatch")


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    path = write_entry(line, out_dir)
    verify_written(path, line)
    print(f"Wrote {len(line)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
