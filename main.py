"""Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt for the Make.fun
bounty u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.
Stdlib only.
"""

import os

LINE = (
    "The senator drafting the AI safety bill had his aide convert the "
    "draft to PDF, print it, scan it back in, and email it to himself "
    "as a photo of the screen."
)


def verify():
    """Re-read the output and assert the gate: 1-320 chars, one sentence,
    non-whitespace, byte-identical to LINE."""
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE, "output is not byte-identical to LINE"
    assert content.strip(), "output is only whitespace"
    assert 1 <= len(content) <= 320, f"length {len(content)} out of range"
    assert content.count(".") == 1 and content.endswith("."), (
        "entry must be exactly one sentence ending in a single period"
    )
    return len(content)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {verify()} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
