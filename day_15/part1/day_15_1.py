def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

file_path = 'day_15/part1/input.txt' #'day_15/part1/test.txt'
initialization_sequence = read_from_file(file_path)

steps = initialization_sequence.split(',')
hash_sums = sum(hash_algorithm(step) for step in steps)
print(hash_sums)
