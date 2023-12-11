from collections import deque

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def expand_universe(data):
    galaxies = []

    expand_rows = set()
    expand_cols = set()

    for r, line in enumerate(data):
        if "#" in line:
            for c, v in enumerate(line):
                if v == "#":
                    galaxies.append((r, c))
        else:
            expand_rows.add(r)

    for c, col in enumerate(zip(*data)):
        if "#" not in col:
            expand_cols.add(c)

    return galaxies

def find_neighbors(expanded_image, i, j):
    neighbors = []
    if i > 0 and expanded_image[i - 1][j] == '#':
        neighbors.append((i - 1, j))
    if i < len(expanded_image) - 1 and expanded_image[i + 1][j] == '#':
        neighbors.append((i + 1, j))
    if j > 0 and expanded_image[i][j - 1] == '#':
        neighbors.append((i, j - 1))
    if j < len(expanded_image[0]) - 1 and expanded_image[i][j + 1] == '#':
        neighbors.append((i, j + 1))
    return neighbors

def calculate_shortest_path(expanded_image, start, end):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        (i, j), steps = queue.popleft()

        if (i, j) == end:
            return steps

        if (i, j) not in visited:
            visited.add((i, j))
            for neighbor in find_neighbors(expanded_image, i, j):
                queue.append((neighbor, steps + 1))

    return float('inf')

def calculate_sum_of_shortest_paths(galaxies, expand_level, expand_rows, expand_cols):
    total_shortest_paths = 0

    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            y1, x1 = galaxies[i]
            y2, x2 = galaxies[j]

            y1, y2 = sorted([y1, y2])
            x1, x2 = sorted([x1, x2])

            w = x2 - x1
            h = y2 - y1

            cols = sum([1 for c in expand_cols if x1 < c < x2])
            rows = sum([1 for r in expand_rows if y1 < r < y2])

            total_shortest_paths += w + h + (expand_level - 1) * (cols + rows)

    return total_shortest_paths

def calculate_paths(file_path, expand_level):
    data = read_input_from_file(file_path)
    galaxies = expand_universe(data)

    expand_rows = {r for r, line in enumerate(data) if "#" not in line}
    expand_cols = {c for c, col in enumerate(zip(*data)) if "#" not in col}

    total_shortest_paths = calculate_sum_of_shortest_paths(
        galaxies, expand_level, expand_rows, expand_cols
    )

    return total_shortest_paths


file_path = "day_11/part2/input.txt" # "day_11/part2/test.txt"
expand_level = 1000000
result = calculate_paths(file_path, expand_level)
print(result)