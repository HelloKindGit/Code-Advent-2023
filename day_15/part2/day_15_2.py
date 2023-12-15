def read_initialization_sequence(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace('\n', '')

def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def perform_hashmap_step(boxes, step):
    if '=' in step:
        label, value = step.split('=')
        box_id = hash_algorithm(label)
        boxes[box_id][label] = int(value)
    else:
        label = step[:-1]
        box_id = hash_algorithm(label)
        if label in boxes[box_id]:
            del boxes[box_id][label]

def calculate_focusing_power(boxes):
    total_power = 0
    for box_id1, box in enumerate(boxes, 1):
        for slot_id, lens in enumerate(box.items(), 1):
            total_power += box_id1 * slot_id * lens[1]
    return total_power

def run_hashmap_from_file(file_path):
    initialization_sequence = read_initialization_sequence(file_path)
    boxes = [{} for _ in range(256)]
    steps = initialization_sequence.split(',')
    
    for step in steps:
        perform_hashmap_step(boxes, step)

    return calculate_focusing_power(boxes)

file_path = 'day_15/part2/input.txt' #'day_15/part2/test.txt'
result = run_hashmap_from_file(file_path)
print(result)
