# This is an update on "Week 4/in class exercoses/in_class_2.py"

def main():
    light_color = "" # We define this variable as an "empty" string.

    # Input Validation: We make sure the user MUST enter values we expect the user to input.
    while light_color != "red" and light_color != "yellow" and light_color != "green":
        light_color = input("What is the traffic light's color (Red, Yellow, or Green): ")

        light_color = light_color.lower()

        if light_color == "red":
            print("STOP")
        elif light_color == "green":
            print("GO")
        elif light_color == "yellow":
            is_close = input("Are you close to the intersection? (Y/N): ").upper()

            if is_close == "Y":
                print("Proceed with caution")
            elif is_close == "N":
                print("Slow down")
            else:
                print("Please enter Y or N")
        else:
            print("Please enter Red, Yellow, or Green. Try again!")
    
    print("[Program Terminated]")

if __name__ == "__main__":
    main()