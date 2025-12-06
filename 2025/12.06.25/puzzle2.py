from math import prod
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
current_nums = []
total = 0
current_op = None
for pos in range(len(lines[0])):
    current_num = "".join([line[pos] for line in lines[:-1]])
    if current_num.strip() == "":
        if current_op == "+":
            total += sum([int(num) for num in current_nums])
        elif current_op == "*":
            total += prod([int(num) for num in current_nums])
        current_nums = []
        current_op = None
    else:
        current_nums.append(current_num)
        if lines[-1][pos] == "+":
            current_op = "+"
        elif lines[-1][pos] == "*":
            current_op = "*"

# one final operation
if current_op == "+":
    total += sum([int(num) for num in current_nums])
elif current_op == "*":
    total += prod([int(num) for num in current_nums])
    
print(total)
        
        