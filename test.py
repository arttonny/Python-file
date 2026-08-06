def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    position = input("Enter your job title: ")
    return (name, age, position)
print(get_user_info())
# Unpacking elements
point = (3, 7)
x, y = point  # x = 3, y = 7

# Returning multiple values from a function (uses tuples under the hood!)
def get_user_info():
    return "Alex", 28, "Developer"

name, age, job = get_user_info()

# Swapping two variables without a temporary variable
a, b = 5, 10
a, b = b, a  # Now a = 10, b = 5