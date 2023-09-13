class Stack:
    def __init__(self,maxSize):
        self.data=[]
        self.maxSize=maxSize
    
    def isEmpty(self):
        if self.data == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.data)==self.maxSize:
            return True
        else:
            return False
    
    def lenOfStack(self):
        return len(self.data)
    
    def peek(self):
        if len(self.data)==self.maxSize:
            return "stack is full"
        else:
            return self.data[-1]
    
    def push(self,ele):
        self.data.append(ele)
        
    def display(self):
        return self.data
        
    def pop(self):
        if self.isEmpty():
            return "No elements to remove"
        else:
            return self.data.pop()
   
s1=Stack(5)
while True:
    print("select the operations to perform on stack :")
    print("1.push\n2.pop\n3.peek\n4.display\n5.isEmpty\n6.isFull\n7.length")
    opt=int(input("eneter your option :"))
    match opt:
        case 1:
            val=int(input("enter the element to insert :"))
            s1.push(val)
        case 2:
            print("remove the element from the stack",s1.pop())
        
        case 3:
            print("top element ",s1.peek())
            
        case 4:
            print(s1.display())
        case 5:
            print("is Stack is empty",s1.isEmpty())
            
        case 6:
            print("is stack is full",s1.isFull())
        
        case 7:
            print("lenght of stack is",s1.lenOfStack())
            
        case _:
            exit()
            
            
    