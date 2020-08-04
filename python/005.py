# Project Euler
# Problem 5: Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Status: Unfinished

# Initialise result
# Cannot be lower than 2520
result = 0
# div_by_20 = False
limit = 100000

i = 2520
while i < limit:
   # We could save on compute by cherry picking numbers here
   # eg every number is divisible by 1, if a number is divisible by 20 it will be divisible by 2 etc
   for j in range(20):
      

