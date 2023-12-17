import heapq

def read_grid_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid

def find_min_heat_loss(grid, minimum_step_before_turn=4, maximum_consecutive_steps=10):
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = {}  # {(position, direction): heat loss}
    priority_queue = [(0, start, -1)]  # (heat loss, position, direction)

    while priority_queue:
        heat_loss, position, direction = heapq.heappop(priority_queue)
        if position == end:
            return heat_loss

        allowed_directions = [_d for _d in range(4) if _d != direction and (_d + 2) % 4 != direction]

        for new_direction in allowed_directions:
            # Generate potential new positions, heat losses, and steps
            positions_losses_steps = (
                (tuple(position[p] + directions[new_direction][p] * step for p in range(2)),
                 heat_loss + sum(int(grid[min(rows - 1, max(0, position[0] + directions[new_direction][0] * s))][min(cols - 1, max(0, position[1] + directions[new_direction][1] * s))]) for s in range(1, step + 1)))
                for step in range(minimum_step_before_turn, maximum_consecutive_steps + 1)
            )

            # Check each potential position, heat loss, and step
            for next_position, next_loss in positions_losses_steps:
                if 0 <= next_position[0] < rows and 0 <= next_position[1] < cols:
                    if next_loss < visited.get((next_position, new_direction), float("inf")):
                        visited[(next_position, new_direction)] = next_loss
                        heapq.heappush(priority_queue, (next_loss, next_position, new_direction))

    return float("inf")

file_path = 'day_17/part2/input.txt' #'day_17/part2/test.txt'
grid = read_grid_from_file(file_path)

result = find_min_heat_loss(grid)
print(result)