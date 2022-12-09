with open("input.txt") as f:
    rucksacks = f.read().strip().split("\n")
    rucksacks = [
        rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)
    ]  # split into chunks of 3

common_letters = []
for rucksack in rucksacks:
    groups = list(map(set, rucksack))
    common = (groups[0] & groups[1] & groups[2]).pop()
    common_letters.append(common)

get_value = lambda x: ord(x) - 38 if x.isupper() else ord(x) - 96
print("Answer:", sum(map(get_value, common_letters)))
