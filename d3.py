with open('input.txt', mode='r') as file:
    t = (file.read()).splitlines()

doubled = []

for line in t:
    first = line[0:int((len(line)/2))]
    second = line[int((len(line)/2)):]

    checked = []

    for char in first:
        if char not in checked:
            if char in second:
                doubled.append(char)
                checked.append(char)


total = 0
for _ in doubled:
    if _.islower():
        total += ord(_) - 96

    else:
        total += ord(_) - 38

print(total)

