from functools import reduce

num = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, num))
print("Using map squres:", squares)
evens = list(filter(lambda x: x % 2 == 0, num))
print("Using filter even:", evens)
total = reduce(lambda x, y: x + y, num)
print("Using reduce total:", total)