# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#   solution 1
# def calc():
#     i = 0
#     result = 0
#     while i < 1000:
#         if (i % 3 == 0 or i % 5 == 0):
#             result = result + i
#         i = i + 1
#     return result

#   solution 2
def calc():
    result = 0
    for i in range(1000):
        if (i % 3 == 0 or i % 5 == 0):
            result = result + i
    return result