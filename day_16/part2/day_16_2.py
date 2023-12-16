from collections import deque

def read_grid_from_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]

def simulate_light_beam(grid, start_row, start_col, start_dir):
    height, width = len(grid), len(grid[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    interaction_map = {
        '.': lambda d: [d],
        '\\': lambda d: [d + (-1) ** d],
        '/': lambda d: [3 - d],
        '-': lambda d: [(d + 1) % 4, (d + 3) % 4] if d % 2 else [d],
        '|': lambda d: [d] if d % 2 else [(d + 1) % 4, (d + 3) % 4]
    }

    beam_queue = deque([((start_row, start_col), start_dir)])
    energized = set()
    visited = set()

    while beam_queue:
        position, dir_idx = beam_queue.popleft()

        if (position, dir_idx) in visited:
            continue

        visited.add((position, dir_idx))
        row, col = position
        energized.add((row, col))

        current_tile = grid[row][col]
        next_dirs = interaction_map[current_tile](dir_idx)

        for nd in next_dirs:
            new_row, new_col = row + directions[nd][0], col + directions[nd][1]
            if 0 <= new_row < height and 0 <= new_col < width:
                next_state = ((new_row, new_col), nd)
                if next_state not in visited:
                    beam_queue.append(next_state)

    return len(energized)

def find_best_start_configuration(grid):
    height, width = len(grid), len(grid[0])
    max_energized = 0

    # Top row (heading downwards)
    for col in range(width):
        energized = simulate_light_beam(grid, 0, col, 1)  # Direction index for 'down' is 1
        max_energized = max(max_energized, energized)

    # Bottom row (heading upwards)
    for col in range(width):
        energized = simulate_light_beam(grid, height - 1, col, 3)  # Direction index for 'up' is 3
        max_energized = max(max_energized, energized)

    # Leftmost column (heading right)
    for row in range(height):
        energized = simulate_light_beam(grid, row, 0, 0)  # Direction index for 'right' is 0
        max_energized = max(max_energized, energized)

    # Rightmost column (heading left)
    for row in range(height):
        energized = simulate_light_beam(grid, row, width - 1, 2)  # Direction index for 'left' is 2
        max_energized = max(max_energized, energized)

    return max_energized

file_path = 'day_16/part2/input.txt'  #'day_16/part2/test.txt'
input_grid = read_grid_from_file(file_path)

result = find_best_start_configuration(input_grid)
print(result)
