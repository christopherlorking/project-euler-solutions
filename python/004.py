'''
https://projecteuler.net/problem=4

Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Status: Complete
'''

# Assumption: numbers will have 6 digits

def getPalindromes(x):
    allPalindromes = []
    # take the number and compare first three digits to last three digits
    # if [0] == [5], [1] == [4], [2] == [3] then palindrome
    for y in range(x):
        l = list(str(y))
        if len(l) == 6:
            if l[0] == l[5] and l[1] == l[4] and l[2] == l[3]:
                allPalindromes.append(y)
    return allPalindromes

def allNumsWithTwoThreeDigitFactors(floor, ceiling):
    l = []
    x = floor
    y = floor
    while x < ceiling:
        while y < ceiling:
            l.append(x * y)
            y = y + 1
        x = x + 1
        y = floor
    return l

palindromes = getPalindromes(999 * 999)
numbers = allNumsWithTwoThreeDigitFactors(100, 999)

set1 = {1}
set2 = {1}
set3 = {1}

set1.update(palindromes)
set2.update(numbers)
set3 = set1 & set2

result = 0
for x in set3:
    if x > result:
        result = x

print(result)