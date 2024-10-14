
"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import json

# Function to add a relationship and decide whether to make it mutual based on the relationship type
def add_connection(group, person_name, connection_name, relation):
    # Find both people's records
    person = next((p for p in group if p["name"] == person_name), None)
    connection = next((p for p in group if p["name"] == connection_name), None)
    
    if person and connection:
        # Add the connection for the person
        if [connection_name, relation] not in person["connections"]:
            person["connections"].append([connection_name, relation])
        
        # Only add reciprocal relationship for symmetric types
        if is_symmetric_relation(relation):
            if [person_name, relation] not in connection["connections"]:
                connection["connections"].append([person_name, relation])

# Define which relationships are symmetric (mutual)
def is_symmetric_relation(relation):
    symmetric_relations = ["friend", "partner", "cousin", "colleague"]
    return relation in symmetric_relations

# Create the initial group structure
group = [
    {"name": "Jill", "age": 26, "job": "Biologist", "connections": []},
    {"name": "Zalika", "age": 28, "job": "Artist", "connections": []},
    {"name": "John", "age": 27, "job": None, "connections": []},
    {"name": "Nash", "age": 34, "job": "Chef", "connections": []}
]

# Add both symmetric and non-symmetric relationships
add_connection(group, "Jill", "Zalika", "friend")
add_connection(group, "Jill", "John", "partner")
add_connection(group, "John", "Nash", "cousin")
add_connection(group, "Nash", "Zalika", "landlord")  # Non-symmetric relationship, only outputs landlord, no tenant

# Print the final group structure in a nicely formatted way
print(json.dumps(group, indent=4))
