import time
import functools

# This is the bsic structure of any decorator
# Decorators use Closures as shown below
# You can add any functionality in the wrapper() function
# When you use a Decorator the wrapper wrappes the orignal function
def decorator_template(func):
    def wrapper(*args, **kwargs): #wrapper takes the args/kwargs of func and passes them to it
        result = func(*args, **kwargs)
        return result
    return wrapper

# ******************** Creating custom Decorators *********************
# Decorator for noting time taken for execution
def execution_time(func):
    @functools.wraps(func) #This line is explained at the end of file
    def wrapper(*args, **kwargs):
        func_name = func.__name__ #get the name of orignal func
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"The function: {func_name} ran for: {round(end_time - start_time, 3)}s")
        return result
    return wrapper

# Decorator to get the name and arguments of a function for debugging
def debug(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        arg_value = ", ".join(map(str, args))
        kwargs_value = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"The function named: '{func_name}' was called") 
        print(f"Containing args: {arg_value}") 
        print(f"kwargs: {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def cache_output(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        print(f"cache_1st: {cache}")
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"cache_2nd: {cache}")
        return result
    return wrapper


# ************************ Usage of Decorators ***************************
@execution_time
def timetTakingFunction(a,b):
    time.sleep(4)
    return f"{a} + {b} = {a+b}"
# timetTakingFunction(10,1)

@debug
def a_function(*args, **kwargs):
    total = sum(args)
    kwargs_list = list(item for item in kwargs.items())
    print(f"Sum of all the numbers: {total}, kwargs: {kwargs_list}")
# a_function(1,2,3,4,5,6,7,8,9,10, name = "Shahram", level = 20)

@cache_output
def timetTakingFunction2(a,b):
    time.sleep(4)
    return f"{a} + {b} = {a+b}"
timetTakingFunction2(5,5)
timetTakingFunction2(5,5)

# Stacked decorators
@execution_time
@cache_output
def timetTakingFunction3(a,b):
    time.sleep(4)
    return f"{a} + {b} = {a+b}"
# timetTakingFunction3(3,5)
# timetTakingFunction3(3,5)



# functools.wraps(func) Explaination:
# When you write a decorator, it typically wraps a function with 
# another function (usually called wrapper). But without functools.wraps,
# the original function’s metadata—like its name, docstring, annotations, 
# and even its identity—gets lost. That’s where functools.wraps(func) 
# comes in. It copies all the important metadata from func to wrapper, 
# so your decorated function still looks and behaves like the original.

