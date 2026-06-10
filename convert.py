#!/usr/bin/env python3
"""Command-line file format converter.

Usage:
    python convert.py input.xml output.xlsx
"""
import argparse
import sys
from pathlib import Path

from converters import get_converter, supported_conversions


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert files between formats.")
    parser.add_argument("input", type=Path, help="path to the input file")
    parser.add_argument("output", type=Path, help="path to the output file")
    args = parser.parse_args()

    if not args.input.exists():
        sys.exit(f"Input file not found: {args.input}")

    input_format = args.input.suffix.lower().lstrip(".")
    output_format = args.output.suffix.lower().lstrip(".")

    converter = get_converter(input_format, output_format)
    if converter is None:
        supported = ", ".join(f"{i} -> {o}" for i, o in supported_conversions())
        sys.exit(
            f"No converter available for '{input_format}' -> '{output_format}'.\n"
            f"Supported conversions: {supported}"
        )

    converter(args.input, args.output)
    print(f"Converted {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
