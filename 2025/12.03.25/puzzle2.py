def find_largest_subsequence(line, k):
    if len(line) < k:
        return None
    
    result = []
    n = len(line)
    
    for i, digit in enumerate(line):
        while (result and 
               len(result) + (n - i - 1) >= k and 
               result[-1] < digit):
            result.pop()
        
        result.append(digit)
    
    return ''.join(result[:k])


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

score = 0
for line in lines:
    largest_12_digit = find_largest_subsequence(line, 12)
    if largest_12_digit:
        score += int(largest_12_digit)

print(score)

