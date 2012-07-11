# prob12.py

def getNumFactors(number):
    """
    Returns number of natural numbers that exactly divide number,
    including 1 and number itself.
    """

    numFactors = 2 # Already accounting for 1 and number itself.

    i = 2
    while i < number:
        if (number % i) == 0:
            numFactors += 1

        i += 1
        
    return numFactors

def main():
    currentTriNum = 0
    currentNum    = 1 # Start with 1
    numFactors    = 0
    
    while numFactors <= 500:
        currentTriNum += currentNum
        currentNum += 1
        print(currentTriNum, ", ", currentNum)
        numFactors = getNumFactors(currentTriNum)
    else:
        print("currentTriNum := ", currentTriNum)
  
# end main

if __name__ == "__main__":
    main()
