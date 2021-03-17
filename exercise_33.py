#mult

import sys

def mult(x,y,z):
    return x * y * z

for num in sys.stdin:
    x, y, z = num.split()
    x = int(x)
    y = int(y)
    z = int(z)
    num = num.strip()
    value = mult(x,y,z)
    print(value)

