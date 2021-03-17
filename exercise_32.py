#add

import sys

def add(x,y):
    return x+y


for num in sys.stdin:
    x, y = num.split()
    x = int(x)
    y = int(y)
    num = num.strip()
    value = add(x,y)
    print(value)
