# Validate Input
# Pro: Keep asking the user for input until they entera number between 1 and 10


while True:
 number  = int(input("Enter the number: "))
 if 1 <=  number <= 10:
  print('Thanks') 
 else:
  print("Incorrect number,try again")