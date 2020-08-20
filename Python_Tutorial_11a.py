# Decorators


'''calculate time to run the code'''
import time
from functools import wraps

'''decorative function'''
def calculate_time(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        print(f"Executing {any_func.__name__} function")
        t1 = time.time()
        returned_value = any_func(*args, **kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f"this function took {total_time} sec to execute")
        return returned_value
    return wrapper


@calculate_time
def time_find(n):
    return [i**2 for i in range(1, n+1)]

'''only calculating time, not printing the list'''
time_find(10000)




