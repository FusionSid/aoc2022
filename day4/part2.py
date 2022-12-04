with open("input.txt") as f:
    assignments = [i.split(",") for i in f.read().strip().split("\n")]

answer = 0
for pair in assignments:
    left, right = [list(map(int, i.split("-"))) for i in pair]
    l1, l2, r1, r2 = left + right
    cases = [
        l1 <= r1 and l2 >= r2,
        l1 >= r1 and l2 <= r2,
        r2 >= l1 and r2 <= l2,
        l2 >= r1 and l2 <= r2,
    ]
    if any(cases):
        answer += 1

print("Answer:", answer)
