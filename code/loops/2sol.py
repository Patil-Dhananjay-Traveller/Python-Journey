#Sum of Even Two numbers
#pro: Calculate the Sum of even numbers up to a given numbers n.

n = 10
sum_even = 0

for i in range(1, n+1):
    if i %2 == 0:
        sum_even +=i
print('positive nuber: ',sum_even)