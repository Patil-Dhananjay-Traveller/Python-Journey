#List uniqueness Checker
#Pro: Check if all elemets in a list are unique. if a duplicte is forund, exit the loop and prime the puplict
# items = ["apple","mango","orange","watermellon","mango","strobarry","lichy"]

items = ["apple","mango","orange","watermellon","mango","strobarry","lichy"]

uneq = set()

for items in items:
    if items in uneq:
        print('Dupicate',items)
    else:
        uneq.add(items)