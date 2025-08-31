import math

def square(function):
    def wrapper(a, b):
        _sum = function(a, b)
        return math.pow(_sum, 2)

    return wrapper

@square
def summa(a, b):
    return a + b

print(summa(2, 3))
