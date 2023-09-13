import json as j
j_string={"name":"rama","age":21,"gender":"male"}
print(j_string,type(j_string))

f=open("file1.json","w")
j.dumps(j_string,f)
f.close()