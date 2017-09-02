
# To get module dictionary.
module_dict = globals()

# Adding a variable to the module namespace
my_module_var = 'hello'

print(f'Module name: {module_dict["__name__"]}, Value of my my_module_var: {module_dict["my_module_var"]}')

# Adding a variable to module namespace by adding to the dictionary directly
module_dict["my_new_var"] = "world"

# Accessing created variable
print(f'Value of my_new_var is {my_new_var}')
