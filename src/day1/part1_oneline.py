with open("input.txt") as f: print("Answer:", max(map(lambda elf: sum(map(int, elf)), [i.split("\n") for i in f.read().split("\n\n")])))
