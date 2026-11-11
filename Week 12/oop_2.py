class user:
    # Class Attributes or Class Fields
    # These attribute will belong to the class
    # unless you manually promote these attributes
    username = "Hello"
    password = "World"

def main():
    user.password = "CSE 1321"
    user.username = "Goodbye"

    user_1 = user()

    user_2 = user()

    # This line of code is promoting the class attribute "username" to
    # a object attribute
    user_2.username = "jdoe01"

    print(user_1.username)
    print(user_1.password)
    print()
    print(user_2.username)
    print(user_2.password)

if __name__ == "__main__":
    main()