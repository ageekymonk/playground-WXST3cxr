# Multiple Inheritance

## Multiple Inheritance with two non overlapping parents
Multiple Inheritance is easy if we inherit from two parent class, each without any overlapping methods

```python runnable
class Father:
    print("In Father")
    def funcA(self):
        print('In funcA')

class Mother:
    print("In Mother")

    def funcB(self):
        print('In funcB')


class Son(Father, Mother):
    print("I am son")


x = Son()
x.funcA()
x.funcB()

```

## Multiple Inheritance with overlapping methods
If there are overlapping methods, the method of first parent class will be called. In the below example, since we added the class `Father` as the first argument in `class Son(Father, Mother)`, the method in class `Father` will be called. If it had been `class Son(Mother, Father)`  then method in class `Mother` will be called.

```python runnable

class Father:
    print("In Father")
    def funcA(self):
        print('In Father funcA')

class Mother:
    print("In Mother")

    def funcA(self):
        print('In Mother funcA')

class Son(Father, Mother):
    print("I am son")

x = Son()
x.funcA()

```

## Multiple Inheritance with Diamond Structure
To solve this python computes `mro`, method resolution order for a class. This can be found by `__mro__`. This gives a list of parent classes linearized. So python checks for next in line based on the `__mro__`.

`super` follows the `mro` as well. It does not call the parent of a class. It calls next in line based mro.

The algorithm used for computing the mro is C3 Linearization Algorithm. More details on the algorithm in [mro](https://www.python.org/download/releases/2.3/mro/)

```python runnable
class Adam:
    pass

class Eve:
    pass

class PaternalGrandFather(Adam, Eve):
    def funcA(self):
        print('In Paternal Grandfather funcA')

class PaternalGrandMother(Adam, Eve):
    pass

class MaternalGrandFather(Adam, Eve):
    def funcA(self):
        print('In Maternal GrandFather funcA')

class MaternalGrandMother(Adam, Eve):
    pass

class Father(PaternalGrandFather, PaternalGrandMother):
    pass

class Mother(MaternalGrandFather, MaternalGrandMother):
    def funcA(self):
        print('In Mother funcA')

class Son(Father, Mother):
    pass

print(Son.__mro__)
x = Son()

x.funcA()

```
