import random

def main():
    random.seed(1)

    print("This was generated with randint()")
    for x in range(5):
        my_random_number = random.randint(1, 10)
        
        print(my_random_number)

    print("This was generated with randrange()")
    for x in range(10):
        my_random_number = random.randrange(1, 11, 6)
        
        print(my_random_number)

if __name__ == "__main__":
    main()