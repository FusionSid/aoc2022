with open("input.txt") as f: print("Answer:", sum(map(lambda game: {"A": {"X": 3, "Y": 1, "Z": 2}, "B": {"X": 1, "Y": 2, "Z": 3}, "C": {"X": 2, "Y": 3, "Z": 1},}[game[0]][game[1]] + {"X": 0, "Y": 3, "Z": 6}[game[1]], [i.split(" ") for i in f.read().strip().split("\n")])))
