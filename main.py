#!/usr/bin/env python3
"""One Line, Zero Use: a hilariously useless superpower, in one line."""

import os

ENTRY = "I can stop time, but only while I sneeze. The universe freezes, and all I get is one decent achoo."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
