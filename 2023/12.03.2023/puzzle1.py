import re
import numpy as np

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

chars = "[^a-zA-Z\d\.]"

sum_parts = 0
for idx, line in enumerate(lines):
    if idx == 0:
        prev_line = "." * (len(line) + 2)
    else:
        prev_line = "." + lines[idx-1] + "."
    if idx == (len(lines) - 1):
        next_line = "." * (len(line) + 2)
    else:
        next_line = "." + lines[idx+1] + "."
    padded_line = "." + line + "."

    neighb_chars = []
    current_chars = []
    
    for c in re.finditer(chars, prev_line):
        neighb_chars.append(c.start())
    for c in re.finditer(chars, next_line):
        neighb_chars.append(c.start())
    for c in re.finditer(chars, padded_line):
        current_chars.append(c.start())
    
    neighb_chars = np.array(neighb_chars)
    current_chars = np.array(current_chars)
    for d in re.finditer("\d+", padded_line):
        start = d.start()
        end = d.end()
        qualifying_neighbs = np.any((neighb_chars >= start-1) & (neighb_chars <= end))
        qualifying_same_line = np.any((current_chars == start-1) | (current_chars == end))
        if qualifying_neighbs | qualifying_same_line:
            sum_parts += int(d.group(0))

print(sum_parts)      
      