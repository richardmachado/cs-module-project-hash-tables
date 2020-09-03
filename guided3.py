# The General Problem Hash Tables Solve

#? Good at o(1) lookup

#? if we have somehting to look up quickly we can use a hash table
#? espcially true if it isn't normally quick to look up

#? Can we do this expensive, time-consuming process one time, save the result,  and then look it up


#! Example

#? Identify the time consuming process

# Linear search
    # if n < 10:
        # who cares what you search for
        

    # n < 100000000000000000
        # now we might care

    # if n < 100000000000000000000000000000000000
        # now we really need to care
        
#Bonus sort

#quicker sort
    # quick sort when n > 32
    # else insertion sort

#added Memoization
    
cache = {}

def fib(n):
    if n <= 1:
        return n
    
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]
    
for i in range(10):
    print(f"{i}: {fib(i)}")
    
   