#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
import math

def triangle(n1, n2, n3):
    a1 = math.pow(n1,2)
    a2 = math.pow(n2,2)
    a3 = math.pow(n3,2)

    area = [a1,a2,a3]
    total = sum(area)
    Lar = max(a1,a2,a3)
    Sma = min(a1,a2,a3)
    Med = total - Lar - Sma

    perimeter = [n1,n2,n3]
    P = sum(perimeter)
    l = max(n1,n2,n3)
    s = min(n1,n2,n3)
    m = P - l - s

    if s + m <= l:
        val = 0
    elif Sma + Med > Lar:
        val = 1
    elif Sma + Med == Lar:
        val = 2
    elif Sma + Med < Lar:
        val = 3

    return val


def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  

if __name__== "__main__":
    tests()