def read_input(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()
    return data

def parse_input(data):
    seeds = [int(i) for i in data[0].strip().split(": ")[1].split(" ")]
    mappings = []
    for line in data[2:]:
        line = line.strip()
        if line.endswith(":"):
            mappings.append([])
        elif len(line) > 0:
            mappings[-1].append([int(i) for i in line.split(" ")])
    return seeds, mappings

def calculate_result(seeds, mappings):
    min_result = 2**64

    for seed_start, seed_offset in zip(seeds[::2], seeds[1::2]):
        seed_ranges = [(seed_start, seed_start + seed_offset - 1)]

        for type_mappings in mappings:
            seed_ranges = update_ranges(seed_ranges, type_mappings)

        min_result = min(min_result, min(seed_ranges)[0])

    return min_result

def update_ranges(ranges, type_mappings):
    new_ranges = []

    for range_start, range_end in ranges:
        found = False

        for map_offset, map_start, map_size in type_mappings:
            map_end = map_start + map_size - 1

            if range_start >= map_start and range_end < map_end:
                new_ranges.append((range_start - map_start + map_offset, range_end - map_start + map_offset))
                found = True
            elif range_start < map_start and range_end >= map_start and range_end < map_end:
                ranges.append((range_start, map_start - 1))
                new_ranges.append((map_offset, map_offset + range_end - map_start))
                found = True
            elif range_start < map_start + map_size and range_end >= map_start + map_size and range_start >= map_start:
                ranges.append((map_start + map_size, range_end))
                new_ranges.append((map_offset + range_start - map_start, map_offset + map_size - 1))
                found = True
            elif range_start < map_start and range_end >= map_start + map_size:
                ranges.append((range_start, map_start - 1))
                new_ranges.append((map_offset, map_offset + map_size - 1))
                ranges.append((map_start + map_size, range_end))
                found = True

            if found:
                break

        if not found:
            new_ranges.append((range_start, range_end))

    return new_ranges

def run_calculations():
    file_path = "day_5/part1/input.txt" # "day_5/part1/test.txt"
    data = read_input(file_path)
    seeds, mappings = parse_input(data)
    result = calculate_result(seeds, mappings)
    return result

results = run_calculations()
print(results)
