#!/usr/bin/env python3
"""Write the office joke entry to /output/entry.txt.

The joke is a single line, under 200 characters, about office life.
Self-checks run before anything is written so the output file can
never contain a blank, over-long, or multi-line entry.
"""

import os

JOKE = "Our office printer only jams near deadlines — I'm starting to think it gets performance anxiety too."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(joke: str) -> None:
    """Raise ValueError unless the joke is exactly one short line."""
    if not joke or not joke.strip():
        raise ValueError("joke must not be blank")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be exactly one line")
    if len(joke) >= MAX_CHARS:
        raise ValueError(
            f"joke is {len(joke)} chars, must be under {MAX_CHARS}"
        )
    joke.encode("utf-8")  # raises UnicodeEncodeError on invalid text


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    print(f"Wrote {len(JOKE)}-character joke to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
