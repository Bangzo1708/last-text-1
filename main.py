#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the dying phone's final text message to entry.txt.
One message, in the phone's own voice, no explanation, no waste.
"""

import os

# The phone's last text: it spends its final 1% doing something
# drastic on its owner's behalf, then signs off.
TEXT = "1%. I just texted your boss 'I quit' for you. You're free now. Goodbye."


def main():
    # Fail loudly instead of ever writing an entry the gate would refuse.
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        raise ValueError("entry text must be 1-200 non-blank characters")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
