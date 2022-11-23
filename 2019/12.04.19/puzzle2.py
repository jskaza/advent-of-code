def tokenize(pw: int) -> list:
    return [int(x) for x in list(str(pw))]


def never_decrease(pw: list) -> bool:
    for i in range(len(pw)-1):
        if pw[i] > pw[i+1]:
            return False
    else:
        return True


def double(pw: list) -> bool:
    for i in range(len(pw)-1):
        # check next
        next = pw[i] == pw[i+1]
        # check 2 ahead
        if i < len(pw)-2:
            two_ahead = pw[i] == pw[i+2]
        else:
            two_ahead = False
        # check previous
        if i > 0:
            prev = pw[i] == pw[i-1]
        else:
            prev = False
        if next and not two_ahead and not prev:
            return True
    else:
        return False


def check(pw: list) -> int:
    return sum([never_decrease(y) & double(y) for y in [tokenize(x) for x in pw]])


input = range(172851, 675869+1)
print(check(input))
