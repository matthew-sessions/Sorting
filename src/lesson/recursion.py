def recurse(num):
    print(num)
    if num <= 0:
        #print(' ')
        return(num)

    #print(num)
    num -= 1
    recurse(num)
    recurse(num)



def fib(n):
    if n == 0:
        return(0)
    elif n <= 0:
        print('no')
    elif n == 1:
        return(1)
    else:
        print(fib(n-1) + fib(n-2))
        #return(fib(n-1) + fib(n-2))
    
print(fib(8))
