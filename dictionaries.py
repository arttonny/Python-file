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