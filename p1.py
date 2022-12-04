with open('input_one.txt', mode='r') as file:
    test = file.read()

test = test.split('\n\n')
elves = []
for _ in test:
    elf = _.split('\n')
    elves.append(elf)

max_cal_1 = 0
max_cal_2 = 0
max_cal_3 = 0
for elf in elves:
    total = 0
    for item in elf:
        item = int(item)
        total += item
    if total > max_cal_1:
        max_cal_3 = max_cal_2
        max_cal_2 = max_cal_1
        max_cal_1 = total
    elif total > max_cal_2:
        max_cal_3 = max_cal_2
        max_cal_2 = total
    elif total > max_cal_3:
        max_cal_3 = total

print(max_cal_1 + max_cal_2 + max_cal_3)
