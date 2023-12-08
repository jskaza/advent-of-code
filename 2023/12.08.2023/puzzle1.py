with open("input.txt", "r") as f:
    lines = f.read().splitlines()

left_right = lines[0]
nodes = {}
for node in lines[2:]:
    n = node.split(" = (")
    nodes[n[0]] = {"L": n[1].split(",")[0], "R": n[1].split(", ")[1][:-1]}

def calc_steps(left_right: str, nodes: dict) -> int:
    current_node = "AAA"
    steps = 0
    while True:
        for i in range(len(left_right)):
            direction = left_right[i]
            current_node = nodes[current_node][direction]
            steps += 1
            if current_node == "ZZZ":
                return steps
            
print(calc_steps(left_right, nodes))