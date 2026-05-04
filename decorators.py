import functools


def log_call(func):
    # functools.wraps keeps the original function's name and info intact
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Print the function name before it runs
        print(f"[LOG] '{func.__name__}' was called")
        # Print positional arguments (like numbers, strings passed directly)
        print(f"      positional args: {args}")
        # Print keyword arguments (like name="Hasan")
        print(f"      keyword args: {kwargs}")
        # Actually run the original function and return its result
        result = func(*args, **kwargs)
        print(f"      returned: {result}")
        return result
    return wrapper


# Now let's use the decorator on two example functions

@log_call
def add(a, b):
    # Simple addition — nothing special here
    return a + b

@log_call
def greet(name, greeting="Hello"):
    # Returns a greeting string
    return f"{greeting}, {name}!"



add(10, 5)
add(5,5)
greet("Hasan", greeting="Hey")