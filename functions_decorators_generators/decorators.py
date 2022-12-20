from datetime import datetime
from functools import singledispatch


def print_time_stats(func):
    def wrapper_func(*args):
        start_at = datetime.now()
        print(f"Start execution of {func.__name__} at {start_at}")
        func(*args)
        end_at = datetime.now()
        print(f"Finished execution of {func.__name__} at {end_at}")
        print(f"Execution of {func.__name__} took {(end_at - start_at).total_seconds()}")
    return wrapper_func


def bold_decorator(func):
    def wrapper_func(*args):
        func_result = func(*args)
        return f"<b>{func_result}</b>"
    return wrapper_func


def pre_tag_decorator(func):
    def wrapper_func(*args):
        func_result = func(*args)
        return f"<pre>{func_result}</pre>"
    return wrapper_func


@bold_decorator
@pre_tag_decorator
def capitalize_name(name: str):
    """print_name decorated function docstring"""
    return name.upper()


print(capitalize_name("test"))


@singledispatch
def printer(value):
    print(f"Other: {value}")


@printer.register(str)
def str_printer(value):
    print("Print string: ", value)


@printer.register(int)
def int_printer(value):
    print("Print integer: ", value)


@printer.register(dict)
def dict_printer(dictionary):
    for value in dictionary.values():
        print("Value of dict item is: ", value)


# printer({"name": "Pesho", "age": "uknown"})

@print_time_stats
def loop_in_a_billion():
    print("Start loop over 1B")
    for _ in range(1_000_000_001):
        continue
    print("End loop over 1B")


loop_in_a_billion()
