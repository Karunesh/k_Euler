# prob14.py

number = 1
count = 0 # terms in sequence for this number

# This will contain all powers of 2 upto 5 million (I don't think we'll need more
# than 3 million, but still). In case that happens, there won't be any problem
# since that number (being even) will be divided by 2 and we'll go on from there.
powersOf2 = []

def populatePowersOf2():
    num = 1
    while num < 5000000:
        powersOf2.append(num)
        num *= 2
    print(powersOf2)

def calculateSequenceForNumber(num):
    print("In calculateseq, for num :=", num)
    val = num
    countForNum = 0
    while val not in powersOf2:
        countForNum += 1
        if val % 2 == 0:
            val = int(val / 2)
        else:
            val = int((val * 3) + 1)
        print(num, val)
    else:
        countForNum += powersOf2.index(val) + 1


    global count
    if countForNum > count:
        number = num
        count = countForNum
        
def main():
    populatePowersOf2()

    for i in range(1, 1000001):
        calculateSequenceForNumber(i)

    print(number, "Count :=", count)

if __name__ == "__main__":
    main()
