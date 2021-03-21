#oddeven

import sys

for userNum in sys.stdin:
    userNum = int(userNum)
    if userNum % 2 == 0:
        print('even')
    else:
        print('odd')
