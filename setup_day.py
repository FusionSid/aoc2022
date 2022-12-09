import os
import webbrowser
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

day = int(input("Enter day: "))
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src/")

os.mkdir(f"{path}day{day}")  # make directory for code
path = os.path.join(path, f"day{day}")  # set path to the folder

response = requests.get(
    f"https://adventofcode.com/2022/day/{day}/input",
    headers={"cookie": f"session={os.environ.get('SESSION')}"},
)  # get input for day
with open(f"{path}/input.txt", "w") as f:
    f.write(response.text.strip())  # save input to file

# create other files for day
Path(f"{path}/part1.py").touch()
Path(f"{path}/part2.py").touch()
Path(f"{path}/test.txt").touch()

# open problem statement
webbrowser.open(f"https://adventofcode.com/2022/day/{day}")
