# Multiplication Table Printer
#Pro:Print the multication table for a given number up to 10,but skip the fifth iteration.
n = 69
for i in range(1,11):
    if i == 5:
        continue
    print(n,'x',i,'=',n*i)