with open("input.txt") as f:
    motions = [i.split(" ") for i in f.read().split("\n")]

head_pos = [0, 0]
tail_pos = [0, 0]
spots_tail_visited = []

for line in motions:
    direction = line[0]
    move_amount = int(line[1])
    for _ in range(move_amount):
        match direction:
            case "L":
                head_pos[0] -= 1
            case "R":
                head_pos[0] += 1
            case "U":
                head_pos[1] += 1
            case "D":
                head_pos[1] -= 1

        if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
            if head_pos[0] != tail_pos[0]:
                tail_pos[0] += (
                    0
                    if head_pos[0] == tail_pos[0]
                    else (head_pos[0] - tail_pos[0]) / abs(head_pos[0] - tail_pos[0])
                )
            if head_pos[1] != tail_pos[1]:
                tail_pos[1] += (
                    0
                    if head_pos[1] == tail_pos[1]
                    else (head_pos[1] - tail_pos[1]) / abs(head_pos[1] - tail_pos[1])
                )

        spots_tail_visited.append(tuple(tail_pos))

print("Answer:", len(set(spots_tail_visited)))
