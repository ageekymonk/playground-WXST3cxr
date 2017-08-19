def addressbook(firstname, lastname, age, address=''):
    print(f'Name: {firstname} {lastname} \nAge: {age} \naddress: {address}')

# How not to do it
addressbook('Jason', 'Bourne', 40, 'unknown')

print('---------------------------')

# How pros do it
addressbook(lastname='Bourne',
            firstname='Jason',
            age=40,
            address='unknown')
