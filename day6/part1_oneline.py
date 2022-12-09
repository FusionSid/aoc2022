with open("input.txt") as f: print([char for char in range(4, len(f.read())) if len(set(open("input.txt").read()[char - 4 : char])) == 4][0])
