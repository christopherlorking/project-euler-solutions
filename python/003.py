'''
https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Status: Complete
'''

# Returns true if x is a prime number
def isPrime(x):
    # throw out any even numbers
    if x % 2 == 0:
        return False
    i = int(round(x/3)+1) # Highest prime factor of a number cannot be higher than 1/3 of that number, so start with x / 3.
    while i > 2:
        if x % i == 0:
            return False
        i = i - 1
    return True

# Returns highest prime factor of 600851475143 under a limit
def calc(limit):
    i = limit
    while limit > 0:
        if 600851475143 % i == 0:
            if isPrime(i):
                return i
        i = i - 1
    return -1

print(calc(100000))