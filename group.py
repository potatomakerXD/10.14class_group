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
        
        # 函数来添加关系并保证关系互通
def add_connection(group, person_name, connection_name, relation):
    # 找到两个人的记录
    person = next((p for p in group if p["name"] == person_name), None)
    connection = next((p for p in group if p["name"] == connection_name), None)
    
    if person and connection:
        # 为 person 添加 connection
        if [connection_name, relation] not in person["connections"]:
            person["connections"].append([connection_name, relation])
        
        # 为 connection 添加反向关系
        reverse_relation = get_reverse_relation(relation)
        if [person_name, reverse_relation] not in connection["connections"]:
            connection["connections"].append([person_name, reverse_relation])

# 定义关系的反向
def get_reverse_relation(relation):
    reverse_relations = {
        "friend": "friend",
        "partner": "partner",
        "cousin": "cousin",
        "landlord": "tenant",  # 房东和租客的关系
        "tenant": "landlord",
        "colleague": "colleague"
    }
    return reverse_relations.get(relation, relation)

# 创建初始的群体结构
group = [
    {"name": "Jill", "age": 26, "job": "Biologist", "connections": []},
    {"name": "Zalika", "age": 28, "job": "Artist", "connections": []},
    {"name": "John", "age": 27, "job": None, "connections": []},
    {"name": "Nash", "age": 34, "job": "Chef", "connections": []}
]

# 添加互通的关系
add_connection(group, "Jill", "Zalika", "friend")
add_connection(group, "Jill", "John", "partner")
add_connection(group, "John", "Nash", "cousin")
add_connection(group, "Nash", "Zalika", "landlord")

# 显示最终的结构
group

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

# Show the final group structure
group
