with open("input.txt", "r") as f:
    input = f.read().splitlines()

def eval(c, p):
    '''
    c: a condition to test
    p: a part dictionary
    '''
    if ":" not in c:
        return c
    else:
        test, action = c.split(":")
        val = p[test[0]]
        comparator = test[1]
        comparison = int(test[2:])
        if comparator == ">":
            if val > comparison:
                return action
            else:
                return None
        else:
            if val < comparison:
                return action
            else:
                return None

def test_part(p):
    conditions = flows["in"]
    while True:
        for c in conditions:
            res = eval(c, p)
            if res is None:
                continue
            elif res == "A":
                return sum(p.values())
            elif res == "R":
                return 0
            else:
                conditions = flows[res]
                break
    
parts = []
flows = {}
for line in input:
    if line == "":
        continue
    elif line.startswith("{"):
        parse = line[1:-1].split(",")
        temp = {}
        for p in parse:
            temp[p.split("=")[0]] = int(p.split("=")[1])
        parts.append(temp)
    else:
        flow_name = line.split("{")[0]
        conditions = line[:-1].split("{")[1].split(",")
        flows[flow_name] = conditions
 
print(sum([test_part(p) for p in parts]))

        

