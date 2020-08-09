'''
https://projecteuler.net/problem=4

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Status: Complete
Performance: Abysmal, 65-75s to run.
'''

result = 0
div_by_20 = False

i = 2520
while div_by_20 == False:
   div_by_20 = True
   # If a number is divisible by 20 it will be divisible by 2.
   for j in range(4, 21): # Python ranges are base index 0, starting at j = 3
      if i % j != 0:
         div_by_20 = False
      j += 1
   if div_by_20 == True:
      result = i
      break
   i += 20

print('The following number is divisible by all numbers 1-20: ' + str(result))