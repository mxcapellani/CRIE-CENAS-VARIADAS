#!/usr/bin/env python3
"""Exact ratio from supplied dimensions; does not infer dimensions from pixels."""
from math import gcd
import argparse

def aspect_ratio(width, height):
    if isinstance(width, bool) or isinstance(height, bool) or not isinstance(width, int) or not isinstance(height, int) or width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    divisor = gcd(width, height)
    return f"{width // divisor}:{height // divisor}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    args = parser.parse_args()
    try:
        print(aspect_ratio(args.width, args.height))
    except ValueError as exc:
        parser.error(str(exc))
