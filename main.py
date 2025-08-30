import math

# s = (lambda a, b : a + b)(234, 4324)
# print(s)

s = lambda a, func: a + func(a)

print(s(12, lambda a: int(math.pow(a, 2))))
