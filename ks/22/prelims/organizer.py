import os
from glob import glob
from os.path import abspath, dirname

os.chdir(dirname(abspath(__file__)))

files = glob("*.py")
for file in files:
    if file == "organizer.py":
        continue
    problem = file[:-3]
    os.mkdir(problem)
    os.rename(file, f"./{problem}/solution.py")
    if os.path.exists(f"./in/{problem}.txt"):
        os.rename(f"./in/{problem}.txt", f"./{problem}/input.txt")
