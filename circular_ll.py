class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Circular_linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_last(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head=newNode
            newNode.next=self.head
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
                if temp == self.head:
                    break
            temp.next = newNode
            newNode.next=self.head
    def display(self):
        if self.head is None:
            print("no elements to dipslay")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" --> ")
                temp=temp.next
                if temp==self.head:
                    break
            print()
    def length_ll(self):
        if self.head is None:
            print("no elements to count")
        
        else:
            temp=self.head
            count=0
            while temp:
                temp=temp.next
                count+=1
                if temp==self.head:
                    break
            return count
    def inesrt_at_last(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            newNode.next=self.head
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.head
            self.head=newNode
    def insert_at_first(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            newNode.next=self.head
        
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.head
            self.head=newNode
    #insert at location
    def insert_at_loc(self,val,loc):
        newNode=Node(val)
        if loc>self.length_ll():
            print("enter the loc less than len of ll")
        elif loc<=0:
            print("enter the loc greater than 0")
        elif loc == 1:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.head
            self.head=newNode
        else:
            temp=self.head
            cnt=1
            while temp.next != None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            newNode.next=temp.next
            temp.next=newNode
    # delete elemen0ts at last
    def delete_at_last(self):
        if self.head is None:
            print("no elements to delete")
        
        elif self.head.next == self.head:
            self.head=None
        else:
            temp=self.head
            while temp.next.next != self.head:
                temp=temp.next
            temp.next=self.head
    
    #delete at first
    def delete_at_first(self):
        if self.head is None:
            print("no elements to delete")
        
        elif self.head.next == self.head:
            self.head=None
        
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=self.head.next
            self.head=temp.next
    
    #delete at specified location
    def delete_at_loc(self,loc):
        if loc > self.length_ll():
            print("enter loc less than length of ll")
        elif loc<=0:
            print("enter the loc greater than 0")
        elif loc==1:
            self.head=None
            
        else:
            temp=self.head
            cnt=1
            while temp.next != None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            temp.next=temp.next.next
            

                
        
            
        
        
        
        
        
            
            
        
        
        
        
        
        
ob=Circular_linked_list()  
ob.insert_at_last(10)             
ob.insert_at_last(103)             
ob.insert_at_last(13)             
ob.insert_at_last(12)   
ob.insert_at_last(199)   
ob.insert_at_last(15)   
ob.insert_at_last(1654)   
ob.display()    
print("no of elements present in list is -->",ob.length_ll()) 
ob.insert_at_first(120)    
ob.insert_at_first(100)    
ob.display()    
ob.delete_at_first()
ob.display() 
ob.delete_at_loc(3)
ob.display() 
ob.delete_at_loc(7)
ob.display() 




 
                    
    
