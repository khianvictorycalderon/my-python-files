print("Python Register & Login System \nby Khian Calderon \n")
print("Type 'exit' to terminate the program\n--------------")

usernames = []
passwords = []

def loggedin():
    logout = input("Type 'Logout' to log out\n")
    print("--------------")
    if(logout.lower() == "logout") :
        print("Logging out....")
        print("Logged Out")
        print("--------------")
        ask()
    else :
        loggedin()
        
def login():
    print("--------------")
    print("Login")
    log_name = input("Enter your username: \n")
    if(log_name in usernames) :
        log_pass = input("Enter your password: \n")
        ind = usernames.index(log_name)
        if(log_pass == passwords[ind]) :
            print(f"Welcome {log_name}")
            loggedin()
        else :
            print("Incorrect Password!")
            print("--------------")
            ask()
    else :
        print("User does not exist")
        print("--------------")
        ask()
        

def reg():
    print("--------------")
    print("Register")
    reg_name = input("Enter your username: \n")
    if(reg_name.lower() in [username.lower() for username in usernames]) :
        print("Username already taken, try again")
        print("--------------")
        ask()
    else:
        reg_pass = input("Enter your password: \n")
        reg_confirmpass = input("Confirm your password: \n")
        if(reg_pass == reg_confirmpass) :
            usernames.append(reg_name)
            passwords.append(reg_pass)
            print("You are now a registered user, you may login now!")
            print("--------------")
            ask()
        else:
            print("Password does not match, registration failed, try again")
            print("--------------")
            ask()

def exit():
    print("--------------")
    print("Thank you for using my program\nHave a good day!")

def ask():
    x = input("Hello user, register or login? \n")
    if(x.lower()=="login") :
        login()
    elif (x.lower()=="register") :
        reg()
    elif (x.lower()=="exit") :
        exit()
    else:
        print("Invalid input, try again\n--------------")
        ask()

ask()