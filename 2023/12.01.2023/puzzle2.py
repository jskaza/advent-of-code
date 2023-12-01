import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    
def extract_value(line: str) -> int:
    word_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }
    for k, v in word_digit.copy().items():
        word_digit[k[::-1]] = v
    expr1 = "|".join([word for word in list(word_digit.keys())] + ["\d"])
    expr2 = "|".join([word[::-1] for word in list(word_digit.keys())] + ["\d"])
    digit1 = re.findall(expr1, line)[0]
    digit2 = re.findall(expr2, line[::-1])[0]
    value = ""
    for d in (digit1, digit2):
        if d in word_digit:
            value += word_digit[d]
        else:
            value += d
    return int(value)

print(sum([extract_value(line.strip()) for line in lines]))