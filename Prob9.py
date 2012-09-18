# Prob9.py

from math import *

total = 1000

def main():
    for i in range(1, total):
        print(i)
        a = i
        for b in range(a, total):
            c = getHypotenuse(a, b)
            if a + b + c == total:
                print("    ", a, ", ", b, ", ", c)
                print("    ", a * b * c)
                break

def getHypotenuse(a, b):
    return sqrt(a * a + b * b)

if __name__ == "__main__":
    main()


