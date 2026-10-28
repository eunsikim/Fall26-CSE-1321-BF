def main():
    grades = [95.6, 81.5, 70.0]

    print(grades)

    print(f"Updating the value at index 1...")

    # We can update values by the index
    grades[1] = 90.0
    
    print(grades)

if __name__ == "__main__":
    main()