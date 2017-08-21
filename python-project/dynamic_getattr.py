class BetterDict(dict):
    def __init__(self, *args):
        super().__init__(*args)

    def __getattr__(self, key):
        if self.__contains__(key):
            return self.__getitem__(key)
        else:
            #For unknown key return empty dict
            return {}


addressbook = BetterDict()
addressbook['jason'] = {'name': 'Jason Bourne', 'age': 40}
print(addressbook.jason)
print(addressbook.ironman)
