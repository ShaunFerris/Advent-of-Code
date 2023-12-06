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


print(f"Part One: {sumDecode(lines)}")


def decodeWithWords(calValue):
    replaceMap = {
        "zero": "z0o",
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for key, value in replaceMap.items():
        calValue = calValue.replace(key, value)
    return decode(calValue)


def sumDecodeWithWords(calList):
    out = 0
    for i in calList:
        out += int(decodeWithWords(i))
    return out


print(f"Part Two: {sumDecodeWithWords(lines)}")
