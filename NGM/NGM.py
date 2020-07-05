import sys

f = open('data.txt', 'r')
print(['2' if int(line.rstrip()) % 10 == 0 else '1\n'+line.rstrip()[-1] for line in f][0])
