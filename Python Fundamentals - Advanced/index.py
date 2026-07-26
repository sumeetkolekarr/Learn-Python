# =============================================================
# Python Fundamentals - Advanced
# Why this folder exists: NumPy/Pandas/sklearn code you'll read
# and write for AI/DS is full of *args/**kwargs, decorators,
# generators and type hints. This folder fills the gaps between
# "finished a Python course" and "can read real DS codebases".
# =============================================================

# -------------------------------------------------------------
# 1) *args and **kwargs
# You'll see this in almost every library function signature,
# e.g. pd.read_csv(*args, **kwargs)
# -------------------------------------------------------------
def describe(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)

describe(1, 2, 3, name="Sumeet", role="learner")


# -------------------------------------------------------------
# 2) Generators (yield)
# Useful for processing large datasets without loading
# everything into memory at once.
# -------------------------------------------------------------
def counter(limit):
    n = 0
    while n < limit:
        yield n
        n += 1

for value in counter(5):
    print(value)

# TODO Q1: Write a generator `even_numbers(limit)` that yields
# only even numbers from 0 up to (not including) limit.


# -------------------------------------------------------------
# 3) Context managers (with)
# You already used this for file handling. Here it's a
# reusable pattern beyond files (timers, DB/GPU sessions).
# -------------------------------------------------------------
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        print(f"Elapsed: {time.time() - self.start:.4f}s")

with Timer():
    total = sum(range(1_000_000))


# -------------------------------------------------------------
# 4) Decorators
# You'll see @staticmethod, @property today, and later things
# like @tf.function. Understanding the pattern here removes
# the "magic".
# -------------------------------------------------------------
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 4))

# TODO Q2: Write a decorator `timer(func)` that prints how long
# `func` took to run (reuse the idea from the Timer class above).


# -------------------------------------------------------------
# 5) functools basics
# -------------------------------------------------------------
from functools import reduce, partial, lru_cache

# reduce: collapse a list into a single value
product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print("product:", product)

# partial: pre-fill some arguments of a function
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print("square(5):", square(5))

# lru_cache: memoize expensive/recursive calls
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("fib(30):", fib(30))


# -------------------------------------------------------------
# 6) Type hints
# Not enforced at runtime, but library docs and IDE autocomplete
# rely on them heavily - worth reading and writing comfortably.
# -------------------------------------------------------------
def greet(name: str, times: int = 1) -> str:
    return (name + " ") * times

print(greet("Sumeet", 2))

# TODO Q3: Add type hints to the `describe` function above.
