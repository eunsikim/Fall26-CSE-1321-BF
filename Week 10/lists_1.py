import time

def main():
    # Initializing an empty list
    grades = []

    # Initializing a list with some initial values/items/elements
    my_favorite_numbers = [1, 3, 4]

    for index in range(len(my_favorite_numbers)):
        print(my_favorite_numbers[index])

    print()

    print("Adding up my favorite numbers...")

    my_favorite_numbers_sum = 0
    for number in my_favorite_numbers:
        print(f"sum: {my_favorite_numbers_sum}, adding: {number}")
        my_favorite_numbers_sum += number
        print(f"sum: {my_favorite_numbers_sum}")
        time.sleep(0.5)

    print(my_favorite_numbers_sum)

if __name__ == "__main__":
    main()