
def calculate_distance(data):
    loop_nodes = parse_map(data)
    return len(loop_nodes) // 2

def parse_map(data):
    start = None
    _map = []

    for h, line in enumerate(data):
        _map.append(list(line))
        if "S" in line:
            start = (h, line.index("S"))

    adj_dirs = [  # top, right, bottom, left
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    symbol_connects = {  # top, right, bottom, left
        "|": (1, 0, 1, 0),
        "-": (0, 1, 0, 1),
        "L": (1, 1, 0, 0),
        "J": (1, 0, 0, 1),
        "7": (0, 0, 1, 1),
        "F": (0, 1, 1, 0),
    }
    
    adj_connect_types = {
        (-1, 0): "F|7",
        (0, 1): "7-J",
        (1, 0): "L|J",
        (0, -1): "F-L",
    }

    adjs = [0, 0, 0, 0]  # top, right, bottom, left
    for i, adj in enumerate(adj_dirs):
        pos = tuple(a + b for a, b in zip(start, adj))
        if _map[pos[0]][pos[1]] in adj_connect_types[adj]:
            adjs[i] = 1

    _map[start[0]][start[1]] = {v: k for k, v in symbol_connects.items()}[tuple(adjs)]

    queue = [start]
    visited = set()

    while queue:
        pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if _map[pos[0]][pos[1]] in ".":
            continue

        sym = _map[pos[0]][pos[1]]
        _dirs = [adj_dirs[i] for i, v in enumerate(symbol_connects[sym]) if v == 1]
        for dy, dx in _dirs:
            queue.append((pos[0] + dy, pos[1] + dx))

    return visited

def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()

file_path = "day_10/part1/input.txt"  # "day_10/part1/test.txt"
input_data = read_input(file_path)
result = calculate_distance(input_data)
print(result)
