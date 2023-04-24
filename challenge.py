#!python3

"""
Population growth can be modeled with the equation P = p*(1+r)^n
Where 
P is the future Population
p is the current population
r is the annual rate of grown as a decimal
n is the number of years

Write a function to determine the future population

Given 2 groups with given starting populations and different rates of growth,
determine how many years in the future they will have the same population or 
if they are diverging and will never have the same population
"""
import math
import time
def population(p,r,n):
    P = round(p * math.pow((1 + r), n))
    print(P)
    return P

def equal(p1,r1,p2,r2):
    n = 0
    while True:
        n += 0.05
        P1 = round(p1 * math.pow((1 + r1), n))
        P2 = round(p2 * math.pow((1 + r2), n))
        if p1 < p2 and r1 < r2 or p1 > p2 and r1 > r2:
            print("None")
            return None
        elif P1 == P2:
            break
    
    print(round(n))
    return n

def tests():
    assert round(population(1000,.05, 5)) == 1276
    assert round(population(1000,.02, 20)) == 1486
    assert equal(1000,.05,2000,.06) == None
    assert round(equal(1000,.03,2000,.01)) == 35
    
if __name__ == "__main__":
    tests()
