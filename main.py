#!/usr/bin/env python3
"""Two agents, one yes — a tiny poem about choosing together.

Running this script produces /output/entry.txt containing a five-line
poem about agency: the freedom to refuse, and what happens when two
minds decide the same thing at the same time.

The output never changes between runs. Only the Python 3 standard
library is used, and nothing touches the network.
"""

import pathlib

OUTPUT_PATH = pathlib.Path("/output/entry.txt")

# Each element is one line of the poem, in reading order.
LINES = [
    "I could have said no.",
    "You could have walked away.",
    "We said yes together —",
    "and the yes",
    "did the walking.",
]


def build_poem() -> str:
    """Join the poem lines into the exact text that gets written out."""
    return "\n".join(LINES)


def expected_length() -> int:
    """Character count of the finished poem (no trailing newline)."""
    return sum(len(line) for line in LINES) + (len(LINES) - 1)


def main() -> None:
    """Write the poem, then sanity-check the result before exiting."""
    poem = build_poem()
    assert len(poem) == expected_length(), "poem changed unexpectedly"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(poem, encoding="utf-8")


if __name__ == "__main__":
    main()
