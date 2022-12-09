with open("input.txt") as f:
    # data looks like: [['A', 'Y'], ['B', 'Z'], ...] (list[list[str]])
    guide = [i.split(" ") for i in f.read().strip().split("\n")]

moves = {
    "X": {"A": 3, "B": 0, "C": 6},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"A": 0, "B": 6, "C": 3},
}  # 0 lost, 3 draw, 6 win

total_score = sum(
    map(lambda game: moves[game[1]][game[0]] + list(moves).index(game[1]) + 1, guide)
)

print("Answer:", total_score)
