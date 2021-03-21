#pi

import sys

def circumference(r):
    p = float(3.141592653)
    return float(2) * p * float(r)
    
def area(r):
    p = float(3.141592653) 
    return p * float(r) ** 2

for num in sys.stdin:
    num = num.strip()
    newValue = circumference(num)
    newValue2 = area(num)
    newValue = format(newValue, '.2f')
    newValue2 = format(newValue2, '.2f')
    print(newValue,newValue2)
