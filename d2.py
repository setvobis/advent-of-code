with open('input.txt', mode='r') as file:
    t = (file.read()).splitlines()

total = 0
for line in t:
    first = line.split(' ')[0]
    second = line.split(' ')[1]
    second = second.replace('X', 'A')
    second = second.replace('Y', 'B')
    second = second.replace('Z', 'C')

    if first == 'A':
        if second == 'A':
            total += 4
        elif second == 'B':
            total += 8
        else:
            total += 3
    elif first == 'B':
        if second == 'A':
            total += 1
        elif second == 'B':
            total += 5
        else:
            total += 9
    else:
        if second == 'A':
            total += 7
        elif second == 'B':
            total += 2
        else:
            total += 6

print(total)