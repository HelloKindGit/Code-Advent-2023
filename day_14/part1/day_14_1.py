def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def tilt_platform(platform):
    transposed_platform = ["".join(row) for row in zip(*platform)]
    tilted_cols = []

    for col in transposed_platform:
        parts = col.split("#")
        parts_tilted = [("O" * t.count("O")).ljust(len(t), ".") for t in parts]
        tilted_cols.append("#".join(parts_tilted))

    platform_tilted = [list(x) for x in zip(*tilted_cols)]

    # Update the original platform with the tilted one
    for i, row in enumerate(platform):
        row[:] = platform_tilted[i][:]

def calculate_total_load(platform):
    height = len(platform)
    return sum((height - i) * sum(1 for c in cell if c == "O") for i, cell in enumerate(platform))

def start_calc():
    file_path = 'day_14/part1/input.txt' #'day_14/part1/test.txt'
    platform_data = read_input(file_path)
    platform = [list(line) for line in platform_data]

    tilt_platform(platform)
    total_load = calculate_total_load(platform)

    return total_load

result = start_calc()
print(result)
