#!python3

"""
Create a function that determines the area of a circle if given the radius
1 input parameter
float: radius

return: float area for the circle

note: Area of a circle is given by A = pi*(square of the radius)
You may want to use the math module to complete this problem
"""
import math
def area(r):
    r = float(r)
    A = round(math.pi * math.pow(r,2),2)
    print(f"{A}\n\n")
    return A


assert round(area(2),2) == 12.57

def main():
    try:
        print("\n<<< Calculate the area of a circle >>>\n")
        n = float(input("Enter the radius: "))
        area(n)
    except:
        print("ERROR\n\n")

main()