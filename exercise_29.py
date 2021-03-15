#owes

import sys

for line in sys.stdin:
    name1,value1,name2 = line.split()
    line = line.strip()
    print(name1 + ' owes ' + '$'+str(value1) + ' dollars to ' + name2)

