import networkx as nx

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
print(len(list(nx.all_simple_paths(G, source="you", target="out"))))