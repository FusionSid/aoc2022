with open("input.txt") as f:
    instructions = [i.split(" ") for i in f.read().split("\n")]

cycle_count = 0
sprite_position = 1
signal_strengths: list[int] = []


def draw():
    global cycle_count
    cycle_count += 1

    # if over 40 use the mod 40 count instead
    if cycle_count > 40:
        cycle_count %= 40

    # check what type of pixel to draw
    if cycle_count in [sprite_position, sprite_position + 1, sprite_position + 2]:
        print("#", end="")
    else:
        print(".", end="")

    # check if to draw a new line
    if cycle_count % 40 == 0:
        print()


for instruction in instructions:
    draw()
    if instruction[0] == "noop":
        continue
    draw()

    value = int(instruction[1])
    sprite_position += value
