#hi

import fileinput

for name in fileinput.input():
    print('Hello, ' + name.rstrip() +'!')
