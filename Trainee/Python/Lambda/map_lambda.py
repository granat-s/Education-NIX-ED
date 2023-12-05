nums = [1, 2, 3, 4, 5]


def sq(n):
    return n * n


square = list(map(lambda x: x ** x, nums))

print(square)
