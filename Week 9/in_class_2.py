"""
Alarm Clock

Create a program where the user can enter an 
amount of minutes. 

The program should then wait for that time period.

The program should print every 1 second the current time

at the end of said time, the program should print out 
"WAKE UP!" .
"""

import time

minutes = int(input("Enter the number of minutes: "))

seconds = minutes * 60

for i in range(seconds):
    print(time.ctime(time.time()))
    time.sleep(1)

print("WAKE UP!")