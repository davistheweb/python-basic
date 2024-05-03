def theFatherSname():
   father_name = input ("Enter your Father's name: ")
   return(father_name)

def fatherDATEOFBIRTH():
   father_dateofbirth = input ("Enter your fathers date of birth: ")
   return(father_dateofbirth)

def Father_Age():
   father_age = int(input ("Enter your father's Age: "))
   add_father_age = 20;
   total_age = father_age + add_father_age
   return(total_age)

def fatherInoformation():
   print("Welcome to Father's bio.")
fatherInoformation()

father_nam = theFatherSname()
father_dateofbirt = fatherDATEOFBIRTH()
total_ag = Father_Age()

print(f"Your father's name is: {father_nam}")
print(f"Your Father's date of birth is: {father_dateofbirt}")
print (f"Your father's age is: {total_ag}")