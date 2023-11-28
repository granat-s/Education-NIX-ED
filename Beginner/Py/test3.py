# Напишите функцию, которая будет преобразовывать цену к формату, отображающему
#   до двух знаков после точки, например:
#
# 22.32131 -> 22.32
# 58.60125 -> 58.6
# 34.0 -> 34


def price_strip(price):
    return float("{:.2f}".format(price))


print(price_strip(22.32131))
print(price_strip(58.60125))
print(price_strip(34.0))
