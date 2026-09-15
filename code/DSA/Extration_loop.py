"""n = 9292929292
num = n
while num > 0:
    last_degit = num % 10
    print(last_degit)
    num = num // 10 
"""


# DSA in Python Course - Count the Number of Digits in an Integer - Part 6
"""n = int(input('Enter number: '))
num = n
count = 0

while num > 0:
    count += 1
    num = num // 10

print(count)"""

import math

def countDigits(num):
    return int(math.log10(num) + 1)

print(countDigits(563476))