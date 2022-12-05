import re

with open("input.txt") as f:
    crates, procedure = [i.split("\n") for i in f.read().split("\n\n")]
    stack_count = len(crates.pop().split("   "))

crates = list(list(crate[1::4]) for crate in crates)
stacks = [list() for _ in range(stack_count)]

for line in crates:
    for idx, val in enumerate(line):
        if val.strip():
            stacks[idx].append(val)

for step in procedure:
    amount, stack, to = map(int, re.findall("[0-9]+", step))
    stacks[to - 1] = stacks[stack - 1][:amount][::-1] + stacks[to - 1]
    stacks[stack - 1] = stacks[stack - 1][amount:]

print("Answer:", "".join(i[0] for i in stacks))
