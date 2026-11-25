"""Have You Tried Turning It Off? — make.fun entry.

Writes a single funny line a hopeless tech support agent says to a
desperate customer, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = "Good news — I've escalated your case to Tier 2. Bad news — Tier 2 is also me, but with a different headset."

# Gate from the competition rules: UTF-8 text, 1 to 199 characters,
# a single line, plain text.
def validate(text):
    assert 1 <= len(text) <= 199, f"entry length {len(text)} outside 1..199"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
