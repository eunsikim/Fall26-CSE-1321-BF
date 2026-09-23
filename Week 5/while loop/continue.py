def main():
    start = int(input("What is the starting number? ")) 
    end = int(input("What is the ending number? "))

    while start <= end:
        if start == 6:
            start += 1
            continue # Will forcefully skip to the NEXT iteration

        print(start)

        start += 1

    print("Program Terminated")

if __name__ == "__main__":
    main()