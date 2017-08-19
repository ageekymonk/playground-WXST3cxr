def addressbook(name, age, address=''):
    print(f'Name: {name} Age: {age} address: {address}')

# How not to do it
addressbook('Jason Bourne', 40, 'unknown')

# How pros do it
addressbook(name='Jason Bourne',
            age=40,
            address='unknown')
