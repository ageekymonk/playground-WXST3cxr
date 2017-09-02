# Namespace
In python there are three different namespace
1. global
2. local
3. builtin

Rougly namespace in python in a dictionary containing bunch of variables. So every object has `__dict__` associated with it.
That contains all the attributes that belong to that object. You can modify them for fun and profit.

Tricky bit is the scope of the namespace and where are those visible. This is defined by the scope.
Variable is first searched in the inner most namespace, and then to enclosing namespace
(for example functions inside functions) and moves to global and finally builtin.

# Global Namespace
To see what to see in modules' namespace, you need to access its `__dict__` which is done by calling `globals()`.
If you are running a standalone python file then the module is called `__main__`

```python
module_dict = globals()
```

@[Global Namespace]({"stubs": ["namespace_global.py"], "command": "python3 namespace_global.py"})

# Builtin Namespace
Python automatically imports all the builtin functions into every modules' namespace without polluting the modules' `__dict__`.
So when you see modules' dictionary you wont see them directly. You can still access them in variety of ways.

In below example we are modifying builtin function.

@[Builtin Namespace]({"stubs": ["namespace_builtin.py"], "command": "python3 namespace_builtin.py"})

`vars()` returns the local namespace. If it is called inside function it returns functions `__dict__`
It also takes an argument which could be any object and returns its `__dict__` object.
