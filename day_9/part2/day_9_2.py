def generate_sequences(history):
    differences = [b - a for a, b in zip(history, history[1:])]
    sequences = [history, differences]
    non_zero_check = sum(1 for i in differences if i)

    while non_zero_check:
        next_differences = [b - a for a, b in zip(differences, differences[1:])]
        sequences.append(next_differences)
        differences = next_differences
        non_zero_check = sum(1 for i in differences if i)

    return sequences

def extrapolate_values(sequences):
    value = 0
    for sequence in sequences[::-1]:
        value += sequence[-1]

    return value

def extrapolate_previous_value(history):
    sequences = generate_sequences(history)
    previous_value = 0
    for sequence in sequences[::-1]:
        previous_value = sequence[0] - previous_value
    return previous_value

def calculate_histories():
    file_path = "day_9/part2/input.txt"  # 'day_9/part2/test.txt'
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]

    sum_of_extrapolated_values = sum(extrapolate_previous_value(list(map(int, line.split()))) for line in data)

    return sum_of_extrapolated_values

result = calculate_histories()
print(result)