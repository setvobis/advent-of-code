with open('input.txt', mode='r') as file:
    t = (file.read()).splitlines()

total = 0
for line in t:
    first = line.split(' ')[0]
    second = line.split(' ')[1]

    if first == 'A':
        if second == 'X':
            total += 3
        elif second == 'Y':
            total += 4
        else:
            total += 8
    elif first == 'B':
        if second == 'X':
            total += 1
        elif second == 'Y':
            total += 5
        else:
            total += 9
    else:
        if second == 'X':
            total += 2
        elif second == 'Y':
            total += 6
        else:
            total += 7

print(total)
