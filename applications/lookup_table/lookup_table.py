"""
There's no test file for this. It's counting to 50,000, so if it
finishes before you give up, then you're golden.
"""

# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    #cache values
    #build libraries based on some random numbers
    key = (x, y)
    if key not in cache:
        cache[key] = math.pow(key[0], key[1])
        cache[key] = math.factorial(cache[key])
        cache[key] //= (x + y)
        cache[key] %= 982451653
        
    return key

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
