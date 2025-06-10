# a first look at reading files 

file = open("testfile.txt", "r")
content = file.read()

print("The file's name is ", file.name)
print("Is the file closed? ", file.closed)
print("The file was opened in which mode? ", file.mode)
print(type(content))
print(repr(content))

content_of_line = file.readline()

print(repr(content))

file.close()