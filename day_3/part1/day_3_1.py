from collections import defaultdict

def read_engine_schematic(file_path):
    data = open(file_path).read().strip()
    return [[c for c in line] for line in data.split('\n')]

def calculate_result(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = 0
    adjacent_numbers = defaultdict(list)

    for r in range(rows):
        gears = set()  # positions of '*' characters next to the current number
        current_number = 0
        has_part = False

        for c in range(cols + 1):
            if c < cols and grid[r][c].isdigit():
                current_number = current_number * 10 + int(grid[r][c])
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < rows and 0 <= c + dc < cols:
                            char = grid[r + dr][c + dc]
                            if not char.isdigit() and char != '.':
                                has_part = True
                            if char == '*':
                                gears.add((r + dr, c + dc))
            elif current_number > 0:
                for gear in gears:
                    adjacent_numbers[gear].append(current_number)
                if has_part:
                    result += current_number
                current_number = 0
                has_part = False
                gears = set()

    return result

# Example usage
file_path = 'day_3/part1/input.txt' #'day_3/part1/test.txt'
grid = read_engine_schematic(file_path)
result = calculate_result(grid)

print(result)
