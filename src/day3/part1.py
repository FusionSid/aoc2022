with open("input.txt") as f:
    rucksacks = f.read().strip().split("\n")

common_letters = []
for rucksack in rucksacks:
    length = len(rucksack) // 2
    common = (set(rucksack[:length]) & set(rucksack[length:])).pop()
    common_letters.append(common)

get_value = lambda x: ord(x) - 38 if x.isupper() else ord(x) - 96
print("Answer:", sum(map(get_value, common_letters)))
