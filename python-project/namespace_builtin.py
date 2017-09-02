# Accessing builtin namespace via module's namespace
module_dict = globals()

builtin_dict = module_dict["__builtins__"].__dict__

# you can also access by importing builtins
import builtins as _builtins

# Both of them are same
print(builtin_dict == vars(_builtins))

# Modifying the builtin print function
_print = _builtins.print
_builtins.print = lambda *args, **kwargs: _print('YodaSays: ', *args, **kwargs)

print("Do. Or do not. There is no try")
