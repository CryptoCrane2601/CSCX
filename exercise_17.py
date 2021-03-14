#factorial1

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n - 1)

number = int(input())
if number <0 or number >= 10:
    print('Please use only number between 0 and 10!')
else:
    factorialOfN = factorial(number)
    print(factorialOfN)




        
