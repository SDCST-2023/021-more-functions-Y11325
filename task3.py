#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""
import math

def hypotenuse(n1,n2):
    try:
        if n1 < 0:
            c = None
        elif n2 < 0:
            c = None
        else:
            float(n1)
            float(n2)
            c = round(math.sqrt(math.pow(n1,2) + math.pow(n2,2)), 2)
            print(c)
    except:
        c = print("Something's wrong\n")
    return c

assert hypotenuse(6,8) == 10
assert hypotenuse(5,12) == 13
assert hypotenuse(4,6) == 7.21
assert hypotenuse(-3,4) == None