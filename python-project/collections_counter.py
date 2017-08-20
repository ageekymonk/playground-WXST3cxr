import collections


c = collections.Counter([1, 2, 3, 1, 3, 1, 3, 4])
print(c)

# Accessing individual elements
print(f'4 is repeated {c[4]} times')

# Finding most common elements
print(f'Most common element is {c.most_common(1)[0][0]} repeated {c.most_common(1)[0][1]} times')
