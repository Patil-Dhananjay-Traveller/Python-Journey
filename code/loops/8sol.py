#Prime Numbers Checker
#Pro: Check if a number is prime #

number = int(input('Ente the number: '))

for i in range(2, number):
 if number % i == 0:
  print("Not prime number")
 else:
  print('number is prime')