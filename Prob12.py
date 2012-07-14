# prob12.py
import math

def getNumFactors(number):
    """
    Returns number of natural numbers that exactly divide number,
    including 1 and number itself.
    -- Any number has factors of the form num1 * num2, where
       num1 < number's square root and num2 > number's square root.
       This means that finding number of factors upto the square
       root and multiplying by 2 will give us the number of factors.
    -- EDGE CASE: If the number is a perfect square, we should be
       counting its square root only once and not twice.
    """

    numFactors = 2 # Already accounting for 1 and number itself.

    if math.sqrt(number) == int(math.sqrt(number)): # number is a perfect square.
        numFactors += 1

    for i in range(2, int(math.sqrt(number))):
        if (number % i) == 0:
            numFactors += 2
        i += 1

    return numFactors

# end getNumFactors

def main():
    currentTriNum = 0
    currentNum    = 1 # Start with 1
    numFactors    = 0
    
    while numFactors <= 500:
        currentTriNum += currentNum
        currentNum += 1
        numFactors = getNumFactors(currentTriNum)
    else:
        print("currentTriNum := ", currentTriNum)

# end main

if __name__ == "__main__":
    main()
