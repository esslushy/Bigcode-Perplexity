from argparse import ArgumentParser
import itertools
from pathlib import Path

def read_file(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()
    
args = ArgumentParser()
args.add_argument("--input", help="The base file path to draw from", required=True, type=Path)
args.add_argument("--extension", help="The extension of files to get", required=True, type=str)
args.add_argument("--out", help="Output file for code", required=True, type=str)
args = args.parse_args()

all_files = "".join([ read_file(p) for p in itertools.chain(Path(args.input).rglob(f"*.{args.extension}"))])

with open(args.out, "wt+") as f:
    f.write(all_files)