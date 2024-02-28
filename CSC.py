# THIS WORK WAS DONE BY JOSIAH DAVIS (DAVISTHEWEB), (Code written in global variable or scope)!!!!!
# I Defined empty lists for storing usernames and passwords
username = []
password = []
# Function to log in
def login():
    print("\t\t\t\t PLEASE LOGIN HERE")
    for x in range(2):
        user = input("ENTER USERNAME \n")
        userpass = input("\n ENTER USER PASSWORD \n")
        # Check if both username and password match
        if user in username and userpass == password[username.index(user)]:
            dashboard(user)
            break
    else:
        print("Login failed. You have exceeded the maximum number of attempts.")

# Function to register
def registration():
    print("\t\t\t\t REGISTER WITH US NOW")
    user = input("ENTER USERNAME \n")
    username.append(user)
    userpass = input("ENTER PASSWORD\n")
    if len (userpass) < 8:
        print("password cannot be less than 8 digit")
    else:
        password.append(userpass)
    login()  # After successful registration, proceed to login
# Function to display dashboard
def dashboard(user):
    print(f"Welcome, {user}! You are now logged in.")

# Function to welcome users and prompt for login or registration
def welcome():
    print("\t\t\t\t WELCOME TO OUR APP")
    a = input("ENTER 1 TO LOGIN OR 2 TO REGISTER \n")
    if a == '1':
        login()
    elif a == '2':
        registration()
    else:
        print("Invalid command")

# Call the welcome function to start the program
welcome()
