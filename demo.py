java=int(input("java marks :"))
python=int(input("python marks :"))
sql=int(input("sql marks :"))
if java<35 or python<35 and sql<35:
    print('fail')
else:
    per=((java+sql+python)/300)*100
    if per>=85:
        print("distinction")
    elif per<85 and per>=60:
        print('first class')
    elif per<60 and per>=35:
        print("pass")