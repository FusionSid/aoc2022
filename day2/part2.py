with open("input.txt") as f:
    # data looks like: [['A', 'Y'], ['B', 'Z'], ...] (list[list[str]])
    guide = [i.split(" ") for i in f.read().strip().split("\n")]

moves = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}
what_to_do = {"X": 0, "Y": 3, "Z": 6}

total_score = sum(
    map(lambda game: moves[game[0]][game[1]] + what_to_do[game[1]], guide)
)

print("Answer:", total_score)
