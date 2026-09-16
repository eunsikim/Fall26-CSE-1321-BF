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

    match light_color:
        case "red":
            print("STOP")
        case "green":
            print("GO")
        case "yellow":
            is_close = input("Are you close to the intersection? (Y/N): ").upper()

            match is_close:
                case "Y":
                    print("Proceed with caution")
                case "N":
                    print("Slow down")
                case _:
                    print("Please enter Y or N")
        case _:
            print("Please enter Red, Yellow, or Green")

if __name__ == "__main__":
    main()