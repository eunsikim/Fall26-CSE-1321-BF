def main():
    order = input("What is your shape?: ")

    match order:
        case "Square":
            print("You should put the shape in the square hole")
        case "Circle":
            print("You should put the shape in the circle hole")
        case "Triangle":
            print("You should put the shape in the triangle hole")
        case _:
            print("I do not know that shape")



if __name__ == "__main__":
    main()