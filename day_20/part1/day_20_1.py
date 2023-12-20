import collections
import math

def parse_config(inp):
    mods = {}
    cables = {}

    for line in inp.splitlines():
        mod, outs = line.split(' -> ')
        if mod.startswith(('%', '&')):
            op, mod = mod[0], mod[1:]
            mods[mod] = op
        cables[mod] = outs.split(', ')
    return mods, cables

def initialize_memory(mods, cables):
    mem = {}
    for mod, op in mods.items():
        if op == '%':
            mem[mod] = False
        elif op == '&':
            mem[mod] = {src: False for src in cables if mod in cables[src]}
    return mem

def process_button_press(mods, cables, mem, count, start):
    count[0] += 1  # Initial low pulse
    queue = collections.deque()
    for out in cables[start]:
        queue.append((start, out, False))

    while queue:
        src, dst, pulse = queue.popleft()
        count[pulse] += 1

        if dst in mods:
            if mods[dst] == '%':
                if not pulse:
                    mem[dst] = not mem[dst]
                    for out in cables[dst]:
                        queue.append((dst, out, mem[dst]))
            elif mods[dst] == '&':
                mem[dst][src] = pulse
                new_pulse = not all(mem[dst].values())
                for out in cables[dst]:
                    queue.append((dst, out, new_pulse))

def simulate_machine_with_start(machine_input):
    mods, cables = parse_config(machine_input)
    mem = initialize_memory(mods, cables)

    start = 'broadcaster'
    count = [0, 0]
    for _ in range(1000):
        process_button_press(mods, cables, mem, count, start)
    
    return math.prod(count)

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_path = 'day_20/part1/input.txt' #'day_20/part1/test.txt'
data = read_from_file(file_path)
result = simulate_machine_with_start(data)
print(result)