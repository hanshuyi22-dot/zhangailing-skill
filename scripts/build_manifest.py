#!/usr/bin/env python3
"""Build a markdown manifest from a folder of txt files.

Usage:
    python build_manifest.py <txt_dir> <output_md>
"""

from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python build_manifest.py <txt_dir> <output_md>")
        return 1

    txt_dir = Path(sys.argv[1]).resolve()
    output_md = Path(sys.argv[2]).resolve()

    if not txt_dir.exists() or not txt_dir.is_dir():
        print(f"Error: txt_dir not found or not a directory: {txt_dir}")
        return 1

    files = sorted(
        p.name
        for p in txt_dir.iterdir()
        if p.is_file() and p.suffix.lower() == ".txt"
    )

    lines = [
        "# TXT Manifest",
        "",
        f"Total files: {len(files)}",
        "",
        "## Files",
        "",
    ]
    lines.extend(f"- {name}" for name in files)
    lines.append("")

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote manifest to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
