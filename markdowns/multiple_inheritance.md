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
