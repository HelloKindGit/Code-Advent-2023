import heapq

def read_grid_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid

def find_min_heat_loss(grid, minimum_step_before_turn=1, maximum_consecutive_steps=3):
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = {}
    priority_queue = [(0, start, -1)]

    while priority_queue:
        heat_loss, position, direction = heapq.heappop(priority_queue)
        if position == end:
            return heat_loss
        
        allowed_directions = [_d for _d in range(4) if _d != direction and (_d + 2) % 4 != direction]

        for new_direction in allowed_directions:
            new_position = position
            new_heat_loss = heat_loss
            for steps in range(1, maximum_consecutive_steps + 1):
                new_position = tuple(p + d for p, d in zip(new_position, directions[new_direction]))
                if not (0 <= new_position[0] < rows and 0 <= new_position[1] < cols):
                    break
                new_heat_loss += int(grid[new_position[0]][new_position[1]])
                if steps >= minimum_step_before_turn:
                    if new_heat_loss < visited.get((new_position, new_direction), float("inf")):
                        visited[(new_position, new_direction)] = new_heat_loss
                        heapq.heappush(priority_queue, (new_heat_loss, new_position, new_direction))

    return float("inf")

file_path = 'day_17/part1/input.txt' #'day_17/part1/test.txt'
grid = read_grid_from_file(file_path)

result = find_min_heat_loss(grid)
print(result)