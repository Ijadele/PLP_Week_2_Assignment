# create an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert the value 15 at the 2nd position
my_list.insert(1, 15)

# extend my_list with another lists
my_list.extend([50, 60, 70])

# remove the last element 
my_list.pop()

# sorting list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)

print(my_list, index_of_30)