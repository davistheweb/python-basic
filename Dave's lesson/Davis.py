#string fromat.
''''''''''
std= 'joy'
lecturer= 'mr drake'
print("I am {} and my lecturer is {}".format(std,lecturer))
'''
"""""""""
Age= 36
Name= 'John'
print("His name is {1}.{1} is {0} old" .format(Age,Name) )
"""""""""
"""""""""
quantity= 50
item_no= 205
price= 2565
print("The product item no is {1}, But the item no is not up to {1}, please give me {0} quantities at {2} dollars. {2} dollars is a good price for the {0} quantities. \n Thank you very much" .format(quantity, item_no, price))
"""""""""
#python if else statement
"""""""""
num=int(input("Enter a no: "))
if num % 2 ==0:
 print ("number is even")
"""""""""
#Assignment
"""""""""
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c

print(largest, "is the largest of the three numbers.")
"""""""""""
"""""""""""
#python modify string
a='Hello,World'
print(a.replace("H","fan"))
"""""""""""
"""""""""""
a='day* break'
print(a.split(','))
"""""""""""
#Python condition, if statement, else statement & elif statement.
"""""""""""
a=33
b=206
if a==b:
    print("a is equal to b")
else:
    print("the value is wrong")
"""""""""""
"""""""""""
a=33
b=203
if a<b:
    print("a is less than b")
else:
    print("The value is wrong")
"""""""""""
"""""""""""
number1=int(input("Enter first no: "))
number2=int(input("enter second number: "))
if number1>number2:
    largest_no=number1
else:
    largest_no=number2
    print("The largest no is:", largest_no)
"""""""""""
#IF-ELIF-ELSE_ STATEMENTS
"""""""""""
a = input("please enter a no: ")
b = input("please enter a no: ")
if a >  b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
elif a==b:
    print("a is equal to b")
else:
    print("invalid no")
"""""""""""
#program to print the largest of three numbers.
"""""""""""
a = input("please enter the ist  no: ")
b = input("please enter the 2nd no: ")
c = input("please enter the 3rd no: ")
if a > b and a > c:
    print("a is the largest no")
if b > a and b > c:
    print("b is the largest no")
if c > a and c > b:
    print("c is the largest no")
"""""""""""
"""""""""""
x = 200
y = 33
if x < y:
    print("x is less than y")
elif x==y:
    print("x is equal to y")
else:
    print("x is greater than y")
"""""""""""
#OPERATORS
#ARITHEMITIC OPERATOR
"""""""""""
x = 3
y = 2
a = x + y
b = x * y
c = x / y
d = x - y
e = x % y
f = x ** 2
g = x // y
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
"""""""""""
#COMPARISON OPERATOR
"""""""""""
a = 5
b = 8
if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")
"""""""""""
#ASSIGNMENT OPERATORS
"""""""""""
x = 2
y = 3
x += y
print(x)
"""""""""""
#OR
"""""""""""""""
x = 2
y = 3
x = x + y
print(x)
"""""""""""""""
#LOOPS.
"""""""""""""""
fruit=['Apple', 'Mango', 'orange','pear']
for i in fruit:
 print(i)
"""""""""""""""
"""""""""""""""
number=(1,2,3,4,5,6,7,8,9,10)
for x in number:
    print(x)
"""""""""""""""
"""""""""""""""
number=(1,2,3,4,5,6,7,8,9,10)
for x in number:
    print(x+2)
"""""""""""""""
"""""""""""""""
number=(1,2,3,4,5,6,7,8,9,10)
for x in number:
    print(x*2)
"""""""""""""""
"""""""""""""""
number=(2,4,1,3,5,6)
for x in number:
    print(x**2)
"""""""""""""""
"""""""""""""""
number=(2,4,1,3,5,6)
sum=0
for x in number:
    sum=sum+(x**2)
print(sum)
"""""""""""""""
"""""""""""""""
for x  in 'banana':
    print(x)
"""""""""""""""
"""""""""""""""
x=(1,2,3,4,5)
for i in x :
    print(i)
    if i == 3:
        break
"""""""""""""""""
"""""""""""""""
x=(1,2,3,4,5)
for i in x :
    if i == 3:
        break
    print(i)
'"""""""""""
#FORLOOP.
"""""""""""""""
name='elephant'
for i in name:
    print (i)
"""""""""""""""
"""""""""""""""
numbers=[3,5,23,10,8,4,9,6]
for x in numbers:
    print(x**2)
"""""""""""""""""
"""""""""""""""""
numbers=[3,5,23,10,8,4,9,6]
for x in numbers:
    print(x/2)
"""""""""""""""""
"""""""""""""""""
numbers=[3,5,23,10,8,4,9,6]
sum=0
for x in numbers:
    sum = sum + (x)
print (sum)
"""""""""""""""""
#find the cube of every element and sum it.
"""""""""""""""""
numbers=[3,5,23,10,8,4,9,6]
sum=0
for x in numbers:
    sum = sum + (x**3)
print (sum)
"""""""""""""""""
"""""""""""""""""
for x in range(10):
    print(x)
"""""""""""""""""
"""""""""""""""""
for x in range (3,8):
    print(x)
"""""""""""""""""
"""""""""""""""""
for x in range (2,8,2):
    print(x)
"""""""""""""""""
#write a program that uses
"""""""""""""""""
x=('mississippily')
for i in x:
    print(x)
"""""""""""""""""
"""""""""""""""""
thislist=["apple", "banana", "cherry",]
for i in range (len(thislist)):
        print(thislist[i])
"""""""""""""""""
"""""""""""""""""
new=['apple', 'mango','orange','lemon',]
for x in new:
        print(x)
        if x == 'mango':
                break
"""""""""""""""""
"""""""""""""""""
new=['apple', 'mango','orange','lemon',]
for x in new:
        if x == 'mango':
                break
        print(x)
"""""""""""""""""
"""""""""""""""""
new=['apple', 'mango','orange','lemon', 'pear','carrot']
for x in new:
        if x == 'orange':
                continue
        print(x)
"""""""""""""""""
"""""""""""""""""
x=5
while x>5:
   print(x)
"""""""""""""""""
"""""""""""""""""
x=3
while x<=5:
    print (x)
"""""""""""""""""
"""""""""""""""""
x=3
while True:
    print (x)
"""""""""""""""""
"""""""""""""""""
x=1
while x<=10:
    print(x)
    x +=1
"""""""""""""""""
#write a program that reads a sequence of number and count how many numbers are even and how many are odd,
# The program terminate when zero is entered
"""""""""""""""""
odd_no=0
even_no=0
number=int(input("please enter a no: or type 0 to stop: "))
while number !=0:
    if number % 2 == 1 :
        odd_no +=1
    else:
        even_no +=1
    number=int(input("please enter a no: "))
    z = odd_no + even_no
print("total no you entered is: ",z )
print("No of odd no is:", odd_no)
print("No of even no is", even_no)
"""""""""""""""""
#wirte a program to print 1 to ten using while loop
"""""""""""""""""
x=1
while x<=10:
    print(x)
    x +=1
"""""""""""""""""
"""""""""""""""""
i = 1
number = int(input("Enter a no: "))
while i<=12:
    print("%dx%d=%d" "\n" %(number,i,number *i))
    i  += 1
"""""""""""""""""
