#a function is a block of code designed to perform a specific function.
# Defining the function
def say_hello():
    print("Welcome to Python programming!")

# Calling (running) the function
say_hello()  # Output: Welcome to Python programming!
def introduce(name, age):
    print (f"My name is {name}. I am {age} years old.")
#calling the function
introduce("Antony", 33)
#output is (My name is Antony. I am 33 years old.)
def calculate_price(price, tax_rate):
    total_price = price + (price * tax_rate)
    return total_price
print (calculate_price(100, 0.20))