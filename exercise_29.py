#owes

import sys

for line in sys.stdin:
    amount,name1,name2 = line.split()
    amount = float(amount)
    line = line.strip()
    print(name1 + ' owes ' + '$' + "%.2f" % amount + ' dollars to ' + name2 + '.')

