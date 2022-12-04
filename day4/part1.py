with open("input.txt") as f:
    assignments = [i.split(",") for i in f.read().strip().split("\n")]

answer = 0
for pair in assignments:
    left, right = [list(map(int, i.split("-"))) for i in pair]
    l1, l2, r1, r2 = left + right
    if l1 >= r1 and l2 <= r2:
        answer += 1
    elif l1 <= r1 and l2 >= r2:
        answer += 1

print("Answer:", answer)
