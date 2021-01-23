# //////////////////// FIBONACCI WITH DYNAMIC PROGRAMMING CACHE ///////////

def fib_Dynamic(n):
    global cache
    cache={}
    if n in cache:
        return cache[n]
    else:
        if(n<2):
            return n
        cache[n]=fib_Dynamic(n-1)+fib_Dynamic(n-2)
        return cache[n]
print(fib_Dynamic(30))
print(cache)



# //////////////// FACTORIAL + FIBONACCI ITERATIVE AND RECCURSIVE BELOW! 
def factorial(num):
    if num == 0:
        return 1
    return num* factorial(num-1)

def factorialITERATIVE(num):
    result = 1
    for num in range(1,num+1):
        result = result * num
    return result
    
# print(factorial(12))
# print(factorialITERATIVE(12))
# 10! = 10x9x8x7x6x5x4x3x2x1


def fib(num):
    arr= [0,1]
    for n in range(2,num+1):
        arr.append(arr[n-1]+arr[n-2])
    return arr[num]

def fib_r(num):
    if num < 2:
        return num
    return fib_r(num-1)+fib_r(num-2)

# print(fib_r(12))
    
def reverse_string(string):
    string = list(string)
    size=len(string)
    for i in range(size):
        if i < size/2:
            string[i],string[size-i-1] = string[size-i-1],string[i]
    return ''.join(string)
    

    
# print(reverse_string('1234567890'))
# print(fib(9))



    
