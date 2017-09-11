# How to argue with functions

In this section we will look at how to write functions and call them. There are two types of arguments for functions
   1. Positional Arguments
   2. Keyword Arguments

## Positional Arguments
For example for the given function
```python
def addressbook(firstname, lastname, age, address=''):
    print(f'Name: {firstname} {lastname} \nAge: {age} \naddress: {address}')
```

if we pass in `addressbook('Jason', 'Bourne', 40, 'unknown')`
then all the arguments are positional arguments. Because values are automatically assigned to variables at defined at that position.

## Keyword Arguments, a better way to call functions

Python allows caller to call a function by passing parameters with `parameter_name=value` syntax. This is called keyword argument syntax

We can call the above function by keyword argument syntax.
```python
addressbook(lastname='bourne',
            firstname='jason',
            address='unknown',
            age=40)
```

Calling a function with keyword arguments is a better approach because it improves code readibility. With keyword argument syntax you can pass parameters in any order.

## Forcing keyword arguments
You can also force callers of your function to use keyword arguments rather than using positional parameters. This is achieved by placing `*` in the function definition from where the keyword arguments should start. `*` can be at any position. In the below example it is at second position

```python runnable
def addressbook(firstname,*, lastname, age, address=''):
    print(f'Name: {firstname} {lastname} \nAge: {age} \naddress: {address}')

addressbook('jason', age=40, address='unknown', lastname='bourne')

addressbook('jason', 'bourne', 40, 'unknown') # This will throw error.
```

## Unknown number of arguments

Sometimes you need to pass unknown number of arguments to functions. They could be plain arguments or keyword arguments.

All non keyword argments become a tuple. In below example `phonenumber` is a tuple contains all the phone numbers. Remember the syntax the function declaration should have `*phonenumber`. Default naming convention is `*args`

All keyword arguments become a dictionary. In below example `info` is a dict.
Remember the syntax the function declaration should have `**info`. Default naming convention is `**kwargs`

```
def addressbook(name, *phonenumber, **info):
    print(f'Name: {name}')
    for idx, elem in enumerate(phonenumber):
        print(f'phone {idx}: {elem}')

    for key, value in info.items():
        print(f'{key}: {value}')


addressbook('Jason Bourne',
            '11111111',
            '22222222',
            address='unknown')

```
