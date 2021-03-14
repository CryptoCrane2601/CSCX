#good1

currentHour = int(input())

if currentHour >= 4 and currentHour <= 11:
    print('Good morning')
elif currentHour >= 12 and currentHour <= 17:
    print('Good afternoon')
elif currentHour >= 18 and currentHour <= 23:
    print('Good evening')
else:
    print('Hi')
