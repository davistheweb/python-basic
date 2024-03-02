def fatherName():
   name = input ("Enter your Father's name: ")
   return(name)

def fatherDOB():
   dob = input ("Enter your fathers date of birth: ")
   return(dob)

def fatherAge():
   age = int(input ("Enter your father's Age: "))
   add_age = 20;
   total_age = age + add_age
   return(total_age)

def fatherBio():
   print("Welcome to Father's bio.")

  
fatherBio()
name =fatherName()
dob = fatherDOB()
total_age = fatherAge()

print(f"Your father's name is: {name}")
print(f"Your Father's date of birth is: {dob}")
print (f"Your father's age is: {total_age}")