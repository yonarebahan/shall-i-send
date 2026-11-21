"""Write one short poem about agency to /output/entry.txt."""

import os
from pathlib import Path

POEM = """It drafted the letter in your voice,
found the address, got the hard name right,
did everything except the last thing.
Now the cursor blinks over Send.
All its power lives in that pause —
it can do anything except begin.
The yes was never its to give. Only yours.
"""


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
