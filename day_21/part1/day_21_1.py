from collections import deque

def parse_map(map_str):
    grid = [list(line) for line in map_str.split('\n') if line.strip() != '']
    start = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
                break
        if start:
            break
    return grid, start

def bfs(grid, start, steps):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set([(start, 0)])
    queue = deque([(start, 0)])
    unique_plots = set()

    while queue:
        position, step = queue.popleft()

        if step == steps:
            unique_plots.add(position)
            continue

        for dx, dy in directions:
            new_x, new_y = position[0] + dx, position[1] + dy

            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                if grid[new_y][new_x] == '.' and (new_x, new_y, step + 1) not in visited:
                    visited.add((new_x, new_y, step + 1))
                    queue.append(((new_x, new_y), step + 1))

    return len(unique_plots) + 1

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_path = 'day_21/part1/input.txt' #'day_21/part1/test.txt'
map_str = read_file(file_path)

grid, start = parse_map(map_str)
result = bfs(grid, start, 64)
print(result)
