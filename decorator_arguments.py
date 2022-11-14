def decorator(func):
    def wrapper(wrapper_parameter):
        print('decoration begins')
        func(wrapper_parameter)
        print('decoration ends')
    return wrapper

@decorator
def func(func_parameter):
    print(func_parameter)

func('hello')