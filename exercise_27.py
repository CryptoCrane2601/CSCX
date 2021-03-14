#age

import sys

for line in sys.stdin:
    name, age = line.split()
    age = int(age)
    line = line.strip()
    print(name + ' is ' + str(age) + ' years old.')


    
    
