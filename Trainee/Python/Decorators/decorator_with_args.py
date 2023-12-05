def my_decorator(input_arg):

    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f'{input_arg}\n{result}\n{input_arg}'
        return wrapper

    return the_real_decorator


@my_decorator('----------')
def my_decorater_function(input):
    return input


print(my_decorater_function('Hello World'))
