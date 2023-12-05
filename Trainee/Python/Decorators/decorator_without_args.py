def my_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'Adding some text in the decorator\n{result}'
    return wrapper


@my_decorator
def my_decorated_function(input):
    return input


print(my_decorated_function('Hello World'))
