def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

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

def turn_platform(platform):
    platform[:] = [list(x)[::-1] for x in zip(*platform)]

def calculate_total_load(platform):
    height = len(platform)
    return sum((height - i) * sum(1 for c in cell if c == "O") for i, cell in enumerate(platform))

def simulate_spin_cycles(platform, num_cycles):
    cache = {}

    for cycle_idx in range(num_cycles):
        for _ in range(4):
            tilt_platform(platform)
            turn_platform(platform)

        platform_hash = hash("".join("".join(x) for x in platform))

        if platform_hash not in cache:
            cache[platform_hash] = cycle_idx
        else:
            diff = cycle_idx - cache[platform_hash]
            head = cache[platform_hash]
            rest = num_cycles - ((num_cycles - head) // diff) * diff - head - 1
            break

    for _ in range(rest):
        for _ in range(4):
            tilt_platform(platform)
            turn_platform(platform)

def start_calc(num_cycles):
    file_path = 'day_14/part2/input.txt' #'day_14/part2/test.txt'
    platform = read_input(file_path)

    simulate_spin_cycles(platform, num_cycles)
    total_load = calculate_total_load(platform)

    return total_load

num_cycles = 1000000000

result = start_calc(num_cycles)
print(result)
