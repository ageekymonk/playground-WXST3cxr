# Decorators

Decorator is a syntactic sugar for higher order functions. Higher order functions take a function as input and return another function. It extends the functionality of the input function for fun and profit

For programmers print is best tool for debugging. In the example below the decorator is used to print the input and output of a function. Just adding the decorator to functions will do the job rather than going inside the function and adding a print and it is reusable.

@[Decorators]({"stubs": ["decorators.py"], "command": "python3 decorators.py"})

This implementataion of decorator has two problems.
1. Name of the function is wrong
2. Docstring is wrong.


## Better Decorator using functools
Functools module provide necessary wrapper to write your own custom decorator. `@wraps` takes care of writing all the boiler plate code
for retaining the name of the function and docstring. This is an improvement on our earlier implementataion.

@[Custom Decorator]({"stubs": ["functools_custom_decorators.py"], "command": "python3 functools_custom_decorator.py"})
