#Reading and writing to files

"""
'r' --->open files in read only mode
'w' --->open file in write only mode or create file
'w+' --->open file in a reading and writing modes
'a' --->Append to a file

with-as ---> automaticaly closes the file for you
"""
file_one = open("test.txt", "w")
file_one.write("this is the first test with writing in a file ")
file_one.close()



file_one = open("test.xls", "w")
file_one.write("this is the first test with writing in a file ")
file_one.close()


#Automaticaly closes file for you

# with open("Textfiletwo.txt", "a") as demo_file:
#     demo_file.write("appended text")

