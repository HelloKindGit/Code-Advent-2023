import sys

# Increase the recursion limit to handle larger inputs
sys.setrecursionlimit(10000)

def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        map_grid = file.readlines()
        map_grid = [line.strip() for line in map_grid]
    return map_grid

def find_longest_hike(map_grid):
    rows, cols = len(map_grid), len(map_grid[0])
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    max_hike_length = 0

    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and map_grid[x][y] != '#' and not visited[x][y]

    def dfs(x, y, visited, length):
        nonlocal max_hike_length
        max_hike_length = max(max_hike_length, length)

        if map_grid[x][y] in directions: # If current tile is a slope
            slope_dir = directions[map_grid[x][y]]
            next_x, next_y = x + slope_dir[0], y + slope_dir[1]
            if is_valid(next_x, next_y, visited):
                visited[next_x][next_y] = True
                dfs(next_x, next_y, visited, length + 1)
                visited[next_x][next_y] = False
        else: # If current tile is a path
            for dx, dy in directions.values():
                next_x, next_y = x + dx, y + dy
                if is_valid(next_x, next_y, visited):
                    visited[next_x][next_y] = True
                    dfs(next_x, next_y, visited, length + 1)
                    visited[next_x][next_y] = False

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for y in range(cols):
        if map_grid[0][y] == '.':
            visited[0][y] = True
            dfs(0, y, visited, 0)

    return max_hike_length

file_path = 'day_23/part1/input.txt' #'day_23/part1/test.txt'
map_grid = read_map_from_file(file_path)

results = find_longest_hike(map_grid)
print(results)