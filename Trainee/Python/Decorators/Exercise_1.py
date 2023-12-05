# -*- coding: utf-8 -*-
def a_function():
    """Обычная фукнция"""
    return "1+1"


def another_function(func):
    """
    Функция которая принимает другую функцию
    """

    def other_func():
        val = "Результат от %s это %s" % (func(), eval(func()))
        return val

    return other_func


if __name__ == "__main__":
    value = a_function()
    print(value)
    decorator = another_function(a_function)
    print(decorator())
