# How to argue with functions

   In this section we will look at how to write functions and call them

## Multiple Arguments, a better way to call it

Python allows caller to call a function by passing parameters with `parameter_name=value` syntax. This is called keyword argument syntax

Calling a function with keyword arguments is a better approach because it improves code readibility. With keyword argument syntax you can pass parameters in any order.

@[Better function call]({"stubs": ["functions.py"], "command": "python3 functions.py"})

## Unknown number of arguments

Sometimes you need to pass unknown number of arguments to functions. They could be plain arguments or keyword arguments.

All non keyword argments become a tuple. In below example `phonenumber` is a tuple contains all the phone numbers. Remember the syntax the function definition should have `*phonenumber`

All keyword arguments become a dictionary. In below example `info` is a dict.
Remember the syntax the function definition should have `**info`

@[Unknown number of arguments]({"stubs": ["functions_varargs.py"], "command": "python3 functions_varargs.py"})
