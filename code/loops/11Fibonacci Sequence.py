'''def fib(n):

    a = 0
    b = 1

    for i in range (n):
        print(a)
        c = a+b 
        a = b
        b = c
fib(10)'''

def feb(n):

    a = 0
    b = 1

    print (a)
    print (b)

    for i in range (2,n):

        c = a + b
        a = b
        b = c
        print(c) 

feb(10)