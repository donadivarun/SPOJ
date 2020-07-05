import sys

f = open('data.txt', 'r')
for line in f:
    counter = 0
    line = line.rstrip()
    res = int(line)
    while res != 0:
        sort_res = list(map(int, list(str(res))))
        sort_res.sort()
        rev = int(''.join(list(map(str, sort_res))))
        res -= rev
        counter += 1
    print(counter)