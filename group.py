"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# Create the initial group structure
my_group = [
    {"name": "Jill", "age": 26, "job": "Biologist", "connections": [{"name": "Zalika", "relationship": "friend"},{"name": "John", "relationship": "partner"}]},
    {"name": "Zalika", "age": 28, "job": "Artist", "connections": [{"name": "Jill", "relationship": "friend"}]},
    {"name": "John", "age": 27, "job": "Writer", "connections": [{"name": "Jill", "relationship": "partner"}]},
    {"name": "Nash", "age": 34, "job": "Chef", "connections": [{"name": "John", "relationship": "cousin"},{"name": "Zalika", "relationship": "landlord"}]}
]
group = my_group

# Print the final group structure in a nicely formatted way
for i in group:
    print(i)
    
    


