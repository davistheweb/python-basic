x = "man"
# Attempting to assign an attribute to a string object will raise an AttributeError
# x.man = "hekki" 

# Instead, you could create a dictionary and assign values to keys
x_dict = {}
x_dict['man'] = "hekki"

# Now you can access the value associated with the 'man' key
print(x_dict['man'])  # Output will be 'hekki'
