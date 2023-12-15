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

def sum_of_results(initialization_sequence):
    steps = initialization_sequence.split(',')
    total_sum = 0
    for step in steps:
        total_sum += hash_algorithm(step)
    return total_sum

file_path = 'day_15/part1/input.txt' #'day_15/part1/test.txt'
initialization_sequence = read_initialization_sequence(file_path)

result = sum_of_results(initialization_sequence)
print(result)