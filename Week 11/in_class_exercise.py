"""
Create program where you ask the user to enter 5 colors,
then ask the user to rank these colors from 1 (least favorite) 
- 10 (favorite)

Then, print out the user's favorite colors (only rank 8 or greater)

You have to implement a dictionary to keep track of colors and their
ranking.

Sample Output:
Enter a color: Blue
Enter a color: Brown
Enter a color: Red
Enter a color: Green
Enter a color: Yellow

Rank the color Blue (1 to 10): 10
Rank the color Brown (1 to 10): 8
Rank the color Red (1 to 10): 4
Rank the color Green (1 to 10): 5
Rank the color Yellow (1 to 10): 2

Your favorite colors are:
Blue
Brown
"""

def approach_1():
    color_rankings = {}

    colors = []

    for i in range(5):
        color = input("Enter a color: ")
        colors.append(color)

    print()

    for color in colors:
        ranking = int(input(f"Rank the color {color} (1 to 10): "))
        color_rankings[color] = ranking

    print()

    print("Your favorite colors are:")
    for key in color_rankings:
        if color_rankings[key] >= 8:
            print(key)


def approach_2():
    color_rankings = {}

    for i in range(5):
        color = input("Enter a color: ")
        color_rankings[color] = 0

    print()

    for key in color_rankings:
        ranking = int(input(f"Rank the color {key} (1 to 10): "))
        color_rankings[key] = ranking

    print()

    print("Your favorite colors are:")
    for key in color_rankings:
        if color_rankings[key] >= 8:
            print(key)

approach_2()

