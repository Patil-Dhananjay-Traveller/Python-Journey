#Counting Positive Number
# pro = Given a list ofnumbers, count how many are poositive
#numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5]

numbers = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]

total_positive_numbers = 0
for num in numbers:
    if num >0:
        total_positive_numbers +=1
        print("P numbers: ",total_positive_numbers)
