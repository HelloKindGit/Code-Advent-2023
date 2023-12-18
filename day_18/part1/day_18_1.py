def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def parse_actual_instructions(input_lines):
    instructions = []
    for line in input_lines:
        parts = line.split()
        direction = parts[0]
        distance = int(parts[1])
        instructions.append((direction, distance))
    return instructions

def simulate_digging(instructions):
    dug_cells = set()
    x, y = 0, 0
    
    for direction, distance in instructions:
        for _ in range(distance):
            dug_cells.add((x, y))
            
            if direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
                
        dug_cells.add((x, y))
    return dug_cells

def flood_fill(dug_cells, start_x, start_y, min_x, max_x, min_y, max_y):
    to_fill = [(start_x, start_y)]
    filled = set()
    
    while to_fill:
        x, y = to_fill.pop()
        if (x, y) in filled or (x, y) in dug_cells or x < min_x or x > max_x or y < min_y or y > max_y:
            continue
        
        filled.add((x, y))
        to_fill.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    
    return filled

def calculate_lagoon_volume(input_lines):
    instructions = parse_actual_instructions(input_lines)
    dug_cells = simulate_digging(instructions)
    
    min_x = min(x for x, _ in dug_cells) - 1
    max_x = max(x for x, _ in dug_cells) + 1
    min_y = min(y for _, y in dug_cells) - 1
    max_y = max(y for _, y in dug_cells) + 1
    
    exterior_cells = flood_fill(dug_cells, min_x, min_y, min_x, max_x, min_y, max_y)
    interior_cells = {(x, y) for x in range(min_x + 1, max_x) for y in range(min_y + 1, max_y) 
                      if (x, y) not in dug_cells and (x, y) not in exterior_cells}

    total_dug_cells = dug_cells.union(interior_cells)
    return len(total_dug_cells)

file_path = 'day_18/part1/test.txt' #'day_18/part1/test.txt'
input_lines = read_input_from_file(file_path)

results = calculate_lagoon_volume(input_lines)
print(results)