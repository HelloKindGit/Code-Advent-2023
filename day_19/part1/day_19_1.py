def evaluate_condition(condition, part_ratings):
    if condition is None:
        return True  # No condition means always true

    category, comparison, value = condition[0], condition[1], int(condition[2:])

    if comparison == '<':
        return part_ratings[category] < value
    elif comparison == '>':
        return part_ratings[category] > value

def process_part(part, workflows):
    current_workflow = 'in'

    while True:
        for condition, destination in workflows[current_workflow]:
            if evaluate_condition(condition, part):
                if destination == 'A':
                    return 'Accepted', part
                elif destination == 'R':
                    return 'Rejected', None
                else:
                    current_workflow = destination
                    break

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    workflow_lines, part_lines = [], []
    parsing_workflows = True

    for line in lines:
        line = line.strip()
        if line == "":
            parsing_workflows = False
            continue

        if parsing_workflows:
            workflow_lines.append(line)
        else:
            part_lines.append(line)

    workflows = {}
    for w in workflow_lines:
        name, rules_str = w.split('{')
        rules_str = rules_str[:-1] #Remove closing brace
        rules = rules_str.split(',')

        workflow_rules = []
        for rule in rules:
            if ':' in rule:
                condition, destination = rule.split(':')
                workflow_rules.append((condition, destination))
            else:
                workflow_rules.append((None, rule))

        workflows[name] = workflow_rules

    parts = []
    for p in part_lines:
        p = p[1:-1] #Remove braces
        ratings = p.split(',')

        part_ratings = {}
        for rating in ratings:
            category, value = rating.split('=')
            part_ratings[category] = int(value)

        parts.append(part_ratings)

    return workflows, parts

def calculate_accepted_parts_sum(file_path):
    workflows, parts = parse_input(file_path)

    total_sum = 0
    for part in parts:
        status, accepted_part = process_part(part, workflows)
        if status == 'Accepted':
            total_sum += sum(accepted_part.values())

    return total_sum

file_path = 'day_19/part1/input.txt' #'day_19/part1/test.txt'
print(calculate_accepted_parts_sum(file_path))
