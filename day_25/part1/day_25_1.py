import networkx as nx
import random

def parse_input_to_graph(input_str):
    graph = nx.Graph()
    for line in input_str.strip().split('\n'):
        node, edges = line.split(': ')
        for edge in edges.split(' '):
            graph.add_edge(node, edge, capacity=1.0)
    return graph

def find_minimum_cut_solution(graph):
    cut_value = 100  # Arbitrary large value
    while cut_value > 3:
        k1, k2 = random.sample(list(graph.nodes()), 2)

        cut_value, partition = nx.minimum_cut(graph, k1, k2)
    
    return len(partition[0]) * len(partition[1])

def solve_puzzle_from_file(file_path):
    with open(file_path, 'r') as file:
        input_str = file.read().strip()

    graph = parse_input_to_graph(input_str)

    result = find_minimum_cut_solution(graph)
    return result

file_path = "day_25/part1/input.txt" #"day_25/part1/test.txt"
result = solve_puzzle_from_file(file_path)
print(result)