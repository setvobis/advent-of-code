with open('input.txt') as file:
    s = file.read().splitlines()[:9]
    from itertools import zip_longest

    transposed = list(zip_longest(*s))
    transposed_list = [str(tuples) for tuples in transposed]
    stripped_transposed_list = []
    for line in transposed_list:
        for ch in line:
            if not ch.isalpha():
                line = line.replace(ch, '').strip('')

        if len(line) != 0:
            if line != 'None':
                stripped_transposed_list.append(line)

    loading_area = {}
    for count, ele in enumerate(stripped_transposed_list, 1):
        loading_area[count] = [*ele]

file.close()


with open('input.txt') as file:
    transposed_list = (file.read()).splitlines()[10:]

for line in transposed_list:
    how_many, stack_from, stack_to = [int(line.split(' ')[i]) for i in (1, 3, 5)]
    gcc = loading_area[stack_from][:how_many]
    # comment out gcc.reverse for '`9001` upgrade' a.k.a. part 2
    gcc.reverse()
    loading_area[stack_to][:0] = gcc
    del loading_area[stack_from][:how_many]

answer = ""
x = 1
for k in loading_area.items():
    answer += loading_area[x][0]
    x += 1

print(answer)
