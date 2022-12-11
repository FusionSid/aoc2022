import re
import math


class Monkey:
    def __init__(self, monkey_data: str):
        self.items = list(map(int, re.findall("\\d+", monkey_data[1])))
        self.operation = monkey_data[2].split("= ")[1]
        self.divisible_by = int(re.findall("\\d+", monkey_data[3])[0])
        self.throw_to = list(
            map(int, re.findall("\\d+", monkey_data[4] + monkey_data[5]))
        )
        self.inspected = 0

    def __repr__(self):
        return f'({self.inspected}): {", ".join(map(str, self.items))}'


with open("input.txt") as f:
    monkey_notes = [i.split("\n") for i in f.read().split("\n\n")]
    monkeys = [Monkey(monkey) for monkey in monkey_notes]

ROUND_COUNT = 10000
manage = 1
for monkey in monkeys:
    manage *= monkey.divisible_by

for round in range(ROUND_COUNT):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1
            worry = eval(monkey.operation, None, {"old": item}) % manage
            if worry % monkey.divisible_by == 0:
                monkeys[monkey.throw_to[0]].items.append(worry)
                continue
            monkeys[monkey.throw_to[1]].items.append(worry)
        monkey.items = []


active_monkeys = math.prod(sorted(map(lambda m: m.inspected, monkeys))[-2:])

print("\n".join(f"Monkey {idx} {monkey}" for idx, monkey in enumerate(monkeys)))
print("\nAnswer:", active_monkeys)
