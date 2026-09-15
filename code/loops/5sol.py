# Find the first non-repeated character
# Pro: Given a string, Find non-repated character

name = "Dhananjay Patil"

for char in name:
    if name.count(char) == 1:
        print("Count char:",char)