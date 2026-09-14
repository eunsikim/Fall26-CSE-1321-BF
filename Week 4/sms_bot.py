def main():
    print("You've been subscribed to Instructor Kim's CSE 1321 Newsletter")
    print("Enter YES to keep your subcription or NO to stop")
    response = input("> ")

    response = response.upper()

    match response:
        case "YES":
            print("You are still subscribed")
        case "NO":
            print("You have unsubscribed from Instructor Kim's CSE 1321 Newsletter")
        case _:
            print("Please enter YES or NO")

if __name__ == "__main__":
    main()