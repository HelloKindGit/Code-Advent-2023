from collections import defaultdict

def read_engine_schematic(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def calculate_result(grid):
    rows, cols = len(grid), len(grid[0])

    result = 0
    adjacent_numbers = defaultdict(list)

    for r in range(rows):
        gears = set()  # positions of '*' characters next to the current number
        current_number = 0

        for c in range(cols + 1):
            if c < cols and grid[r][c].isdigit():
                current_number = current_number * 10 + int(grid[r][c])
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        if 0 <= r + row_offset < rows and 0 <= c + col_offset < cols:
                            char = grid[r + row_offset][c + col_offset]
                            if char == '*':
                                gears.add((r + row_offset, c + col_offset))
            elif current_number > 0:
                for gear in gears:
                    adjacent_numbers[gear].append(current_number)
                current_number = 0
                gears = set()

    for _, v in adjacent_numbers.items():
        if len(v) == 2:
            result += v[0] * v[1]

    return result

# Example usage
file_path = 'day_3/part2/input.txt'
grid = read_engine_schematic(file_path)
results = calculate_result(grid)

print(results)