#power1

def power(b, n):
    return b ** n

b, n = input().split()
b = int(b)
n = int(n)
x = power(b, n)
print(x)
    
