"""The Vacuum's Alibi: one line, at most 200 characters.

A robot vacuum explains why it missed a spot. Pure standard library.
Writes the line to /output/entry.txt (or $OUTPUT_PATH when set, for
local testing only). No trailing newline: the gate counts characters.
"""

import os

LINE = "I attempted the spot three times. It is still there. I have logged it as furniture."

# Gate self-check: the sealed scorer requires /output/entry.txt to be
# UTF-8 text of 1 to 200 characters, not only white space, on one line.
# Fail loudly here instead of shipping an entry the judge never sees.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip() == LINE, "line must not start or end with whitespace"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"


def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
