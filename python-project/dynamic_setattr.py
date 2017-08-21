class BetterDict(dict):
    def __init__(self, *args):
        super().__init__(*args)

    def __getattr__(self, key):
        if self.__contains__(key):
            return self.__getitem__(key)
        else:
            #For unknown key return empty dict
            return {}

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

addressbook = BetterDict()
print(addressbook.ironman)
addressbook.ironman = {'name' : 'Iron Man', 'age': 35}
print(addressbook.ironman)
