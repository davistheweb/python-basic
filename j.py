#call s routine or function named fatherName()
def fatherName():
   #create a variable called name for user to input father's name
   name = input ("Enter your Father's name: ")
   # used the return keyword so that the name variable which is stored can be accessed or be reused 
   return(name)

def fatherDOB():
   dob = input ("Enter your fathers date of birth: ")
   return(dob)

def fatherAge():
   #used int to convert user input to interger data type when the user inputs a number
   age = int(input ("Enter your father's Age: "))
   #created a variable called add_age so that we can use it to sum the father's age with the value given
   add_age = 20;
   #created a new variable for age and add_age to be sum(ed) up using the addition operator
   total_age = age + add_age
   return(total_age)

#created a new function which will be executed first
def fatherBio():
   print("Welcome to Father's bio.")

#called the function, so that it could be executed 
fatherBio()

""""the 'name = fatherName(),dob = fatherDOB,total_age=fatherAge()', is used 
to call back the function so that the user can input the given input field
"""
name =fatherName()
dob = fatherDOB()
total_age = fatherAge()


#Used the 'f (F-string (format string method))' to embed the user input from each variable 
#into the expresssions using the enclosed curly braces

print("Your father's name is: ",name)
print("Your Father's date of birth is: ",dob)
print ("Your father's age is: ",total_age)