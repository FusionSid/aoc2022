with open("input.txt") as f: print("Answer:", sum(sorted(map(lambda elf: sum(map(int, elf)), [i.split("\n") for i in f.read().split("\n\n")]))[::-1][:3]))
