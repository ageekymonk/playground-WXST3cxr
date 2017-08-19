def addressbook(name, *phonenumber, **info):
    print(f'Name: {name}')
    for idx, elem in enumerate(phonenumber):
        print(f'phone {idx}: {elem}')

    for key, value in info.items():
        print(f'{key}: {value}')


addressbook('Jason Bourne',
            '11111111',
            '22222222',
            address='unknown')
