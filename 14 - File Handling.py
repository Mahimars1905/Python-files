# x = create   #  for  create folder
# a = append   # for add in folder
# w = write    # for overwrite in folder
# t = text (default value)
# open() - function used to open the file 

## Creating a file
# f = open("myfile.txt", "x")
# f.close()

# f = open("myfile.txt", "r")
# content = f.read()
# print(content)
# f.close()

## Append
# f = open("myfile.txt", "a")
# f.write(" I am appending the file\n")
# f.close()

## Write
# f = open("myfile.txt", "w")
# f.write("I am writing the file\n")
# f.close()

# import os
# os.remove("myfile.txt")  # for remove .txt file !