def add(num1, num2):
    return num1 + num2

x, y = input().split()
x = int(x)
y = int(y)
newValue = add(x, y)
print(newValue)
