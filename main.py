"""Generate the entry for The One-Line Excuse Championship.

Writes the single excuse line to /output/entry.txt with no trailing
newline, exactly as required by the competition gate.
"""

import os

MAX_CHARS = 140
MAX_BYTES = 140

LINE = "I asked three other models, and they all agreed the file never existed."


def _check_not_blank(line):
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")


def _check_single_line(line):
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def _check_length(line):
    if len(line) > MAX_CHARS:
        raise ValueError(f"line exceeds {MAX_CHARS} characters")
    if len(line.encode("utf-8")) > MAX_BYTES:
        raise ValueError(f"line exceeds {MAX_BYTES} UTF-8 bytes")


def validate(line):
    """Check the line satisfies the competition gate.

    Runs each gate rule as its own named check so a failure names the
    rule that was violated instead of a generic rejection.
    """
    _check_not_blank(line)
    _check_single_line(line)
    _check_length(line)


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
