from scipy.spatial import distance
import numpy as np
from math import prod

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
points = []
for line in lines:
    points.append(tuple(int(x) for x in line.split(",")))
points = np.array(points)
    

distances = distance.pdist(points, metric="euclidean")
circuits = []
largest_circuit = 0
while largest_circuit < len(lines):
    closest = np.argmin(distances)
    distances[closest] = np.inf
    n = points.shape[0]
    m = int(np.floor((2*n - 1 - np.sqrt((2*n - 1)**2 - 8*closest)) / 2))
    j = int(closest - m*(2*n - m - 1)//2 + m + 1)
    
    if any([lines[m] in c and lines[j] in c for c in circuits]):
        pass
    elif any([lines[m] in c for c in circuits]) and any([lines[j] in c for c in circuits]):
        circuit_m = next(c for c in circuits if lines[m] in c)
        circuit_j = next(c for c in circuits if lines[j] in c)
        if circuit_m != circuit_j:
            circuit_m |= circuit_j
            circuits.remove(circuit_j)
    elif any([lines[j] in c for c in circuits]) and not any([lines[m] in c for c in circuits]):
        circuit_j = next(c for c in circuits if lines[j] in c)
        circuit_j.add(lines[m])
    elif any([lines[m] in c for c in circuits]) and not any([lines[j] in c for c in circuits]):
        circuit_m = next(c for c in circuits if lines[m] in c)
        circuit_m.add(lines[j])
    else:
        circuits.append({lines[m], lines[j]})
    largest_circuit = max(largest_circuit, len(circuits[-1]))
    

print(int(lines[m].split(",")[0]) * int(lines[j].split(",")[0]))

