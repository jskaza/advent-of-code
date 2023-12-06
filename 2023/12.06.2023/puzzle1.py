import math

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

times = [int(x) for x in lines[0].split()[1:]]
records = [int(x) for x in lines[1].split()[1:]]

def num_ways(time, rec):
    for i in range(time):
        if i*(time-i) > rec:
            return time-2*i+1
        
print(math.prod([num_ways(time, rec) for time, rec in zip(times, records)]))