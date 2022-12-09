with open("input.txt") as f:
    elves = f.read().split("\n\n")
    elves = [i.split("\n") for i in elves]

highest = [0 for _ in range(3)]  # makes changing number easier then 0,0,0

for elf in elves:
    count = sum(map(int, elf))
    for i in range(len(highest)):
        if count > highest[i]:
            highest[i] = count
            break

print("Answer: ", sum(highest))
