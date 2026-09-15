#Factrial Calculator
#Pro: Computer the factorial of a number using a while loop 
number = 5
factor = 1

while number > 0:
    #factor = factor * number
    #number = number -1

    factor *= number
    number -= 1

    print("Factor is:",factor)