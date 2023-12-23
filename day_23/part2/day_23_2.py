from collections import deque, defaultdict
import sys

# Increase the recursion limit to handle larger inputs
sys.setrecursionlimit(10000)

def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        map_grid = file.readlines()
        map_grid = [line.strip() for line in map_grid]
    return map_grid

def create_graph(map_grid):
    rows, cols = len(map_grid), len(map_grid[0])
    graph = defaultdict(list)
    vertices = set()

    # Identify vertices and start/end points
    for r in range(rows):
        for c in range(cols):
            if map_grid[r][c] == '.':
                nbr_count = sum(
                    0 <= r + dr < rows and 0 <= c + dc < cols and map_grid[r + dr][c + dc] != '#'
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                )
                if nbr_count > 2 or r in [0, rows - 1]:
                    vertices.add((r, c))

    # Create edges between vertices
    for rv, cv in vertices:
        queue = deque([(rv, cv, 0)])
        seen = set()

        while queue:
            r, c, dist = queue.popleft()
            if (r, c) in seen:
                continue
            seen.add((r, c))

            if (r, c) in vertices and (r, c) != (rv, cv):
                graph[(rv, cv)].append(((r, c), dist))
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and map_grid[r + dr][c + dc] != '#':
                    queue.append((r + dr, c + dc, dist + 1))

    # Identify start and end points
    start_points = [(r, c) for r, c in vertices if r == 0]
    end_points = [(r, c) for r, c in vertices if r == rows - 1]

    return graph, start_points, end_points

def find_longest_path(graph, start_points, end_points, grid_size):
    max_length = 0
    rows, cols = grid_size
    visited_global = [[False] * cols for _ in range(rows)]

    def dfs(v, length):
        nonlocal max_length
        r, c = v
        if visited_global[r][c]:
            return
        visited_global[r][c] = True

        if v in end_points:
            max_length = max(max_length, length)

        for (next_v, dist) in graph[v]:
            dfs(next_v, length + dist)

        visited_global[r][c] = False

    for start in start_points:
        dfs(start, 0)

    return max_length

file_path = 'day_23/part2/input.txt' #'day_23/part2/test.txt'
map_grid = read_map_from_file(file_path)

efficient_graph, start_points, end_points = create_graph(map_grid)
grid_size = (len(map_grid), len(map_grid[0]))
results = find_longest_path(efficient_graph, start_points, end_points, grid_size)
print(results)