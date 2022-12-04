with open('input.txt', mode='r') as file:
    t = (file.read()).splitlines()

stack_o = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]

groups = stack_o(lst=t, sz=3)

badges = []
for group in groups:
    first = group[0]
    second = group[1]
    third = group[2]
    checked_items = []
    for item in first:
        if item not in checked_items:
            if item in second:
                if item in third:
                    checked_items.append(item)
                    badges.append(item)

total = 0
for _ in badges:
    if _.islower():
        total += ord(_) - 96

    else:
        total += ord(_) - 38

print(total)
