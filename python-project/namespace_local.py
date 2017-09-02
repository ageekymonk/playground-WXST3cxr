# Here the current namespace is module. So local is equal to global
print(locals() == globals())


def yoda_says(*args, **kwargs):
    prefix = "YodaSays :"
    print(locals())
    quote_list = ["Always pass on what you have learned"]

# you wont see quote_list as it is not visible at that point for locals while it is constructing it.
yoda_says()


class Yoda:
    quote_list = ["Always pass on what you have learned"]
    yoda_dict = locals()
    yoda_dict['movies'] = ['The Phantom Menace', 'Attack of the clones', 'Revenge of the sith']

print(vars(Yoda))
