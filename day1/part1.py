with open("input.txt") as f:
    elves = f.read().split("\n\n")
    elves = [i.split("\n") for i in elves]

highest = 0

for elf in elves:
    count = sum(map(int, elf))
    if count > highest:
        highest = count

print("Answer: ", highest)
