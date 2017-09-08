# Introspection
Ability to look at the type of the object at runtime is one of powerful features of python.
You can look at the type, function signature, code and even disassembled bytecode at runtime.

## Handling type at runtime
We can at runtime find the type of the object and handle actions accordingly.

```python runnable
import types

def square(x):
    if (type(x) != int) and (type(x) != float):
        print('Type mismatch. the argument has to be int or float')
    else:
        return x*x
```

What if you want to find the type of the inherited object. using `type(something)` will not accomplish to check for parent class but `isinstance(something, parentclass)` will achieve it
```python runnable
class A:
    pass

class B(A):
    pass

instance_b = B()

print(f'Is instance_b is type of B = {type(instance_b) == B}') # True
print(f'Is instance_b is type of A = {type(instance_b) == A}') # False

print(f'Is instance_b is type of B = {isinstance(instance_b, B)}') # True
print(f'Is instance_b is type of A = {isinstance(instance_b, A)}') # True

```

Using `isinstance` function we can create other checks for function, module, class etc can be implemented.
Though they are already implemented in `inspect` module

```python runnable
def isFunction(x):
    return isinstance(x, types.FunctionType)
```

The above code is exactly how `isfunction` function in inspect module is implemented.

## Inspecting the Function Signature
You can inspect the function signature using the `inspect` module. you can use `__annotations__` attribute to get the annotations of a function.
```python runnable
import types
import inspect


def square(x: int) -> int:
    assert(type(x) == int)
    return x*x


sig = inspect.signature(square)
print(sig.parameters)
print(square.__annotations__)
```

### Example: Using Introspection for Validating Parameters

Below is an example where we use inspection to write a Decorator to validate if the passed parameters are of correct type.


@[Function Introspection]({"stubs": ["introspection_validate.py"], "command": "python3 introspection_validate.py"})
