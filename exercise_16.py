#triangle1

x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x != y and y != z and z != x:
    print('scalene')
elif x != y or x != z or y != z:
    print('isosceles')
elif x == y and y == z and x == z:
    print('equilateral')
elif x + y <= z or x + z <= y or y + z <= x:
    print('impossible')
