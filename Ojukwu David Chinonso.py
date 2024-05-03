class Dad_Bio:
    def __init__(self, dad_name, dad_birth_year, dad_current_age):
        self.name = dad_name
        self.birth_year = dad_birth_year
        self.current_age =dad_current_age

    def print_info(self):
        print("Name:", self.name)
        print("Year of birth:", self.birth_year)
        print("Current age plus 20:", self.current_age + 20)
        
     # Creating an instance of dad
dad = Dad_Bio("ISAAC", 1940, 45)

    #  Printing Dad's information


dad.print_info()