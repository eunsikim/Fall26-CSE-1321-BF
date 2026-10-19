"""
Alarm Clock

Create a program where the user can enter an 
amount of minutes. The program should then 
wait for that time period and print out "WAKE UP!" 
at the end of said time.
"""
import time

def main():
    minutes = int(input("Minutes: "))

    for x in range(minutes):
        time.sleep(60)

if __name__ == "__main__":
    main()