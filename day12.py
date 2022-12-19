from collections import deque
from sys import maxsize

grid = []

with open("./inputs/d12.txt") as f:
    for line in f:
        grid.append([c for c in line[:-1]])

def bfs(start: tuple) -> int:
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == 'E':
            return len(path) - 1

        current_elevation = ord('a') if grid[x][y] == 'S' else ord(grid[x][y])

        # get all four neighbors
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y))
        
        if x < len(grid) - 1:
            neighbors.append((x + 1, y))

        if y > 0:
            neighbors.append((x, y - 1))

        if y < len(grid[0]) - 1:
            neighbors.append((x, y + 1))

        for neighbor in neighbors:
            nx, ny = neighbor
            elevation = ord('z') if grid[nx][ny] == 'E' else ord(grid[nx][ny]) 
            if elevation <= current_elevation + 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    return -1

def part1():
    start_char = 'S'

    # find starting location
    start = (-1, -1)
    for i, line in enumerate(grid):
        if start_char in line:
            start = (i, line.index(start_char))
            break
        
    return bfs(start)
    
def part2():
    all_possible_starts = []
    for i in range(len(grid)):
        for j, c in enumerate(grid[i]):
            if c == 'a' or c == 'S':
                all_possible_starts.append((i, j))

    shortest = maxsize
    for start in all_possible_starts:
        path_len = bfs(start)
        shortest = min(shortest, path_len) if path_len != -1 else shortest

    return shortest

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
