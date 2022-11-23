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
        if pw[i] == pw[i+1]:
            return True
    else:
        return False


def check(pw: list) -> int:
    return sum([never_decrease(y) & double(y) for y in [tokenize(x) for x in pw]])


input = range(172851, 675869+1)
print(check(input))
