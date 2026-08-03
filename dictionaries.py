#dictionaries are key valued pairs
#dictionaries are immutable
user = {
    "name": "Tonny",
    "age": 32,
    "height": 6.2
}
print(f"my name is {user['name']}")
#searching for info /key in a dictionary
print(user["name"])
#adding or updating in dictionaries
user ["career"] = "pharmacy"
user ["age"] = 37
print(user["age"])
#removing keys from dictionaries
#del user["age"]
#or
#user.pop("height")
#to print all keys in a dictionary
print(user.keys())
#to print all values in a dictionary
print(user.values())
# to print all items in a dictionary
print(user.items())
#to print the length of a dictionary
print(len(user))
#checking if a key exists in a dictionary
if "email" in user:
    print("email exists")
else:
    print("email does not exist")
if "age" in user:
    print(f"{user['name']} is {user['age']} years old")
else:
    print("age does not appear in the dictionary")