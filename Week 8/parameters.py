def calculation(n1, n2 = 2, n3 = 1): # Optional params should always be define after the required params.
    return (n1 + n2) * n3

def main():
    result = calculation(10) # n2 and n3 are defined by their default values 

    print("Performing calculation", end=": ")
    print(result)

    print()

    result = calculation(10, 3) # n2 is defined as 3 and n3 is defined by its default value

    print("Performing calculation", end=": ")
    print(result)

    print()

    result = calculation(10, n3=5) # n2 is defined by its default value, n3 is defined as 5
    
    print("Performing calculation", end=": ")
    print(result)

if __name__ == "__main__":
    main()