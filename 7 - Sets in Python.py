# Set - Set is a data structure in python used to store multiple values in a single variable. 
# Set is mutable/changable
# Set can't contain duplicate values
# Set can contain multiple data types
# Set is an un-ordered collection of data elements

# fruits = {"orange", "banana", "apple", "mango"}
# print(fruits)
# print(type(fruits))

# # add
# fruits.add("pineapple")       # adding 
# print(fruits)

# # update                                    # adding
# fruits.update({"pineapple", "guava"}) 
# print(fruits)

# # # discard                            # removing element (here pineapple is not in our set but program is runing)
# fruits.discard("pineapple")
# print(fruits)

# # remove                               # removing element (here pineapple is not in our set and program is not runing )
# fruits.remove("pineapple")
# print(fruits)
# 
# # difference                            # given what is different in fruits1 from fruits2
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana", "pineapple", "guava"}
# x = fruits1.difference(fruits2)
# print(x)

# # symmetric_difference                #  given different elements from fruits1 and fruits2
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana", "pineapple", "guava"}
# x = fruits1.symmetric_difference(fruits2)
# print(x)

# # difference_update                # given what is different in fruits1 from fruits2
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana", "pineapple", "guava"}
# fruits1.difference_update(fruits2)
# print(fruits1)

# # clear                                 # clear all element 
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits1.clear()
# print(fruits1)

# # pop                                #  delete any one element from set
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits1.pop()
# print(fruits1)

# #  union                                # adding different value from fruits2 in fruits1 
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana", "pineapple", "guava"}
# x = fruits1.union(fruits2)
# print(x)

# # copy                                  # copy
# fruits1 = {"orange", "banana", "apple", "mango"}
# x = fruits1.copy()
# print(x)

# # intersection                    # showing same element from fruits1 and fruits2
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana", "pineapple", "guava"}
# x = fruits1.intersection(fruits2)
# print(x)


# # intersection_update       # same as intersection
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana", "pineapple", "guava"}
# fruits1.intersection_update(fruits2)
# print(fruits1)

# # isdisjoint - The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange1", "banana1", "pineapple", "guava"}
# x = fruits1.isdisjoint(fruits2)
# print(x)

# # issubset                    # check something is commen in set1 and set2 , if any element is same it will return true
# fruits1 = {"orange", "banana"}
# fruits2 = {"orange", "banana", "apple", "mango"}
# x = fruits1.issubset(fruits2)
# print(x)


# # issuperset                      #  check something is commen in set1 and set2 , if any element is same it will return true
# fruits1 = {"orange", "banana", "apple", "mango"}
# fruits2 = {"orange", "banana"}
# x = fruits1.issuperset(fruits2)
# print(x)

