# Slots for scaling
Python stores all the instant attributes of a class in dict. This is useful to add more run time attributes. However if we create thousands of such instances the impact of it on RAM is very high.

If we know that there are no such instance attributes at runtime then we can create millions of such objects without much impact on RAM. This can be achived by using `__slots__`. `__slots__` tells python not to use dict but allocate fixed memory for set of attributes.

@[Slots]({"stubs": ["slots.py"], "command": "python3 slots.py"})
