#!python3
"""
Create a function that converts the price of Bitcoin into Canadian Dollars .
The function will require 2 input parameters:
float: amount of currency being converted

return: float value in Canadian Dollars
You will make use of a local variable called "currBTC"
currBTC shows that the conversion is 1 btc = 45000 cad

Sample assertions:

assert btcTocad(1) == 45000
(2 points) 
"""

def btcTocad(btc):
    try:   
        b = float(btc)
        cad = b * 45000
        print(cad)
    except:
        cad = print("error\n")

    return cad

"""
This checks to see if you are running the program as the main script or
if it is imported by another program.
If this py file is imported by another program, then the commands below
are not executed.
"""

try:    
    if __name__ == "__main__":
        assert btcTocad(1) == 45000
        assert btcTocad(2.5) == 135000
        assert btcTocad('one') == 'error'
except:
    print("error")


def main():

    currBTC = btcTocad(1)
    assert currBTC == 45000
    print("\n<<<Bitcoin to Canadian Dollars>>>\n")
    btc = input("Enter the amount of bitcoin: ")
    btcTocad(btc)

main()

while True:
    again = input("Play again?(y/n): ")
    if again == "y":
        main()
    else:
        print("\n\n---Thanks for playing---\n\n")
        break