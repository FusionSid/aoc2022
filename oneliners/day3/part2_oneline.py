with open("input.txt") as f: print("Answer:", sum(map(lambda x: ord(x) - 38 if x.isupper() else ord(x) - 96, [(list(map(set, rucksack))[0] & list(map(set, rucksack))[1] & list(map(set, rucksack))[2]).pop() for rucksack in [open("input.txt").read().strip().split("\n")[i : i + 3] for i in range(0, len(f.read().strip().split("\n")), 3)]],)),)