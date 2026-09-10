#standard modules(math & random)
import random
#generating a random integer
random_integer = random.randint(1,23)
print(random_integer)
#generating a random float
random_float = random.random()
print(random_float)
#picking a random element from a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
chosen_fruit = random.choice(fruits)
print(chosen_fruit)
#shuffling a list
cards = [1,2,3,4,5,6,7]
random.shuffle(cards)
print(cards)