#empty list
list1 = []
# mixed list
person = ["Alice", 26, 5.7, True]
#list generation
new_list = list(range(1, 20, 2))
print(new_list)
#list indexing
list2 = ["Isaac" ,"Kim", "John", "Mwas", "Shaz", "Msoh", "Tonny", "Ngatia"]
print (list2[4])
print (list2[-3])
#list slicing
#list[start:stop:step]
print(list2[1:6:3])
#list methods
list2.append("ndaiga")
print (list2)
list2.insert(3, "Jose")
print (list2)
#remove
list2.remove("Jose")
print (list2)