n = 8891
sum = 0
order = len(str(n))
copy_n = n
while(n>0):
    digit = n%10
    sum += digit **order
    n = n // 10
if (sum == copy_n):
    print(f'{n} is armstrong number')
else:
    print(f'{n} is not armstrong number')
