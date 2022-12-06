with open('input.txt', mode='r') as file:
    t = (file.read()).splitlines()

answer_1 = 0
answer_2 = 0
for line in t:
    first = line.split(' ')[0]
    second = line.split(' ')[1]

    if first == 'A':
        if second == 'X':
            answer_1 += 4
        elif second == 'Y':
            answer_1 += 8
        else:
            answer_1 += 3
    elif first == 'B':
        if second == 'X':
            answer_1 += 1
        elif second == 'Y':
            answer_1 += 5
        else:
            answer_1 += 9
    else:
        if second == 'X':
            answer_1 += 7
        elif second == 'Y':
            answer_1 += 2
        else:
            answer_1 += 6

    # part 2
    if first == 'A':
        if second == 'X':
            answer_2 += 3
        elif second == 'Y':
            answer_2 += 4
        else:
            answer_2 += 8
    elif first == 'B':
        if second == 'X':
            answer_2 += 1
        elif second == 'Y':
            answer_2 += 5
        else:
            answer_2 += 9
    else:
        if second == 'X':
            answer_2 += 2
        elif second == 'Y':
            answer_2 += 6
        else:
            answer_2 += 7

print(answer_1)
print(answer_2)
