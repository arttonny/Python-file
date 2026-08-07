#standard creation of sets
set1 = {"cherry", "banana", "apple" ,"mango"}
print (set1)
#duplicate removal
set2 = {1, 2, 3, 5, 4, 2, 6, 5, 3, 8, 2, 1, 7, 9, 1}
print (set2)
#to create an empty set use set() because {} creates an ampty dictionary
empty_set = set()
print (empty_set)
#converting a list into a set
#the conversion removes duplicates
list1 = [1, 1, 3, 2, 6, 4, 5, 7, 7, 9, 5, 2, 3, 8, 8, 12]
set5 = set(list1)
print (set5)
colours = {"red", "blue", "green"}
# adding a single item
colours.add("yellow")
print (colours)
#adding multiple items from another collection
colours.update(["black", "white", "orange"])
print (colours)
#removing an item
colours.remove("red")
print (colours)
#safely remove an item. does nothing if the item is missing
colours.discard("blue")
print (colours)
popped_item = colours.pop()
print (popped_item)
set6 = {1, 2, 3, 4, 5}
set7 = {4, 5, 6, 7, 8}
#union of the sets
print (set6 | set7)
#intersection of both sets
print (set6 & set7)
#difference of the two sets
print (set6 - set7)
#symmetric difference (items in a or b but not in both)
print (set6 ^ set7)