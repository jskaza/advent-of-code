import re
import numpy as np
import math

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

parts = []
gears = []
for idx, line in enumerate(lines):
    for d in re.finditer("\d+", line):
        start = d.start()
        end = d.end()
        parts.append(np.array([idx, start, end-1, int(d.group(0))]))
    for g in re.finditer("\*", line):
        start = g.start()
        end = g.end()
        gears.append(np.array([idx, start, start]))

# parts = parts
gears = np.array(gears)

gear_partners = {}
for p in parts:
    # no gears on first or last
    line_req = gears[(gears[:,0] >= (p[0] - 1)) & (gears[:,0] <= (p[0] + 1))]
    start_end_req = line_req[(line_req[:,1] >= p[1] - 1) & (line_req[:,2] <= p[2] + 1)]
    for g in start_end_req:
        g_id = "-".join([str(x) for x in g.tolist()])
        if g_id in gear_partners:
            gear_partners[g_id].append(p[3])
        else:
            gear_partners[g_id] = [p[3]]
sum_gears = 0
for v in list(gear_partners.values()):
    if len(v) == 2:
        sum_gears += math.prod(v)

print(sum_gears)