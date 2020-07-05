import sys
import re

f = open('data.txt', 'r')
it = 0
colors = 'RGB'
for line in f:
    line = line.rstrip()
    it += 1

    if it == 1:
        continue
    if it % 2 == 0:
        continue

    while True:
        prev = line
        p1, p2, p3 = 1, 1, 1
        x1 = re.search(r'RG|GR', line)
        x2 = re.search(r'GB|BG', line)
        x3 = re.search(r'BR|RB', line)
        if x1 is not None:
            p1 = x1.start() * 10e-8
        if x2 is not None:
            p2 = x2.start() * 10e-8
        if x3 is not None:
            p3 = x3.start() * 10e-8

        if p1 < p2 and p1 < p3:
            line = re.sub('RG', 'B', line)
            line = re.sub('GR', 'B', line)
        if p2 < p1 and p2 < p3:
            line = re.sub('BG', 'R', line)
            line = re.sub('GB', 'R', line)
        if p3 < p1 and p3 < p2:
            line = re.sub('RB', 'G', line)
            line = re.sub('BR', 'G', line)
        if prev == line:
            break

    print(len(line))
