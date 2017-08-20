from collections import defaultdict
import json

def tree():
    return defaultdict(tree)

addressbook = tree()
addressbook['jason']['name'] = 'Jason Bourne'
addressbook['jason']['phone']['mobile'] = '11111111'
print(json.dumps(addressbook))
