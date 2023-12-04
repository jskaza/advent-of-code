with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    
def calc_points(line):
    line = line.split(": ")[1]
    nums = line.split(" | ")
    winning_nums = [int(num) for num in nums[0].split()]
    my_nums = [int(num) for num in nums[1].split()]
    ct = 0
    for num in winning_nums:
        if num in my_nums:
            ct+=1
    return 2**(ct-1) if ct > 0 else 0

pts = 0
for line in lines:
    pts += calc_points(line)
    
print(pts)
    