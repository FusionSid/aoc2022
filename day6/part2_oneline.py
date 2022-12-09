with open("input.txt") as f: print([char for char in range(14, len(f.read())) if len(set(open("input.txt").read()[char - 14 : char])) == 14][0])
