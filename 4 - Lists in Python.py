# List - List is a data structure in python used to store multiple values in a single variable. 
# List is mutable/changable
# List can contain duplicate values
# List can contain multiple data types
# List is an ordered collection of data elements

# fruits = ["orange", "banana", "apple", "mango"]
# fruits = list(("orange", "banana", "apple", "mango"))
# print(fruits)
# print(type(fruits))

# for i in range(0, len(fruits)):
#     print(i, fruits[i])

# fruits = ["orange", "banana", "apple", "mango"]

# print(fruits[0])
# print(fruits.index("orange"))
# print(len(fruits))


# fruits.sort()                   # Sorting in ascending order
# print(fruits)

# fruits.sort(reverse=True)       # Sorting in descending order
# print(fruits)

# fruits.append("pineapple")      # add in last=["orange", "banana", "apple", "mango", "pineapple"]
# print(fruits)

# num = [78,87,25,65]             # output=["orange", "banana", "apple", "mango", 78,87,25,65]
# fruits.extend(num)
# print(fruits)

# fruits.reverse()                # ["mango", "apple", "banana", "orange"]
# print(fruits)

# fruits.insert(2, "pineapple")    # ["orange", "banana", "pineapple" "apple", "mango"]
# print(fruits)

# fruits.remove("banana")          # ["orange", "apple", "mango"]
# print(fruits)

# fruits.pop()                    # ["orange", "banana", "apple"]  = remove last element
# print(fruits)

# fruits.pop(2)                  #  ["orange", "banana", "mango"]  = index(2) delete
# print(fruits)

# del fruits                     #  list delete
# print(fruits)

# del fruits[0]                  #  index(0) delete
# print(fruits)

# fruits.clear()                #  all elements delete
# print(fruits)

# x = fruits.copy()             #  ['orange', 'banana', 'apple', 'mango'] 
# print(x)

# x = fruits.count("apple")     #    [1]
# print(x)

