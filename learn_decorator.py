
from typing import Any
from functools import wraps


def decorator_function(func):
    @wraps(func)
    def wrapper_func(*args,** kwargs):

        print(f'function decorators excute before {func.__name__}')
        return func(*args,** kwargs)

    return wrapper_func


def logger_file(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        print(f"logger file  excute before {original_func.__name__}")
        return original_func(*args, **kwargs)

    return wrapper

def my_timer(original_func):
    import time
    @wraps(original_func)
    def wrapper( *args, **kwargs):
        t1= time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_func.__name__} run {t2}")
        return result
    return wrapper

class decorator_class():
    def __init__(self,original_func) -> None:
        self.original_func = original_func
    
    # @wraps(self.original_func)
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'class  decorators excute before {self.original_func.__name__}')
        return self.original_func(*args, **kwds)

@decorator_function
@logger_file
@my_timer
def display(name: str, age: int):
    import time
    time.sleep(1)
    print(f"{name} is {age} years old")

display("lily",22)
# @decorator_function
# def display_exe(*args,** kwargs):
#     print(f"parameters of display_exs ({args} {kwargs})")

# decorators = decorator_function(print_random)

# decorators()


# display()
# display_exe(1,2,hello="world")