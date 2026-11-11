class user:
    # Class Attributes or Class Fields
    username = ""
    password = ""

def main():
    user_1 = user()
    user_2 = user()

    user_1.username = "ekim54"
    user_1.password = "123"

    user_2.username = "jdoe01"
    user_2.password = "qwerty"

    print(f"User_1 username: {user_1.username}")
    print(f"User_1 password: {user_1.password}")
    print()
    print(f"User_2 username: {user_2.username}")
    print(f"User_2 password: {user_2.password}")

    user_2.username = "Hello World"

    print()
    print(f"User_1 username: {user_1.username}")
    print(f"User_1 password: {user_1.password}")
    print()
    print(f"User_2 username: {user_2.username}")
    print(f"User_2 password: {user_2.password}")

if __name__ == "__main__":
    main()