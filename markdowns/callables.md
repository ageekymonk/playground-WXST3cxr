# Callables
At first glance we think functions and methods are the only callables. But in python any object can be callable provided its class
has implemented `__call__` method. This means objects can also act as functions.

You can check if an object is callable using `callable` builtin function

@[Callables]({"stubs": ["callables.py"], "command": "python3 callables.py"})
