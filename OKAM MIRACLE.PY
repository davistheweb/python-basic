def withdraw():
    print("Withdraw successful")


def welcome():
    print("welcome user")
    option1 = input("Enter 1 to withdraw")

    if option1 == 1:
        withdraw()

    else:
        print("Invalid option")
