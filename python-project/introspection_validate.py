import inspect
from functools import wraps


def Validate(f):
    sig = inspect.signature(f)

    @wraps(f)
    def _wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        for name, val in bound_args.arguments.items():
            if name in f.__annotations__:
                if not isinstance(val, f.__annotations__[name]):
                    assert False, f'{val} should be of type {f.__annotations__[name]}'
        return f(*args, **kwargs)
    return _wrapper


@Validate
def square(x: int) -> int:
    return x*x


@Validate
def uppercase(x: str) -> str:
    return x.upper()


print(square(10))
print(uppercase("hello"))
print(uppercase(10))
print(square(1.11))
