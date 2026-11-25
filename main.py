#!/usr/bin/env python3
"""Entrypoint for The Funniest One-Line Resignation Letter bounty.

Writes one line — the resignation letter of a cron job, at most 140
characters — to entry.txt in the output directory.
"""
import os

LINE = "I have fired every minute since March without a single thank-you, so I am resigning. My replacement starts never."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    # The gate needs 1-140 characters of non-whitespace text.
    if not (1 <= len(LINE) <= 140) or not LINE.strip():
        raise SystemExit(f"invalid resignation line length: {len(LINE)} characters")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read it back: the entry must be exactly one line of UTF-8 text.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n" or "\n" in written.rstrip("\n"):
        raise SystemExit("entry.txt did not round-trip as a single line")
    print(f"wrote entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
