"""
Caleb Ellington
CSE 427: Computational Biology
01/25/2020

Usage: align.py <sequence1.file> <sequence2.file>

"""

import sys
import argparse
from os.path import isdir, isfile
from model import Alignment


def main():
    parser = argparse.ArgumentParser(description="Protein/DNA alignment")

    parser.add_argument(
        "file1",
        action="store",
        help="Location of the first sequence file to align",
    )

    parser.add_argument(
        "file2",
        action="store",
        help="Location of the second sequence file to align",
    )

    parser.add_argument(
        "--protein",
        "-p",
        action="store_true",
        default=False,
        help="Protein file flag",
    )

    args = parser.parse_args()
    if not (isfile(args.file1) and isfile(args.file2)):
        print("Invalid sequence path")

    alignment_model = Alignment(args.file1, args.file2, args.protein)




if __name__ == '__main__':
    main()

