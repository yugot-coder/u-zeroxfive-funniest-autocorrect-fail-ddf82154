#!/usr/bin/env python3
"""make.fun entry: Funniest Autocorrect Fail (one line, stdlib only)."""
import hashlib
import os
import sys

ENTRY = "Texted my mom: 'Can't talk, I'm in a meeting with Satan' \u2014 I meant SARAH, my manager. Mom screenshot it straight to Sarah."


def main() -> int:
    if not 1 <= len(ENTRY) <= 199:
        raise SystemExit(f"entry length {len(ENTRY)} outside 1..199 gate")
    data = (ENTRY + "\n").encode("utf-8")
    expected = hashlib.sha256(data).hexdigest()
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as fh:
            fh.write(data)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as fh:
            fh.write(data)
    with open(out_path, "rb") as fh:
        written = fh.read()
    digest = hashlib.sha256(written).hexdigest()
    if written != data or digest != expected:
        raise SystemExit(f"read-back mismatch: wrote {expected}, read {digest}")
    print(f"wrote {out_path} ({len(written)} bytes) sha256={digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
