#converting json file into python dictionary using 
#json package method
import json as j
d1={'name':'spider','age':34,'king':'virat'}

#establishing steam between json.py and file1.json in read mode
f=open("file1.json","w")

#loading file1.json as dictionary
j.dump(d1,f)
print(f)
print(d1,type(d1))
f.close()