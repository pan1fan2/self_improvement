# def start_end_decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print('End')
#     return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")

#print_name = start_end_decorator(print_name)
#print_name()

# import functools
# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('Start')
#         result = func(*args,**kwargs)
#         print('End')
#         return result
#     return wrapper

# @start_end_decorator
# def add5(x):
#     return x+5

# result = add5(10)
# print(result)

# print(add5.__name__) # need to import functools and add @funtools.wrap above def wrap

import functools
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def great(name):
#     print(f'Hello {name}')

# great('Alex')

class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwds):
        #print('Hi There')
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwds)
        
cc = CountCalls(None)
#cc()

@CountCalls
def say_hello():
    print('Hello')

say_hello()