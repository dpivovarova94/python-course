# Write a program that takes a point (x,y)
#  from the user and finds the quadrant where the point lies on a Cartesian plane.

# The following illustration will help you to understand where each point lies on the Cartesian plane.

# Write you code below
first_point = int(input("Enter the first coordinate? "))
second_point = int(input("Enter the second coordinate? "))

if first_point >= 0:
    if second_point >= 0:
        print("The point lies in the 1st Quadrant.")
    else:
        print("The point lies in the 4th Quadrant.")
else:
    if second_point > 0:
        print("The point lies in the 2nd Quadrant.")
    else:
        print("The point lies in the 3rd Quadrant.")
