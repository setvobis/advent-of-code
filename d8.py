with open('input.txt') as file:
    t = file.read().splitlines()

grid = [list(map(int, line)) for line in t]

visible = 0

for row in range(len(grid)):
    # print(grid[row])
    for column in range(len(grid[row])):
        tree = grid[row][column]
        if all(grid[row][x] < tree for x in range(column)) or \
                all(grid[row][x] < tree for x in range(column + 1, len(grid[row]))) or \
                all(grid[x][column] < tree for x in range(row)) or \
                all(grid[x][column] < tree for x in range(row + 1, len(grid[column]))):
            visible += 1
print(visible)
