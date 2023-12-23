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

def solve(bricks):
    bricks_sorted = sorted(bricks, key=lambda brick: brick[2])
    _, fallen = drop(bricks_sorted)
    save_bricks = 0
    for i in range(len(fallen)):
        removed = fallen[:i] + fallen[i + 1:]
        falls, _ = drop(removed)
        if not falls:
            save_bricks += 1
    return save_bricks

file_path = 'day_22/part1/input.txt'  #'day_22/part1/test.txt'
input_data = read_input_from_file(file_path)

bricks = parse_input(input_data)
results = solve(bricks)
print(results)
