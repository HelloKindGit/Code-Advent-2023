import numpy as np
from decimal import Decimal as D

def parse_data_from_file(file_path):
    hailstones = []
    with open(file_path, 'r') as file:
        for line in file:
            pos_vel = line.strip().split(" @ ")
            position = [D(val) for val in pos_vel[0].split(", ")]
            velocity = [D(val) for val in pos_vel[1].split(", ")]
            hailstones.append((position, velocity))
    return hailstones

def adjust_hailstone(hailstone, ax, ay, az):
    (px, py, pz), (vx, vy, vz) = hailstone
    return ((px, py, pz), (vx - ax, vy - ay, vz - az))

def intersectXY(h1, h2):
    (px1, py1, _), (vx1, vy1, _) = h1
    (px2, py2, _), (vx2, vy2, _) = h2
    slope1 = D('inf') if vx1 == 0 else vy1 / vx1
    slope2 = D('inf') if vx2 == 0 else vy2 / vx2

    if slope1 == slope2:
        return None

    if slope1 == float('inf'):
        intX = px1
        intY = slope2 * (intX - px2) + py2
    elif slope2 == float('inf'):
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

def get_collision_time(hailstone, intersection):
    (px, _, _), (vx, _, _) = hailstone
    return (intersection[0] - px) / vx

def get_adjustment_Z(h1, h2, inter):
    (px1, py1, pz1), (vx1, vy1, vz1) = h1
    (px2, py2, pz2), (vx2, vy2, vz2) = h2

    t1 = (inter[0] - px1) / vx1 if vx1 != 0 else (inter[1] - py1) / vy1
    t2 = (inter[0] - px2) / vx2 if vx2 != 0 else (inter[1] - py2) / vy2

    if t1 == t2:
        return None  # Collision at the same time

    return (pz1 - pz2 + t1 * vz1 - t2 * vz2) / (t1 - t2)

def p2(hailstones):
    N = 0
    while True:
        for X in range(N + 1):
            Y = N - X
            for negX in (-1, 1):
                for negY in (-1, 1):
                    aX = X * negX
                    aY = Y * negY
                    H1_adjusted = adjust_hailstone(hailstones[0], aX, aY, 0)
                    inter = None
                    for H2_data in hailstones[1:]:
                        H2_adjusted = adjust_hailstone(H2_data, aX, aY, 0)
                        p = intersectXY(H1_adjusted, H2_adjusted)
                        if p is None:
                            break
                        if inter is None:
                            inter = p
                            continue
                        if p != inter:
                            break

                    if p is None or p != inter:
                        continue

                    aZ = None
                    for H2_data in hailstones[1:]:
                        nZ = get_adjustment_Z(H1_adjusted, H2_data, inter)
                        if aZ is None:
                            aZ = nZ
                            continue
                        elif nZ != aZ:
                            break

                    if aZ == nZ:
                        Z = H1_adjusted[0][2] + get_collision_time(H1_adjusted, inter) * (H1_adjusted[1][2] - aZ)
                        return Z + inter[0] + inter[1]

        N += 1

file_path = 'day_24/part2/input.txt' #'day_24/part2/test.txt'
hailstones_data = parse_data_from_file(file_path)

result = p2(hailstones_data)
print(result)
