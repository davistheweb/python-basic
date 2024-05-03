def my_dad_name():
      name = input("Enter father's name")
      return(name)
def my_dad_dateofbirth():
      date_of_birth = input("Enter father's date of birth")
      return( date_of_birth)
def my_dad_age():
      age = int(input("Enter father's age: "))
      add_age = 20
      total_age = add_age + age
      return(total_age)
def welcomeuser():
      print("Pls Input your father's bio")

welcomeuser()

name=my_dad_name()
date_of_birth = my_dad_dateofbirth()
total_age = my_dad_age()

print(f"Your father's name is {name}")
print(f"Your father's date of birth is {date_of_birth}")
print(f"My dad age is {total_age}")