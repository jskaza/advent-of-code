from math import lcm

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
left_right = lines[0]
nodes = {}
for node in lines[2:]:
    n = node.split(" = (")
    nodes[n[0]] = {"L": n[1].split(",")[0], "R": n[1].split(", ")[1][:-1]}

def first_z_steps(node):
    current_node = node
    steps = 0
    while True:
        for i in range(len(left_right)):
            direction = left_right[i]
            current_node = nodes[current_node][direction]
            steps += 1
            if current_node[-1] == "Z":
                return current_node, steps

# we can verify the assumption that visits to Z happen in cycles, which drastically simplifies the problem
a_to_z = [first_z_steps(node) for  node in nodes if node[-1] == "A"]
z_to_z = [first_z_steps(node[0]) for node in a_to_z]
assert a_to_z == z_to_z

print(lcm(*(node[1] for node in a_to_z)))