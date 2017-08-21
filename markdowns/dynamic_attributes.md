# Dynamic Attributes

## Handling Unknown Instance attributes
You can dynamically respond to get instance attributes. python provides special method called `__getattr__` which can be implemented to respond to get attributes

In the below example we are subclassing dict so that we can get elements as class attributes rather than with element accessor.
@[Dynamic get attributes]({"stubs": ["dynamic_getattr.py"], "command": "python3 dynamic_getattr.py"})
