# This create an empty list called my_list
my_list = []

#  This append elements 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# This print my_list contents
print(my_list)  # output:[10,20,30,40]

# This will add 15 to the second position(index 1,since Python uses zero-based indexing) in the list
my_list.insert(1, 15)

# After adding element to my list,we print
print(my_list)  # output:[10,15,20,30,40]

# This will extend my_list with [50,60,70]
my_list.extend([50, 60, 70])

# After extending my_list,we print
print(my_list)  # output:[10,15,20,30,40,50,60,70]

# This remove the last element from my_list
my_list.pop()

# After removing last element from my_list,we print
print(my_list)   # output:[10,15,20,30,40,50,60]

# This sort my_list in ascending order
my_list.sort()

# After sorting  my_list,we print
print(my_list)   # output:[10,15,20,30,40,50,60]

# This will search for the first occurrence of 30 in my_list and print its index
index_of_30 = my_list.index(30)
print(index_of_30)  # output:3
