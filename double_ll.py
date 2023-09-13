class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Double_linked_list:
    def __init__(self):
        self.head=None
        
    #insert at last
    def add_at_last(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp
            
    def display(self):
        if self.head is None:
            print("No elements to delete")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" <=> ")
                temp=temp.next
            print()
            
    def add_at_first(self,val):
        newNode=Node(val)    
        if self.head is None:
            self.head=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
    def length_dll(self):
        if self.head is None:
            print("no elements to count")
        else:
            temp=self.head
            cnt=0
            while temp:
                temp=temp.next
                cnt+=1
            return cnt
    def add_at_loc(self,val,loc):
        newNode=Node(val)
        if loc > self.length_dll():
            print("loc must be less than length of list")
        elif loc<=0:
            print("enter the loc greater than 0")
        elif loc ==1:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
        else:
            temp=self.head
            cnt=1
            while temp.next != None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            newNode.prev=temp.next.prev
            temp.next.prev=newNode
            newNode.next=temp.next
            temp.next=newNode
    def delete_at_last(self):
        if self.head is None:
            print("no ele's to delete")
        elif self.head==self.head.next:
            self.head=None
        else:
            temp=self.head
            while temp.next.next != None:
                temp=temp.next
            temp.next=None
    def delete_at_first(self):
        if self.head is None:
            print("no ele's to delete")
        elif self.length_dll()==1:
            self.head=None
            
        else:
            self.head=self.head.next
            self.head.prev=None
            
    def delete_at_loc(self,loc):
        if self.head is None:
            print("no ele's to delete")
        elif loc > self.length_dll():
            print("enter the loc less than",self.length_dll())
            
        elif loc<=0:
            print("enter the loc graeter than zero")
        elif loc==1: 
            self.head=self.head.next
            self.head.prev=None
        elif loc==self.length_dll():
            self.delete_at_last()
            
        else:
            temp=self.head
            count=1
            while temp.next != None and count<loc-1:
                temp=temp.next
                count+=1
            temp.next=temp.next.next
            temp.next.prev=temp
            
            
               
            
            
ob=Double_linked_list()
ob.add_at_last(10)    
ob.add_at_last(33)    
ob.add_at_last(1011)    
ob.add_at_last(134) 
ob.display()
ob.add_at_first(90)
ob.add_at_first(999)

ob.display() 
ob.add_at_loc(190,2)  
ob.display() 
ob.delete_at_first()
ob.display() 
ob.delete_at_loc(3)
ob.display() 
print(ob.length_dll())

ob.delete_at_loc(5)

ob.delete_at_loc(1)
ob.display() 
ob.add_at_loc("d",2)
ob.display() 
ob.add_at_loc("jai shree ram",4)
ob.display() 



