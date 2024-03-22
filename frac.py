# MOST SIMPLE WAY
""" import math

num = int(input("Enter a number to get its factorial: "))

factorailz = math.factorial(num)

print("the factorail of", num, 'is' , factorailz ) """

#HARD WAY
def factorial(n):
    if n ==0:
        return 1
    else: 
        return n * factorial(n - 1)

number = int(input('enter a number: '))

if number == 0 or number < 0:
    print('invalid')
else:
    print('factorial of ', number, 'is', factorial(number))