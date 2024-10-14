"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group =group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "Biologist",
        "connections": [["Zalika", "friend"], ["John", "partner"]]
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "Artist",
        "connections": [["Jill", "friend"]]
    },
    {
        "name": "John",
        "age": 27,
        "job": None,  # No job specified
        "connections": [["Jill", "partner"], ["Nash", "cousin"]]
    },
    {
        "name": "Nash",
        "age": 34,
        "job": "Chef",
        "connections": []  # No connections
    }
]

# Print each person and their connections
for person in group:
    print(f"{person['name']} (age {person['age']}), Job: {person['job']}")
    for connection in person["connections"]:
        print(f"  - {connection[1]}: {connection[0]}")