class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack_ll:
    def __init__(self):
        self.head=None
    
    def Push(self,ele):
        newNode=Node(ele)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
     
    def display(self):
        if self.head is None:
            print("no elements to diplay")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print()
    def Min_element(self):
        if self.head is None:
            print("no elements")
        else:
            min=self.head.data
            temp=self.head
            while temp:
                if min>temp.data:
                    min=temp.data
                temp=temp.next
            print(min)
            
    #remove an elements
    def pop(self):
        if self.head is None:
            print("no elemen ts to remove")
        else:
            self.head=self.head.next
            
            
            


ob=stack_ll()

ob.Push(5)
ob.Push(10)
ob.Push(111)
ob.Push(13)
ob.display()
ob.Min_element()
ob.pop()
ob.display()

    
        