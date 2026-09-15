#for besic calculations
'''
def add(a,b):
    return a+b
print(add(8,4))'''

'''
def add(*args):
    return (args)

print(add(4,1,3,4,9,5,7,1,6))'''

'''def add(*args):
    print(args)

    total = 0
    for i in args:
        total += i

    print(total)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)'''


def my_detail(*args):
    print(type(args))
    print(args)
my_detail("Dhananjay Patil",30000,'BCA')