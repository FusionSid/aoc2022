with open("input.txt") as f: print("Answer:",sum([1 for pair in [_.split(",") for _ in f.read().strip().split("\n")] if any([[list(map(int, i.split("-"))) for i in pair][0][0] >= [list(map(int, i.split("-"))) for i in pair][1][0] and [list(map(int, i.split("-"))) for i in pair][0][1] <= [list(map(int, i.split("-"))) for i in pair][1][1], [list(map(int, i.split("-"))) for i in pair][0][0] <= [list(map(int, i.split("-"))) for i in pair][1][0] and [list(map(int, i.split("-"))) for i in pair][0][1] >= [list(map(int, i.split("-"))) for i in pair][1][1], [list(map(int, i.split("-"))) for i in pair][0][0] <= [list(map(int, i.split("-"))) for i in pair][1][0] and [list(map(int, i.split("-"))) for i in pair][0][1] >= [list(map(int, i.split("-"))) for i in pair][1][1], [list(map(int, i.split("-"))) for i in pair][0][0] >= [list(map(int, i.split("-"))) for i in pair][1][0] and [list(map(int, i.split("-"))) for i in pair][0][1] <= [list(map(int, i.split("-"))) for i in pair][1][1], [list(map(int, i.split("-"))) for i in pair][1][1] >= [list(map(int, i.split("-"))) for i in pair][0][0] and [list(map(int, i.split("-"))) for i in pair][1][1] <= [list(map(int, i.split("-"))) for i in pair][0][1], [list(map(int, i.split("-"))) for i in pair][0][1] >= [list(map(int, i.split("-"))) for i in pair][1][0] and [list(map(int, i.split("-"))) for i in pair][0][1] <= [list(map(int, i.split("-"))) for i in pair][1][1],])]),)
