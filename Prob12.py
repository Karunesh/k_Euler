# prob12.py
import math

def getNumFactors(number):
    """
    Returns number of natural numbers that exactly divide number,
    including 1 and number itself.
    """

    numFactors = 2 # Already accounting for 1 and number itself.

    i = 2
    for i in range(2, int(number / 2)):
        if (number % i) == 0:
            numFactors += 1

        i += 1

    print("num := ", number, "     numFactors := ", numFactors)    
    return numFactors

# end getNumFactors

def main():
    currentTriNum = 0
    currentNum    = 1 # Start with 1
    numFactors    = 0
    
    while numFactors <= 500:
        currentTriNum += currentNum
        currentNum += 1
        #print(currentTriNum, ", ", currentNum)
        numFactors = getNumFactors(currentTriNum)
    else:
        print("currentTriNum := ", currentTriNum)

# end main

if __name__ == "__main__":
    main()
