# Work done By Josiah Davis
# to checks each possible letter grade and return the corresponding grade point value.
def getGradePoint(courseLetterGrade):
    if courseLetterGrade == "A":
        return 4.0
    elif courseLetterGrade == "A-":
        return 3.67
    elif courseLetterGrade == "B+":
        return 3.33
    elif courseLetterGrade == "B":
        return 3.0
    elif courseLetterGrade == "B-":
        return 2.67
    elif courseLetterGrade == "C+":
        return 2.33
    elif courseLetterGrade == "C":
        return 2.0
    elif courseLetterGrade == "D":
        return 1.0
    else:
        return 0.0

def run():
#1 to covert user input to string datatype
    courseLetterGrade1 = str(input("Enter your course 1 letter grade: "))
#2 to covert user input to float datatype
    courseCredit1 = float(input("Enter your course 1 credit: "))
#1
    courseLetterGrade2 = str(input("Enter your course 2 letter grade: "))
#2
    courseCredit2 = float(input("Enter your course 2 credit: "))
#1
    courseLetterGrade3 = str(input("Enter your course 3 letter grade: "))
#2
    courseCredit3 = float(input("Enter your course 3 credit: "))

#to calculate grade of each courses obtained
    totalGrade = (getGradePoint(courseLetterGrade1) * courseCredit1) + \
                           (getGradePoint(courseLetterGrade2) * courseCredit2) + \
                           (getGradePoint(courseLetterGrade3) * courseCredit3)
    
# to add credit obtained

    totalCredits = courseCredit1 + courseCredit2 + courseCredit3
#divide totalGrade by totalCredits
    GPA = totalGrade / totalCredits

# print the result from "GPA" (F-string (format string {GPA} and execute in string datatype))
    print(f"Your GPA is: {str (GPA)}")

# to check if the script is running directly (not imported from or as a path of another program)
if __name__ == "__main__":
#then it execute the run function if it is (true)
    run()
