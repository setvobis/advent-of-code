from collections import deque

with open('input.txt') as file:
    t = file.read().splitlines()


# def heights(char):
#     if char == 'S':
#         return 0
#     elif char == 'E':
#         return 27
#     else:
#         return ord(char) - ord('a') + 1

# Grid = [list(map(heights, line)) for line in t]
# Row = len(Grid)
# Col = len(Grid[0])
# Queue = deque()
# Elevation = []

# for row in range(Row):
#     for col in range(Col):
#         point = Grid[row][col]
#         if point == 0:
#             Queue.append((row, col))
#             print(row, col)

G = [list(line) for line in t]
R = len(G)
C = len(G[0])


E = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            E[r][c] = 1
        elif G[r][c] == 'E':
            E[r][c] = 26
        else:
            E[r][c] = ord(G[r][c])-ord('a')+1


def bfs(part):
    Q = deque()
    for r in range(R):
        for c in range(C):
            if (part == 1 and G[r][c] == 'S') or (part == 2 and E[r][c] == 1):
                Q.append(((r, c), 0))

    S = set()
    while Q:
        (r, c), d = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if G[r][c] == 'E':
            return d
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r+dr
            cc = c+dc
            if 0 <= rr < R and 0 <= cc < C and E[rr][cc] <= 1+E[r][c]:
                Q.append(((rr, cc), d+1))


print(bfs(1))
print(bfs(2))
