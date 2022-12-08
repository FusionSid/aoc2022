with open("input.txt") as f:
    grid = [list(map(int, line)) for line in f.read().split("\n")]

visible_trees = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        tree_height = grid[row][column]

        checks = [
            all(grid[row][i] < tree_height for i in range(column)),
            all(grid[row][i] < tree_height for i in range(column + 1, len(grid[row]))),
            all(grid[i][column] < tree_height for i in range(row)),
            all(grid[i][column] < tree_height for i in range(row + 1, len(grid))),
        ]
        visible_trees += 1 if any(checks) else 0

print("Answer:", visible_trees)
