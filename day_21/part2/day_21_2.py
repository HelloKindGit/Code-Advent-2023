from collections import deque

def read_grid(file_path):
    with open(file_path) as file:
        lines = file.read().strip().split('\n')
    return [[char for char in row] for row in lines]

def find_start_position(grid):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == 'S':
                return r, c

def find_distances(grid, start_row, start_col):
    distances = {}
    queue = deque([(0, 0, start_row, start_col, 0)])
    row_count, col_count = len(grid), len(grid[0])

    while queue:
        trans_row, trans_col, row, col, dist = queue.popleft()
        row, trans_row = (row + row_count) % row_count, trans_row + (row < 0) - (row >= row_count)
        col, trans_col = (col + col_count) % col_count, trans_col + (col < 0) - (col >= col_count)
        
        if not (0 <= row < row_count and 0 <= col < col_count and grid[row][col] != '#'):
            continue
        if (trans_row, trans_col, row, col) in distances or abs(trans_row) > 4 or abs(trans_col) > 4:
            continue

        distances[(trans_row, trans_col, row, col)] = dist
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            queue.append((trans_row, trans_col, row + dr, col + dc, dist + 1))
    
    return distances

def solve(distances, row_count, step_limit, part_one):
    solve_cache = {}
    ans = 0
    opt_range = [-3, -2, -1, 0, 1, 2, 3]

    def is_corner(trans_row, trans_col):
        return trans_row in {min(opt_range), max(opt_range)} and trans_col in {min(opt_range), max(opt_range)}

    def is_edge(trans_row, trans_col):
        return trans_row in {min(opt_range), max(opt_range)} or trans_col in {min(opt_range), max(opt_range)}

    for r in range(row_count):
        for c in range(row_count):
            if (0, 0, r, c) not in distances:
                continue

            for trans_row in opt_range:
                for trans_col in opt_range:
                    if part_one and (trans_row != 0 or trans_col != 0):
                        continue

                    d = distances[(trans_row, trans_col, r, c)]
                    if d % 2 == step_limit % 2 and d <= step_limit:
                        ans += 1

                    value = 2 if is_corner(trans_row, trans_col) else 1 if is_edge(trans_row, trans_col) else 0
                    if value:
                        ans += calculate_additional_paths(d, value, step_limit, row_count, solve_cache)

    return ans

def calculate_additional_paths(d, value, step_limit, row_count, cache):
    if (d, value, step_limit) in cache:
        return cache[(d, value, step_limit)]

    amount = (step_limit - d) // row_count
    result = 0
    for x in range(1, amount + 1):
        if d + row_count * x <= step_limit and (d + row_count * x) % 2 == (step_limit % 2):
            result += (x + 1) if value == 2 else 1

    cache[(d, value, step_limit)] = result
    return result

file_path = 'day_21/part2/input.txt' #'day_21/part2/test.txt'
grid = read_grid(file_path)
start_row, start_col = find_start_position(grid)
distances = find_distances(grid, start_row, start_col)
step_limit = 26501365
print(solve(distances, len(grid), step_limit, part_one=False))
