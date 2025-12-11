import networkx as nx
from functools import lru_cache

G = nx.DiGraph()
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
for line in lines:
    a, b = line.split(":")
    if a not in G:
        G.add_node(a)
    b = b.strip().split()
    for b_ in b:
        if b_ not in G:
            G.add_node(b_)
        G.add_edge(a, b_)

# Use bitmask: bit 0 = visited dac, bit 1 = visited fft
@lru_cache(maxsize=None)
def count_paths(node, visited_mask):
    if node == "out":
        # Check if we've visited both dac (bit 0) and fft (bit 1)
        return 1 if visited_mask == 3 else 0
    
    total = 0
    for neighbor in G.successors(node):
        new_mask = visited_mask
        if neighbor == "dac":
            new_mask |= 1
        elif neighbor == "fft":
            new_mask |= 2
        total += count_paths(neighbor, new_mask)
    
    return total

result = count_paths("svr", 0)
print(result)