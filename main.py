"""Entry point for The Funniest Out-of-Office bounty.

Writes one line to /output/entry.txt: a funny one-line out-of-office
reply. The line is at most 140 characters, deterministic, and needs
no network access. The joke is that the author ignores email the way
the office printer ignores paper jams.
"""
from pathlib import Path

OOO_LINE = (
    "I'm out of the office until Monday, ignoring emails the way our "
    "printer ignores paper jams: completely, and with great confidence."
)

TARGET = Path("/output/entry.txt")


def main():
    text = OOO_LINE.strip()
    assert 1 <= len(text) <= 140, f"out-of-office line is {len(text)} characters"
    assert "\n" not in text, "out-of-office line must be a single line"
    assert text.endswith("."), "out-of-office line should end with a full stop"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
