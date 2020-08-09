'''
https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Status: Complete
Performance: Okay, ~5-7s
   - Original version was ~90s
   - Down to ~30s by using nums[...] instead of range(1, 21) for j.
   - Down to current performance by breaking out of for loop if any value in nums is not a multiple, otherwise checks the rest of the numbers for no reason.
   
'''

def compute():
   # Boolean to hold whether a given number is divisible by all numbers 1-20.
   div_by_20 = False

   # List of all relevant numbers to check against numbers.
   # No need to include 1, 2, 3, 4, 5, 6, 7, 8, 10 - eg if a number is divisible by 16, it is also divisible by 8.
   # No need to include 20 as starting on a number divisible by 20 and incrementing by 20 each time - only testing against numbers divisible by 20.
   nums = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19]

   # 2520 is divisible by 20, so using this as starting point and adding 20 each iteration.
   number = 2520 

   while div_by_20 == False:
      div_by_20 = True
      for multiple in nums:
         if number % multiple != 0: # If the multiple being tested is indeed a multiple.
            div_by_20 = False
            break
      if div_by_20 == True:
         break
      number += 20

   print('The following number is divisible by all numbers 1-20: ' + str(number))

if __name__ == "__main__":
   compute()