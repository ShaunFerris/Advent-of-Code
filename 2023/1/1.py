with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]


def decode(calValue):
    out = ""
    for char in calValue:
        if 48 <= ord(char) <= 58:
            out += char
            break
    for char in calValue[::-1]:
        if 48 <= ord(char) <= 58:
            out += char
            break
    return out


def sumDecode(calList):
    out = 0
    for i in calList:
        out += int(decode(i))
    return out


print(sumDecode(lines))
