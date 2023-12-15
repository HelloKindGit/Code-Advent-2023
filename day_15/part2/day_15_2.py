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

def calculate_focusing_power(steps):
    boxes = [{} for _ in range(256)]

    for step in steps:
        if '=' in step:
            label, focal_length = step.split('=')
            focal_length = int(focal_length)
            box_id = hash_algorithm(label)
            boxes[box_id][label] = focal_length
        else:
            label = step[:-1]
            box_id = hash_algorithm(label)
            if label in boxes[box_id]:
                del boxes[box_id][label]

    total_power = 0
    for box_id, box in enumerate(boxes, 1):
        for slot_id, (label, focal_length) in enumerate(box.items(), 1):
            total_power += box_id * slot_id * focal_length

    return total_power

def run_hashmap_from_file(file_path):
    initialization_sequence = read_initialization_sequence(file_path)
    steps = initialization_sequence.split(',')
    return calculate_focusing_power(steps)

file_path = 'day_15/part1/input.txt' #'day_15/part1/test.txt'
result = run_hashmap_from_file(file_path)
print(result)
