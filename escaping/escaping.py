import sys
import re
import numpy as np
from itertools import combinations_with_replacement, combinations

f = open('data.txt', 'r')
it = 0
for line in f:
    line = line.rstrip()
    if it == 0:
        it += 1
        continue

    code = int(line)
    res = 0
    if '0' not in line:
        print('1')
        continue
    elif '1' not in line:
        print('1')
        continue
    for r in range(2, len(line)):
        n = np.append(np.zeros(r, dtype=int), np.ones(r, dtype=int))
        n = list(n)
        # print(n)
        esc = combinations(n, r)
        esc = list(esc)
        # print(esc)
        for i in esc:
            check = ''.join(str(j) for j in i)
            # print(check)
            if re.search(check, line) is not None:
                continue
            res = len(check)
            break
        if res > 0:
            break
    print(res)