# Ask the user to input an username and a password
# We verify that the username is "admin" and the password
# is "password123"
# If the login is successful print "Login Successful" and
# terminate the program
# If not, print whether the username or the password was incorrect or both

def main():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "password123":
        print("Login Successful")
    else: # Assumption: Either username is incorrect or password or both
        if username == "admin":
            print("Password Incorrect")
        elif password == "password123":
            print("Username Incorrect")
        else:
            print("Both Username and Password are incorrect")
        


if __name__ == "__main__":
    main()