import random

def generate_password(length=8):
    # Define pool of allowed characters
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    
    # Pick a random character 'length' times and assemble into a list
    password_chars = [random.choice(chars) for _ in range(length)]
    
    # Join the character list into a single string
    password = "".join(password_chars)
    
    return password

# Testing Problem 3:
print("Default password (8 chars):", generate_password())
# Output: e.g., 'k9#mP2!x'

print("Custom password (16 chars):", generate_password(16))
# Output: e.g., 'A8$vL2#mQ9!zR4&p'