# Ask the user to input an username and a password
# We verify that the username is "admin" and the password
# is "password123"
# If the login is successful print "Login Successful" and
# terminate the program
# If not, print "Login Not Successful" and terminate the program

def main():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin":
        if password == "password123":
            print("Login Successful")
        else:
            print("Login Not Successful")
    else:
        print("Login Not Successful")


if __name__ == "__main__":
    main()