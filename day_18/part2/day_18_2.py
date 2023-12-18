def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def parse_hex_instructions(input_lines):
    hex_to_dir = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    instructions = []

    for line in input_lines:
        _, _, color_code = line.split()
        direction = hex_to_dir[int(color_code[-2], 16)]
        distance = int(color_code[2:-2], 16)
        instructions.append((direction, distance))

    return instructions

def calculate_boundary_points(instructions):
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    curr = (0, 0)
    points = [curr]
    edges = 0

    for direction, distance in instructions:
        edges += distance
        end = tuple(a + distance * b for a, b in zip(curr, dirs[direction]))
        points.append(end)
        curr = end

    return points, edges

def calc_area(points):
    area = 0
    for i in range(len(points) - 1):
        y1, x1 = points[i]
        y2, x2 = points[i + 1]
        area += x1 * y2 - x2 * y1
    return abs(area) // 2

def calculate_lagoon_volume_hex(file_path):
    input_lines = read_input_from_file(file_path)
    instructions = parse_hex_instructions(input_lines)
    points, edges = calculate_boundary_points(instructions)
    area = calc_area(points)
    return area + edges // 2 + 1

file_path = 'day_18/part2/input.txt' #'day_18/part2/test.txt'
volume = calculate_lagoon_volume_hex(file_path)
print(volume)
