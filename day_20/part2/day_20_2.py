import collections
import math

def parse_module_configurations(input_text):
    module_connections = {}

    for line in input_text.splitlines():
        source_module, target_modules = line.split(' -> ')
        target_modules = target_modules.split(', ')

        if source_module == 'broadcaster':
            module_type = None
        else:
            module_type = source_module[0]
            source_module = source_module[1:]

        module_connections[source_module] = (module_type, target_modules)

    return module_connections

def count_low_pulse_cycles_to_rx(module_config):
    module_states = {}
    module_inputs = collections.defaultdict(list)

    for module, (_, destinations) in module_config.items():
        for destination in destinations:
            module_inputs[destination].append(module)

    for module, (module_type, _) in module_config.items():
        if module_type is None:
            continue
        elif module_type == '%':
            module_states[module] = False
        elif module_type == '&':
            module_states[module] = {input_module: False for input_module in module_inputs[module]}

    target = 'rx'
    main_conjunction_module = module_inputs[target][0]
    sub_conjunction_modules = module_inputs[main_conjunction_module]

    cycle_counts_for_low_pulse = {}
    cycle_number = 0

    while len(cycle_counts_for_low_pulse) < len(sub_conjunction_modules):
        cycle_number += 1
        processing_queue = [(None, 'broadcaster', False)]

        while processing_queue:
            next_queue = []

            for source, current_module, high_pulse in processing_queue:
                if current_module in sub_conjunction_modules and not high_pulse:
                    if current_module not in cycle_counts_for_low_pulse:
                        cycle_counts_for_low_pulse[current_module] = cycle_number

                module_details = module_config.get(current_module)
                if module_details is None:
                    continue

                module_type, destinations = module_details
                if module_type == '%':
                    if not high_pulse:
                        module_states[current_module] = not module_states[current_module]
                        for destination in destinations:
                            next_queue.append((current_module, destination, module_states[current_module]))
                elif module_type == '&':
                    module_states[current_module][source] = high_pulse
                    next_pulse = not all(module_states[current_module].values())
                    for destination in destinations:
                        next_queue.append((current_module, destination, next_pulse))
                elif module_type is None:
                    for destination in destinations:
                        next_queue.append((current_module, destination, high_pulse))

            processing_queue = next_queue

    return math.lcm(*cycle_counts_for_low_pulse.values())

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

input_file_path = 'day_20/part2/input.txt'
data = read_input_from_file(input_file_path)

parsed_configs = parse_module_configurations(data)
result = count_low_pulse_cycles_to_rx(parsed_configs)
print(result)
