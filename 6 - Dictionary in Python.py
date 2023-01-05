# Dictionary - '''Dictionary is a data structure in python used to store multiple values in a single variable. 
# Dictionary is mutable/changable.
# Data stored in Dictionary in Key:Value pair
# Key can't be same, Values can be same/duplicate
# Dictionary can contain multiple data types
# Dictionary is an unordered collection of data elements
 
# fruits = {"apple":100, "banana":50, "orange":80, "mango":600}
# fruits = dict({"apple":100, "banana":50, "orange":80, "mango":400})
# print(fruits)
# print(type(fruits))

# print(fruits["apple"])     # getting value of apple

# fruits["apple"] = 300      # changing value of apple
# print(fruits)

# fruits["pineapple"] = 300   # adding new key:value in dict
# print(fruits)

# fruits.update({"apple":700, "pineapple":500})  # changing value of apple  and adding new (key:pair)
# print(fruits)

# print(fruits.get("apple"))    # getting value of apple

# fruits.pop("apple")          # deleting apple from dict
# print(fruits)

# fruits.popitem()             # deleting  last element
# print(fruits)

# fruits.clear()               # for clear all dictionary
# print(fruits)

# fruits.setdefault("pineapple")  # adding new key without value
# print(fruits)

# x = fruits.copy()            # for copy
# print(x)

# fromkeys()          # used for change list to dict. , tuple to dict.
# Python Dictionary fromkeys () Method Syntax: Syntax : fromkeys (seq, val) Parameters : seq : The sequence to be transformed into a dictionary. val : Initial values that need to be assigned to the generated keys. Defaults to None. Returns : A dictionary with keys mapped to None if no value is provided, else to the value provided in the field.

# fruits = ["orange", "banana", "apple", "mango"]   #giving values
# values = None

# x = dict.fromkeys(fruits,0)     # giving values to list items and changing them to dict.
# print(x)

# print(fruits.items())       
# print(fruits.keys())
# print(fruits.values())
