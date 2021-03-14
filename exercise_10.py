def mult(x,y,z):
    return x * y * z

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
newValue = mult(x, y, z)
print(newValue)
