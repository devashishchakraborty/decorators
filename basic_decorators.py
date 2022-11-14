import time

def execute_twice_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper

def decorator(func):
    def wrapper():
        print("decoration begins ")
        func()
        print("decoration ends")
    return wrapper

def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time()-start_time
        print(f"duration {duration}")
    return wrapper

@execute_twice_decorator
@decorator
@duration_decorator
def func():
    print("Function")
    time.sleep(1)

func()