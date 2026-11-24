"""Alien Field Notes: The Two Day Earth Review -- entry generator.

Writes a single original one-line alien tourist review of Earth to
/output/entry.txt as UTF-8 bytes, with no trailing newline.
Deterministic: no network, no randomness, identical bytes every run.
"""

import os

LINE = "Earth review: locals grow grass they never eat, then pay strangers to cut it shorter. Four stars \u2014 lovely lawns, baffling species."

# The competition caps the line at 200 characters; fail loudly if it ever drifts.
assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
