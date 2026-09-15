from math import sqrt
num = 70
result = []

for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        result = []
num = 50
for i in range(1, num // 2):
    if num % i == 0:
        result.append(i)
    if num //i != i:
        result.append(num // i)
        result.sort()
print(result)