from collections import deque

def read_grid_from_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]

def simulate_light_beam(grid):
    height, width = len(grid), len(grid[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_map = {'R': 0, 'D': 1, 'L': 2, 'U': 3}

    interaction_map = {
        '.': lambda d: [d],
        '\\': lambda d: [d + (-1) ** d],
        '/': lambda d: [3 - d],
        '-': lambda d: [(d + 1) % 4, (d + 3) % 4] if d % 2 else [d],
        '|': lambda d: [d] if d % 2 else [(d + 1) % 4, (d + 3) % 4]
    }

    beam_queue = deque([((0, 0), dir_map['R'])])
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

file_path = 'day_16/part1/input.txt'  #'day_16/part1/test.txt'
input_grid = read_grid_from_file(file_path)
result = simulate_light_beam(input_grid)
print(result)
