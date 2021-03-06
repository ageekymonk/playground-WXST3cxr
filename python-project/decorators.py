def debug_input_output(f):
    def wrapping_function(*args, **kwargs):
        print(f'Input: {args} {kwargs}')
        ret = f(*args, **kwargs)
        print(f'Output: {ret}')
        return ret
    return wrapping_function

@debug_input_output
def addressbook(name, **details):
    """My addressbook"""
    return {'name': name, **details}

addressbook('jason', age=40, address='unknown')
print(addressbook.__name__)
print(addressbook.__doc__)
