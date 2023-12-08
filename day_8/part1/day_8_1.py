def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    first_line = lines[0]

    network = {}
    for line in lines[1:]:
        parts = line.split('=')
        if len(parts) == 2:
            variable_name = parts[0].strip()
            variable_value = parts[1].strip()
            network[variable_name] = variable_value.strip('()').split(', ')
    return first_line, network


instructions, network = read_input('day_8/part1/input.txt') #'day_8/part1/test.txt'
steps = 0
targetNode = 'AAA'

while targetNode != 'ZZZ':
    for instruction in instructions:
        
        if targetNode == 'ZZZ':
            print('FINAL STEPS: ', steps)
            break

        left, right = network[targetNode]
        
        if instruction == 'L':
            targetNode = left
            steps += 1
        elif instruction == 'R':
            targetNode = right
            steps += 1