class Person():
    __slots__ = ['name', 'age', 'address']

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nAddress: {self.address}'

jason = Person('Jason Bourne', '40', 'unknown')
print(jason)
