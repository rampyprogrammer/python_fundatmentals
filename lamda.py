import pickle as p
f=open('file.pkl','rb')
res=p.load(f)
print(res)
f.close()