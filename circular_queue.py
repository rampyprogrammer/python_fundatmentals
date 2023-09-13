class Circular_queue:
    def __init__(self,maxSize):
        self.maxSize =maxSize
        self.data=maxSize*[None]
        self.front = -1
        self.rear = -1
        
    def display(self):
        print(self.data)
    def isFull(self):
        if self.front == 0 and self.rear + 1 == self.maxSize:                 
            return True
        elif self.rear+1==self.front:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            print("cq is full")
        else:
            if self.rear+1==self.maxSize:
                self.rear = 0
            else:
                self.rear +=1
                if self.front == -1:
                    self.front+=1
            self.data[self.rear]=value
                
    def peek_ele(self):
        if self.isEmpty(): 
            print("cq is empty")
        else:
            print("peek element in cq-->",self.data[self.front])
    
    def dequeu(self):
        if self.isEmpty():
            print("no ele to delete")
            
        else:
            r_ele=self.data[self.front] 
            start=self.front
            if self.front == self.rear:
                self.front == -1
                self.rear == -1
            elif self.front +1== self.maxSize:
                self.front=0
            else:
                self.front+=1
            self.data[start] =None     
            return r_ele
        
cq=Circular_queue(5)
cq.display()
# cq.enqueue(12)
# cq.enqueue(120)
# cq.enqueue(30)
# cq.enqueue(40)
# cq.enqueue(40)
# cq.display()
# cq.dequeu()
# cq.display()
# cq.enqueue(45)
# cq.display()
cq.enqueue(10)
cq.enqueue(1011)
cq.enqueue(101)
cq.enqueue(100)
cq.enqueue(19)
cq.display()
cq.dequeu()
cq.dequeu()
cq.dequeu()
cq.dequeu()

cq.display()
cq.enqueue(10)
cq.display()
cq.dequeu()
cq.display()
cq.peek_ele()