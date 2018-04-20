#Reading and writing to files

"""
'r' --->open files in read only mode
'.readline' --> read 1 loine at a time
'w' --->open file in write only mode or create file
'w+' --->open file in a reading and writing modes
'a' --->Append to a file

with-as ---> automaticaly closes the file for you
"""
# read_only = open("test.txt", "r")
# print(read_only.read())
#
# #Automaticaly closes file for you
#
# with open("test.txt", "r") as file_name:
#     print(file_name.read())

# using ".readline"

read_line = open("test.txt", "r")
for i in read_line:
    print(i)
