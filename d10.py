with open('input.txt') as file:
    t = file.read().splitlines()

cycle = 0
x = 1
score = 0
crt = [['?' for pixel in range(40)] for line in range(6)]


def tick(tt, x_value):
    global score
    global crt
    char = tt - 1
    crt[char // 40][char % 40] = ('#' if abs(x_value - (char % 40)) <= 1 else ' ')
    # print(char // 40, char % 40, x_value)
    if cycle in (20, 60, 100, 140, 180, 220):
        score += cycle * x
    # print(f"Cycle: {cycle}, x={x}, score={score}")


for line in t:
    cycle += 1
    tick(tt=cycle, x_value=x)
    if line.split(' ')[0] == 'addx':
        cycle += 1
        tick(cycle, x)
        x += int(line.split(' ')[1])


print(score)

for r in range(len(crt)):
    print(''.join(crt[r]))
