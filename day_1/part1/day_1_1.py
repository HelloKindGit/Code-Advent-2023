def extract_calibration_values(line):
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in str(list(reversed(line))) if char.isdigit()), None)
    
    if first_digit is not None and last_digit is not None:
        calibration_value = int(first_digit + last_digit)
        return calibration_value
    else:
        return 0

def sum_of_calibration_values(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    total_sum = sum(extract_calibration_values(line) for line in lines)
    return total_sum

input_file_path = 'day_1/part1/input.txt' # 'day_1/part1/test.txt'
result = sum_of_calibration_values(input_file_path)

print(result)