# Prob10.py

from math import *

limit = 2000000

def isPrime(number):
    # I should probably use a list here.
    if number == 2: return True
    elif number % 2 == 0: return False
    elif number == 3: return True
    elif number == 5: return True
    elif number == 7: return True
    elif number == 9: return False
    else:
        rootOfNumber = sqrt(number)
        tag = 3
        while tag < rootOfNumber:
            if number % tag != 0:
                tag += 2
            else:
                break
        if tag >= rootOfNumber:
            return True
        else:
            return False

sum = 2 # 2 is an even prime, something we are not iterating for
for i in range(3, limit, 2):
    if isPrime(i) == 1:
        sum += i

print(sum)
print('done...')
