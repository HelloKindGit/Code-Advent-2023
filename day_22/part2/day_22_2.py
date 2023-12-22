from collections import defaultdict

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_input(input_data):
    bricks = []
    for line in input_data.strip().split('\n'):
        parts = line.split('~')
        start_coords = [int(n) for n in parts[0].split(',')]
        end_coords = [int(n) for n in parts[1].split(',')]
        brick = start_coords + end_coords
        bricks.append(brick)
    return bricks

def dropped_brick(tallest, brick):
    peak = max(tallest[(x, y)] for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1))
    dz = max(brick[2] - peak - 1, 0)
    return (brick[0], brick[1], brick[2] - dz, brick[3], brick[4], brick[5] - dz)

def drop(tower):
    tallest = defaultdict(int)
    new_tower = []
    falls = 0
    for brick in tower:
        new_brick = dropped_brick(tallest, brick)
        if new_brick[2] != brick[2]:
            falls += 1
        new_tower.append(new_brick)
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                tallest[(x, y)] = new_brick[5]
    return falls, new_tower

def calculate_total_falls_refined_corrected(bricks):
    p2 = 0
    sorted_bricks = sorted(bricks, key=lambda b: b[2])

    _, fallen = drop(sorted_bricks)

    # For each brick, calculate how many falls occur when it is removed
    for i in range(len(fallen)):
        removed = fallen[:i] + fallen[i+1:]
        falls, _ = drop(removed)
        if falls:
            p2 += falls

    return p2

file_path = 'day_22/part1/input.txt'  #'day_22/part1/test.txt'
input_data = read_input_from_file(file_path)
bricks = parse_input(input_data)
total_falls = calculate_total_falls_refined_corrected(bricks)
print(f"Total number of falls: {total_falls}")
