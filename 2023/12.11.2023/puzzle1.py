import numpy as np
from itertools import combinations

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [list(line) for line in lines]
lines = np.array(lines)
padding = 0
for row in range(lines.shape[0]):
    if np.all(lines[row+padding,:] == "."):
        lines = np.insert(lines, row+padding, ".", axis=0)
        padding+=1

padding = 0
for col in range(lines.shape[1]):
    if np.all(lines[:,col+padding] == "."):
        lines = np.insert(lines, col+padding, ".", axis=1)
        padding+=1

galaxies = np.transpose((lines=="#").nonzero()).tolist()
print(sum([np.abs(c1[0]-c2[0]) + np.abs(c1[1]-c2[1]) for c1, c2 in list(combinations(galaxies, 2))]))


# # network approach
# import networkx as nx
# galaxies = []
# G = nx.Graph()
# for row in range(lines.shape[0]):
#     for col in range(lines.shape[1]):
#         if row != 0:
#             G.add_edge(f"{row}.{col}",f"{row-1}.{col}")
#         if row != lines.shape[0]-1:
#             G.add_edge(f"{row}.{col}",f"{row+1}.{col}")
#         if col != 0:
#             G.add_edge(f"{row}.{col}",f"{row}.{col-1}")
#         if row != lines.shape[1]-1:
#             G.add_edge(f"{row}.{col}",f"{row}.{col+1}")
#         if lines[row,col] == "#":
#             galaxies.append(f"{row}.{col}")

# print(sum([nx.shortest_path_length(G, s, t) for s, t in list(combinations(galaxies,2))]))
