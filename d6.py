with open('input.txt') as file:
    t = file.read()

for i in range(len(t)):
    if i - 3 >= 0 and len({t[i], t[i - 1], t[i - 2], t[i - 3]}) == 4:
        print(i+1)
        break

for i in range(len(t)):
    if i - 13 >= 0 and len(
            {t[i], t[i - 1], t[i - 2], t[i - 3], t[i - 4], t[i - 5], t[i - 6], t[i - 7], t[i - 8], t[i - 9], t[i - 10],
             t[i - 11], t[i - 12], t[i - 13], }) == 14:
        print(i + 1)

