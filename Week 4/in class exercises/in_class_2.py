"""
Traffic Light:
- Ask the user whether the traffic light color is Red, Yellow, 
  or Green.
- User input should be case insensitive.
- Based on the user’s input, the program should output whether 
  the user should stop or go.
- For the case the traffic light is Yellow, ask the user if 
  they are close (Y/N) to the intersection and output if the user 
  should slow down or proceed with caution.
- Evaluate if the user’s input is valid or not (for example:
  "Please enter Red, Yellow, or Green")
"""

def main():
    light_color = input("What is the traffic light's color (Red, Yellow, or Green): ")

    # Changing `light_color` to lower-case
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


    light_color = input("What is the traffic light's color (Red, Yellow, or Green): ")
    
    # Changing `light_color` to lower-case
    light_color = light_color.lower()



if __name__ == "__main__":
    main()