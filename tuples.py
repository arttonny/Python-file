#basic creation of a tuple
#using brackets
tuple1 = (1, 2, 3, 4, 5)
#or lose the brackets
tuple2 = 1, 2, 3, 4, 5, 6, 7
#single element tuples must include a trailing comma
tuple3 = ("ready",)
tuple4 = (4,) 
not_a_tuple = ("stay")
#converting a list to a tuple
alist = tuple([1, 2, 3, 4, 5])
#indexing and slicing in tuples works just like in lists.
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[-2])
#tuples are immutable. Tring to change them raises a type error
#tuple1[0] = 8
#print (tuple1)
#if a tuple contains a list, that nested list can be modified.
tuple5 = (1, 4, [5, 2, 3, 6, 8], "stray")
print (tuple5)
tuple5[2].append(12)
print (tuple5)
#because tuples cannot be changed, they have only 2 built-in methods: count and index
tuple6 = (1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 5, 6, 6, 7, 7, 9)
print(tuple6.count(7))
print(tuple6.index(8))
#tuples can be used to return multiple values from a function
def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print(x, y)
def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    position = input("Enter your job title: ")
    return (name, age, position)
#unpacking elements
point = (3, 7)
x, y = point #x = 3, y = 7
#swapping two variables without a temporary variable
a, b= 2, 4
a, b = b, a #now a = 4 and b = 2
print(a, b)