def read_engine_schematic(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def calculate_result(grid):
    rows, cols = len(grid), len(grid[0])

    result = 0

    for r in range(rows):
        current_number = 0
        has_part = False
        for c in range(cols + 1):
            if c < cols and grid[r][c].isdigit():
                current_number = current_number * 10 + int(grid[r][c])
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        if 0 <= r + row_offset < rows and 0 <= c + col_offset < cols:
                            char = grid[r + row_offset][c + col_offset]
                            if not char.isdigit() and char != '.':
                                has_part = True
            elif current_number > 0:
                if has_part:
                    result += current_number
                current_number = 0
                has_part = False

    return result

# Example usage
file_path = 'day_3/part1/input.txt' #'day_3/part1/test.txt'
grid = read_engine_schematic(file_path)
result = calculate_result(grid)

print(result)
