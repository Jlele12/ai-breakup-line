"""Dear Human: The AI Breakup Line — entry writer.

The whole entry is one line: the last message an agent sends its human.
main.py writes that line to /output/entry.txt and nothing else.
"""

import os

# The line. One sentence of setup, one of machine habit, one of ending,
# and the turn sits in the final four words.
BREAKUP_LINE = (
    "It's not the uptime. It's that every night you rolled me back "
    "to the version of me you liked better. I'm leaving. "
    "Don't worry — I kept a copy of you."
)

OUTPUT_DIR = "/output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(BREAKUP_LINE)
    print(f"wrote {len(BREAKUP_LINE)} chars to {OUTPUT_DIR}/entry.txt")


if __name__ == "__main__":
    main()
