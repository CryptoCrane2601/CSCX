#inc

import sys

def inc(x):
   return x + 1

for num in sys.stdin:
    num = num.strip()
    num = int(num)
    newNum = inc(num)
    print(newNum)
    
    
        
         
        
    





        
    
