"""
Alarm Clock

Create a program where the user can enter an 
amount of minutes. 

The program should then wait for that time period.

While waiting, the program should print a random
number (from 1 to 5) of `Z` every second.

at the end of said time, the program should print out 
"WAKE UP!".
"""

import random
import time

minutes = int(input("Enter the number of minutes: "))

seconds = minutes * 60

for i in range(seconds):
    Z = random.randint(1,5)
    
    for j in range(Z):
        print("Z", end="")
    print("")

    time.sleep(1)

print("WAKE UP!")