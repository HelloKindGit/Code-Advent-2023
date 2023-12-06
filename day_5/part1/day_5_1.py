def read_input(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

def parse_input(input_lines):
    seed_values = [int(i) for i in input_lines[0].strip().split(": ")[1].split(" ")]
    mappings = []
    for line in input_lines[2:]:
        line = line.strip()
        if line.endswith(":"):
            mappings.append([])
        elif len(line) > 0:
            mappings[-1].append([int(i) for i in line.split(" ")])
    return seed_values, mappings

def sort_mappings(mappings):
    [m.sort(key=lambda x: x[1]) for m in mappings]
    return mappings

def calculate_result(seed_values, mappings):
    min_result = 2**32
    for x in seed_values:
        for type_mappings in mappings:
            for mapping in type_mappings:
                if x >= mapping[1] and x < mapping[1] + mapping[2]:
                    x = x - mapping[1] + mapping[0]
                    break
        min_result = min(x, min_result)
    return min_result

def run_calculations():
    filename = "day_5/part1/input.txt" # "day_5/part1/test.txt"
    data = read_input(filename)
    seeds, mappings = parse_input(data)
    sorted_mappings = sort_mappings(mappings)
    result = calculate_result(seeds, sorted_mappings)
    return result

results = run_calculations()
print(results)
