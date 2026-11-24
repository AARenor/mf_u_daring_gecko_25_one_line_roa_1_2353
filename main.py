"""Write one short roast for a make.fun bounty to entry.txt.

The text is written as UTF-8 bytes with no trailing newline.
"""

import os
import sys

TEXT = (
    "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
