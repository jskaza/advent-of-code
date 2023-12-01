import re

with open("input.txt", "r") as f:
    lines = f.readlines()

def extract_value(line: str) -> int:
    digits = re.findall("\d", line)
    return int(digits[0]+digits[-1])

print(sum([extract_value(line) for line in lines]))