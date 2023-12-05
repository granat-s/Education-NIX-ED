from functools import reduce


seq = [2, 3, 4, 5, 6]

multiply = reduce(lambda a, b: a * b, seq)
print(multiply)
