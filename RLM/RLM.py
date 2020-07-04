import sys
from itertools import groupby


f = open('data.txt', 'r')
for line in f:
    line = line.rstrip()
    op = None

    # Check which operation to perform
    if '+' in line:
        op = '+'
    elif '-' in line:
        op = '-'
    elif '*' in line:
        op = '*'
    elif '/' in line:
        op = '/'

    # If an operator is found, perform these steps, else return error
    if op is not None:
        line = line.split(op)
        line = [i.strip() for i in line]
        n1, n2 = '', ''

        # Convert them into normal numbers
        for i in range(0, len(line[0])-1, 2):
            n1 += line[0][i + 1]*int(line[0][i])

        for i in range(0, len(line[1])-1, 2):
            n2 += line[1][i + 1]*int(line[1][i])

        # Define the operations to perform
        ops = {'+': lambda x, y: x+y,
               '-': lambda x, y: x-y,
               '*': lambda x, y: x*y,
               '/': lambda x, y: x/y}

        # Preform the operation
        res = ops[op](int(n1), int(n2))
        # print(n1 + ' ' + op + ' ' + n2 + " =", res)

        # Convert it into a string
        str_res = str(res)
        # Count the number of occurrences of a digit
        groups = groupby(str_res)
        result = [[label, sum(1 for _ in group)] for label, group in groups]

        # Convert it into RLM form
        x = ''
        for i in result:
            if i[0] == '.':
                break
            if i[1] > 9:
                while i[1] > 9:
                    x += str(9) + i[0]
                    i[1] -= 9
            x += str(i[1]) + i[0]

        # Print the result
        print(line[0] + ' ' + op + ' ' + line[1] + " = " + x)

    else:
        # Error if operator is not found
        print("Operator not found!")
