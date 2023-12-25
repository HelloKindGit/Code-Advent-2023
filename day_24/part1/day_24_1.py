import numpy as np
from decimal import Decimal as D

def parse_hailstone_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    hailstones = []
    for line in data:
        pos_vel = line.strip().split(" @ ")
        position = [D(val) for val in pos_vel[0].split(", ")]
        velocity = [D(val) for val in pos_vel[1].split(", ")]
        hailstones.append((position, velocity))
    return hailstones

def calculate_slope(velocity):
    vx, vy = velocity
    return D('inf') if vx == 0 else vy / vx

def intersectXY(h1, h2):
    (px1, py1, _), (vx1, vy1, _) = h1
    (px2, py2, _), (vx2, vy2, _) = h2
    slope1 = calculate_slope((vx1, vy1))
    slope2 = calculate_slope((vx2, vy2))

    if slope1 == slope2:
        return None

    if slope1 == float('inf'):  # h1 is vertical
        intX = px1
        intY = slope2 * (intX - px2) + py2
    elif slope2 == float('inf'):  # h2 is vertical
        intX = px2
        intY = slope1 * (intX - px1) + py1
    else:
        intX = (py1 - py2 - px1 * slope1 + px2 * slope2) / (slope2 - slope1)
        intY = py1 + slope1 * (intX - px1)

    intX, intY = intX.quantize(D(".1")), intY.quantize(D(".1"))

    future1 = np.sign(intX - px1) == np.sign(vx1)
    future2 = np.sign(intX - px2) == np.sign(vx2)
    if not (future1 and future2):
        return None

    return (intX, intY)

def count_intersections(hailstones, pMin, pMax):
    count = 0
    for idx, h1 in enumerate(hailstones):
        for h2 in hailstones[idx + 1:]:
            intersection = intersectXY(h1, h2)
            if intersection is not None and pMin <= intersection[0] <= pMax and pMin <= intersection[1] <= pMax:
                count += 1
    return count

file_path = 'day_24/part1/input.txt' #'day_24/part1/test.txt'
hailstones_data = parse_hailstone_data(file_path)

pMin_actual, pMax_actual = D('200000000000000'), D('400000000000000')
result = count_intersections(hailstones_data, pMin_actual, pMax_actual)
print(result)
