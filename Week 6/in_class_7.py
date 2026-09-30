# The X
# Create a program that prints in a 10 x 10 grid
# Two diagonal lines intersecting to form an X
#
# Sample output:
# X                          X  
#    X                    X     
#       X              X        
#          X        X           
#             X  X              
#             X  X              
#          X        X           
#       X              X        
#    X                    X     
# X                          X  
#
# Your output does not need to match exactly the 
# size of the sample output, as long it is 10
# characters wide and 10 characters long

for x in range(10):
    for y in range(10):
        if x == y:
            print("X", end="  ")
        elif x + y == 9:
            print("X", end="  ")
        else:
            print(" ", end="  ")
    print()