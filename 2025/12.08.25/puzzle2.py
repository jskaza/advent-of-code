import networkx as nx
from functools import lru_cache

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
G = nx.DiGraph()
active_positions = [lines[0].index("S")]
G.add_node((0, active_positions[0]))
for line_num, line in enumerate(lines[1:]):
    for ap in active_positions:
        G.add_node((line_num, ap))
        G.add_edge((line_num-1, ap), (line_num, ap))
    splitters = [i for i, letter in enumerate(line) if letter == "^"]
    for i in splitters:
        if i in active_positions:
            active_positions.remove(i)
            if i-1 not in active_positions:
                active_positions.append(i-1) 
            if i+1 not in active_positions:
                active_positions.append(i+1)
            G.add_node((line_num, i-1))
            G.add_node((line_num, i+1))
            G.add_edge((line_num, i), (line_num, i-1))
            G.add_edge((line_num, i), (line_num, i+1))
    if line_num == len(lines)-2:
        G.add_node("END")
        for ap in active_positions:
            G.add_edge((line_num, ap), "END")

@lru_cache(maxsize=None)
def count_paths(node):
    if node == "END":
        return 1
    return sum(count_paths(neighbor) for neighbor in G.successors(node))

print(count_paths((0, lines[0].index("S"))))