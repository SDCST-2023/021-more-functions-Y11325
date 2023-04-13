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
    print(f"sum = {total}")
    L = max(a1,a2,a3)
    S = min(a1,a2,a3)
    M = total - L - S
    print(L,S,M)
    return

assert triangle(12,5,13) == 2
'''
a = round(float(input("Enter one side: ")))
b = round(float(input("Enter a second side: ")))
c = round(float(input("Enter third side: ")))
apow = math.pow(a,2)
bpow = math.pow(b,2)
cpow = math.pow(c,2)
if a < b and b < c:
    sum = apow + bpow
    if sum > cpow:
        print("that is an acute triangle!\n")
    elif sum == cpow:
        print("that is a right triangle!\n")
    elif sum < cpow:
        print("that is an obtuse triangle!\n")
elif b < a and c < a:
    sum = bpow + cpow
    if sum > apow:
        print("that is an acute triangle!\n")
    elif sum == apow:
        print("that is a right triangle!\n")
    elif sum < apow:
        print("that is an obtuse triangle!\n")
elif a < b and c < b:
    sum = apow + cpow
    if sum > bpow:
        print("that is an acute triangle!\n")
    elif sum == bpow:
        print("that is a right triangle!\n")
    elif sum < bpow:
        print("that is an obtuse triangle!\n")
'''


def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


#if __name__== "__main__":
    #tests()
