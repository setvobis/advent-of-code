with open('input.txt') as file:
    t = file.read().strip()

lines = [line for line in t.split('\n')]
groups = [line for line in t.split('\n\n')]


def compare(x1, x2):
    if isinstance(x1, int) and isinstance(x2, int):
        if x1 < x2:
            return 1
        elif x1 == x2:
            return 0
        else:
            return -1
    elif isinstance(x1, list) and isinstance(x2, list):
        i = 0
        while i < len(x1) and i < len(x2):
            c = compare(x1[i], x2[i])
            if c == 1:
                return 1
            if c == -1:
                return -1
            i += 1
        if i == len(x1) and i < len(x2):
            return 1
        elif i == len(x2) and i < len(x1):
            return -1
        else:
            return 0

    elif isinstance(x1, int) and isinstance(x2, list):
        x1 = [x1]
        return compare(x1, x2)
    elif isinstance(x1, list) and isinstance(x2, int):
        x2 = [x2]
        return compare(x1, x2)


answer = 0

for ind, line in enumerate(groups):
    p1, p2 = line.split('\n')
    p1 = eval(p1)
    p2 = eval(p2)
    if compare(p1, p2) == 1:
        answer += 1 + ind


print(answer)
