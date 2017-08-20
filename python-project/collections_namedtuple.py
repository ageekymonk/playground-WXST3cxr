from collections import namedtuple

Contact = namedtuple('Contact', 'name, age, address')

jason = Contact(name='Jason Bourne', age='40', address='unknown')
print(jason)
print(f'Name: {jason.name} \nage: {jason[1]}')

name, age, address = jason
print(f'Name: {name} \nage: {age}')
