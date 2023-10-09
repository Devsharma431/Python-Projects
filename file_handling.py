# Python code to create a file
file = open('py.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.write("THis is a new text by dev sharma ")
file.close()
f = open('py.txt','r')
print(f.read())

