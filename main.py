#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to /output/entry.txt:
a sunrise over the sea — the first morning of a dream
trip, a postcard you can read at a glance.

Why this emoji: it lands on a dream vacation at once
(sun, sea, a faraway shore), it is vivid at small size,
and it is specific — one particular morning, not any
holiday. No words, no second emoji, nothing else.
"""

import os

EMOJI = "\U0001F305"  # SUNRISE — U+1F305, one emoji, 4 bytes UTF-8
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # The grader collects the output as another user: leave it readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
