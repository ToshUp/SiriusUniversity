import math
import sys

def prime_check(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i <= math.sqrt(n) + 1:
        if n%i != 0:
            i = i + 2
        else:
            return False
    return True

def prime_sum(n):
    if n == 2:
        return n
    i = 3
    s = 0
    while i <= n:
        if prime_check(i) == True:
            s = s + i
        i = i + 2
    return s + 2

x = int(sys.argv[1])
print(prime_sum(x))