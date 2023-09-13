#establishing a stream
f=open("j.txt",'r')

#checking the cursor position
print(f.tell)

#reading first two char from file
print(f.read(2))

#checking the cursor posuition
print(f.tell)

#reading next two chr 
print(f.read(2))

#checking the cursor position
print(f.tell())

#moving the cursor back to start
f.seek(0)

#checking cursor position
print(f.tell())

#read
print(f.read())

#checking cursor pos
print(f.tell())

#closing the file
f.close