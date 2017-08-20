from collections import defaultdict

addressbook = defaultdict(lambda: "unknown")
addressbook['jason'] = {'name': 'jason bourne', 'age': 40}

print(addressbook['jason'])
print(addressbook['ironman'])
