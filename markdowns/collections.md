# Collections module

## Better way to count elements

Collections module provide a Counter class which can used to count elements in a list. It also provides utility functions like `most_common` for getting most common elements in the list.

@[counter class]({"stubs": ["collections_counter.py"], "command": "python3 collections_counter.py"})

## defaultdict

defaultdict behaves like normal dict with one key difference. It has a factory function that takes no arguments which provides values for non existent key

@[defaultdict class]({"stubs": ["collections_defaultdict.py"], "command": "python3 collections_defaultdict.py"})

### Example
One most popular example is one liner tree function. You can create a nested dict without even initialising its parents.

@[defaultdict class]({"stubs": ["collections_defaultdict_tree.py"], "command": "python3 collections_defaultdict_tree.py"})
