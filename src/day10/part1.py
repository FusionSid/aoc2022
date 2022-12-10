with open("test.txt") as f:
    instructions = [i.split(" ") for i in f.read().split("\n")]

x = 1
cycle_count = 0
signal_strengths: list[int] = []


def check():
    global cycle_count
    cycle_count += 1
    CHECK_CYCLES = [20, 60, 100, 140, 180, 220]
    if cycle_count in CHECK_CYCLES:
        signal_strengths.append(CHECK_CYCLES[CHECK_CYCLES.index(cycle_count)] * x)


for instruction in instructions:
    check()
    if instruction[0] == "noop":
        continue
    check()

    value = int(instruction[1])
    x += value

print("Answer:", sum(signal_strengths))
