import math

with open('input.txt') as file:
    t = file.read().splitlines()
    new_t = []
    for line in t:
        new_t.append(line.strip().strip(',:').split())

monkeys = []

# same as in d3_2.py
stack_o = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
groups = stack_o(lst=new_t, sz=7)

for m in groups:
    monkey = [[int(str(x).strip(',')) for x in m[1][2:]], m[2][4:], int(m[3][3]), int(m[4][5]), int(m[5][5]), 0]
    monkeys.append(monkey)

p = 1
for m in monkeys:
    # print(m)
    p *= (p*m[2]) // math.gcd(p, m[2])

# part 1
# for _ in range(20):
# part 2
for _ in range(10000):
    for m in monkeys:
        if len(m[0]) != 0:
            inspected = 0
            for i in m[0]:
                if m[1][0] == '*':
                    if m[1][1] == 'old':
                        val = (i * i)
                    else:
                        val = (i * int(m[1][1]))
                else:
                    val = (i + int(m[1][1]))
                # part 1
                # val = val // 3
                # part 2
                val = val % p
                if val % m[2] == 0:
                    monkeys[m[3]][0].append(val)
                else:
                    monkeys[m[4]][0].append(val)
                inspected += 1
            m[0] = []
            m[5] += inspected


most_busy = []
for m in monkeys:
    # print(m)
    most_busy.append(m[5])

most_busy.sort(reverse=True)
print(most_busy[0]*most_busy[1])
