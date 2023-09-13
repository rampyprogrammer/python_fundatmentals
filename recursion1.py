def revers(str):
    size=len(str)
    if size==0:
        return
    last_char=str[size-1]
    print(last_char,end="")
    revers(str[0:size-1])
    
    
str=input('enter str : ')  
revers(str)