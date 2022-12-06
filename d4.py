with open('input.txt') as file:
    t = (file.read()).splitlines()

fully_overlap = 0
partly_overlap = len(t)

for line in t:
    compare = 0
    give_true = []
    fst = line.split(',')[0]
    snd = line.split(',')[1]

    fst_bgn = int(fst.split('-')[0])
    fst_end = int(fst.split('-')[1])
    snd_bgn = int(snd.split('-')[0])
    snd_end = int(snd.split('-')[1])

    # part 1
    if ((fst_bgn >= snd_bgn) and (fst_end <= snd_end)) or ((snd_bgn >= fst_bgn) and (snd_end <= fst_end)):
        fully_overlap += 1

    # part 2
    if snd_bgn > fst_end:
        partly_overlap -= 1
    elif fst_bgn > snd_end:
        partly_overlap -= 1

print(fully_overlap)
print(partly_overlap)
