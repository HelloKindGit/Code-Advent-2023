def read_patterns_from_file(file_path):
    with open(file_path, 'r') as file:
        patterns = file.read().strip().split('\n\n')
    return patterns

def find_mirror(pattern, diff=0):
    def is_mirror(a, b):
        return sum(x != y for x, y in zip(a, b)) == diff

    def reverse_and_join(slice):
        return "".join(slice[::-1])

    pattern_h = pattern.split("\n")
    pattern_v = ["".join(c) for c in zip(*pattern_h)]

    for current_pattern, weight in ((pattern_h, 100), (pattern_v, 1)):
        for i in range(1, len(current_pattern)):
            slice_a, slice_b = current_pattern[:i], current_pattern[i:]
            a, b = reverse_and_join(slice_a), "".join(slice_b)
            if is_mirror(a, b):
                return i * weight

    return -1

def calculate_total_line_of_reflection():
    file_path = 'day_13/part2/input.txt' # 'day_13/part2/test.txt'
    patterns = read_patterns_from_file(file_path)
    return sum(find_mirror(pattern, diff=1) for pattern in patterns)

results = calculate_total_line_of_reflection()
print(results)