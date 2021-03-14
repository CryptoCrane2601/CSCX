def plusOne(number):
    return number + 1
   

userNum = int(input())
newNumber = plusOne(userNum)
if newNumber <= 0 and newNumber >= 100000:
    print('Please use number between 0 and 100000')
else:
    print(newNumber)

