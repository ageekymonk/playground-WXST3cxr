# Dynamic Attributes

## Handling Unknown Instance attributes
You can dynamically respond to get instance attributes. python provides special method called `__getattr__` which can be implemented to respond to get attributes

In the below example we are subclassing dict so that we can get elements as class attributes rather than with element accessor.
@[Dynamic get attributes]({"stubs": ["dynamic_getattr.py"], "command": "python3 dynamic_getattr.py"})

### Setting unknown instance attributes
Extending the above example we can also set attributes using `__setattr__`. `__setattr__` gets called when there is no such attribute to set. We can implement it for our purpose.

@[Dynamic set attributes]({"stubs": ["dynamic_setattr.py"], "command": "python3 dynamic_setattr.py"})
