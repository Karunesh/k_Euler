# prob14.py

import time

limit = 1000001
number = 1
count = 0 # number of terms in sequence for a number
numDict = {}

def populateDict(limit):
    for i in range(1, limit):
        numDict[i] = 1
        
def calculateSequenceForNumber(num):
    if numDict[num] != 0:
        val = num
        countForNum = 0
    
        while val != 1:
            countForNum += 1
            if val % 2 == 0:
                val = int(val / 2)
            else:
                val = (val * 3) + 1

                global limit
                if val < limit:
                    numDict[val] = 0
    
        global count
        global number
        if countForNum > count:
            number = num
            count = countForNum

def main():
    start_time = time.time()
    populateDict(limit)

    # only odd numbers, since for example (4 := 7, 22, 11..) will be less than 7
    for i in range(1, limit, 2): 
        calculateSequenceForNumber(i)
    
    print(number, "Count :=", count, ".time taken :=", (time.time() - start_time))

if __name__ == "__main__":
    main()
