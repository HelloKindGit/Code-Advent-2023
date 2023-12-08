def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    first_line = lines[0].strip()
    network = {}
    for line in lines[1:]:
        parts = line.split('=')
        if len(parts) == 2:
            node = parts[0].strip()
            next_nodes = parts[1].strip()
            network[node] = next_nodes.strip('()').split(', ')
    return first_line, network

instructions, network = read_input('day_8/part2/input.txt') #'day_8/part2/test.txt'

starting_nodes = [node for node in network.keys() if node.endswith('A')]

current_nodes = starting_nodes
instruction_index = 0
steps = 0

least_steps = [0] * len(current_nodes)

while 0 in least_steps:
    for i, node in enumerate(current_nodes):
        if node.endswith('Z') and least_steps[i] == 0:
            least_steps[i] = steps

    new_current_nodes = []
    for node in current_nodes:
        transition_key = instructions[instruction_index]
        new_node = network[node][0] if transition_key == 'L' else network[node][1]
        new_current_nodes.append(new_node)

    current_nodes = new_current_nodes
    instruction_index = (instruction_index + 1) % len(instructions)
    steps += 1

result = 1
for step in least_steps:
    a, b = result, step
    while b:
        a, b = b, a % b
    result *= step // a

print(result)
