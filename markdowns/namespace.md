# Namespace
In python there are three different namespace
1. global
2. local
3. builtin

Rougly namespace in python in a dictionary containing bunch of variables. Tricky bit is the scope of the namespace and where are those visible. This is defined by the scope.
Variable is first searched in the inner most scope and moves to global and finally builtin.

To get module's dictionary use `globals()`. If you are running a standalone python file then the module will be `__main__`

```python
module_dict = globals()
```

@[Global Namespace]({"stubs": ["namespace_global.py"], "command": "python3 namespace_global.py"})
