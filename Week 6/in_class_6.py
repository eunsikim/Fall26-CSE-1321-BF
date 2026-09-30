# Diagonal
# Create a program that prints in a 10 x 10 grid
# A diagonal line that goes from the top-left
# corner, to the bottom-right corner
#
# Sample output:
# X                             
#    X                          
#       X                       
#          X                    
#             X                 
#                X              
#                   X           
#                      X        
#                         X     
#                            X  
#
# Your output does not need to match exactly the 
# size of the sample output, as long it is 10
# characters wide and 10 characters long

# x
# xx
# xxx
# xxxx

def main():
    size = 10

    for x in range(size):
        for y in range(x):
            print(" ", end="  ")
        print("X")

if __name__ == "__main__":
    main()