import importlib.util
import sys
from argparse import ArgumentParser
from os import chdir
from os.path import isdir, isfile

parser = ArgumentParser()
parser.add_argument("-y", "--year", help="Year of challenge", type=int, required=True)
parser.add_argument("-d", "--day", help="Day of AoC [1-25]", type=int, required=True)
parser.add_argument(
    "-p", "--part", help="Part of the challenge [1-2]", type=int, choices=[1, 2], required=True
)
args = parser.parse_args()
if args.day < 1 or args.day > 25:
    parser.error("Day must be between 1 and 25")
    sys.exit(1)


if not isdir(f"./{args.year}"):
    print(f"Directory {args.year} not found")
    sys.exit(1)
chdir(f"./{args.year}")

if not isdir(f"./{args.day:02}"):
    print(f"Solution directory for day {args.day} of {args.year} not found")
    sys.exit(1)
chdir(f"./{args.day:02}")

if not isfile("./solution.py"):
    print(f"Solution file for day {args.day} of {args.year} not found")
    sys.exit(1)
if not isfile("./input.txt"):
    print(f"Input file for day {args.year}/{args.day:02} not found")
    sys.exit(1)

spec = importlib.util.spec_from_file_location("solution", "./solution.py")
if spec is None:
    raise Exception("Could not import solution")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)  # type: ignore

if args.part == 1:
    print(module.part1())
else:
    print(module.part2())
