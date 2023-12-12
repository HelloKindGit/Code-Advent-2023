from functools import cache

def calculate_sum_counts_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    unfolded_data = unfold_records(data)
    return calculate_sum_counts(unfolded_data)

def unfold_records(data):
    unfolded_data = []
    
    for line in data:
        springs, groups = line.split()
        groups = tuple([*map(int, groups.split(","))])
        
        unfolded_springs = "?".join([springs]*5)
        unfolded_groups = ",".join([str(g) for g in groups]*5)
        
        unfolded_line = f"{unfolded_springs} {unfolded_groups}\n"
        unfolded_data.append(unfolded_line)

    return unfolded_data

def calculate_sum_counts(data):
    _sum = 0

    for line in data:
        springs, groups = line.split()
        groups = tuple([*map(int, groups.split(","))])
        _sum += get_possible_count(springs, groups)

    return _sum

@cache
def get_possible_count(springs: str, groups: tuple, prev_size=0, must_operational=False) -> int:
    if springs == "":
        if groups:
            if len(groups) == 1 and groups[0] == prev_size:
                return 1
            return 0
        else:
            if prev_size == 0:
                return 1
            else:
                return 0

    if len(groups) == 0:
        if "#" in springs or prev_size > 0:
            return 0
        return 1

    curr = springs[0]
    rest = springs[1:]

    if curr == "?":
        return get_possible_count("#" + rest, groups, prev_size, must_operational) + get_possible_count("." + rest, groups, prev_size, must_operational)

    if curr == "#":
        if must_operational:
            return 0

        curr_size = prev_size + 1

        if curr_size > groups[0]:
            return 0
        elif curr_size == groups[0]:
            return get_possible_count(rest, groups[1:], 0, True)
        else:
            return get_possible_count(rest, groups, curr_size, False)

    if curr == ".":
        if must_operational:
            return get_possible_count(rest, groups, 0, False)

        if prev_size == 0:
            return get_possible_count(rest, groups, 0, False)
        else:
            if prev_size != groups[0]:
                return 0
            else:
                return get_possible_count(rest, groups[1:], 0, False)

file_path = 'day_12/part2/input.txt'  #'day_12/part2/test.txt'
result = calculate_sum_counts_from_file(file_path)
print(result)
