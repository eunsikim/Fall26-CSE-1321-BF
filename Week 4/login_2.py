# Ask the user to input an username and a password
# We verify that the username is "admin" and the password
# is "password123"
# If the login is successful print "Login Successful" and
# terminate the program
# If not, print whether the username or the password was incorrect or both

def main():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin":
        if password == "password123":
            print("Login Successful")
        else:
            print("Incorrect Password")
    elif password != "password123":
        print("Both password and username are incorrect")
    else:
        print("Incorrect Username")


if __name__ == "__main__":
    main()