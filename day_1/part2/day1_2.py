def extract_calibration_values(line):
    spelled_out_digits = ["one", "two", "three",
                          "four", "five", "six",
                          "seven", "eight", "nine"]

    # Replace spelled-out digits with their corresponding numeric values
    converted_line = "".join([
        char if not char.isalpha() else "".join([
            str(idx) for idx, val in enumerate(spelled_out_digits, 1)
                if line[i:].startswith(val)
        ]) for i, char in enumerate(line)
    ])

    first_digit = next((char for char in converted_line if char.isdigit()), None)
    last_digit = next((char for char in reversed(converted_line) if char.isdigit()), None)

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

input_file_path = 'day_1/part2/input.txt'  # 'day_1/part2/test.txt'
result = sum_of_calibration_values(input_file_path)

print(result)
