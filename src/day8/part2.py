with open("input.txt") as f:
    grid = [list(map(int, line)) for line in f.read().split("\n")]

total = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        tree_height = grid[row][column]
        l, r, u, d = (0, 0, 0, 0)

        for i in range(column - 1, -1, -1):
            l += 1
            if grid[row][i] >= tree_height:
                break

        for i in range(column + 1, len(grid[row])):
            r += 1
            if grid[row][i] >= tree_height:
                break
        for i in range(row - 1, -1, -1):
            u += 1
            if grid[i][column] >= tree_height:
                break

        for i in range(row + 1, len(grid)):
            d += 1
            if grid[i][column] >= tree_height:
                break

        total = max(total, l * r * u * d)

print("Answer:", total)
