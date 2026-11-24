#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one honest, funny line of software error copy to /output/entry.txt:
the brutal truth about what actually broke, in a single line of at most
200 characters.
"""

import os

ENTRY = "Our server didn't crash — it gave up halfway through your request and went home early. Refresh the page; it should be back from its nap by now."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
