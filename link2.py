class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class single_linked:
    def __init__(self):
        self.head=None
    
    def insert_at_last(self,val):
        newNode=Node(val)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
            
        else:
            self.head=newNode
    def display(self):
        if self.head is None:
            print("no ele's to display")
        else:
            temp=self.head
            while temp != None:
                print(temp.data,end=" --> ")
                temp=temp.next
            print()
    def insert_at_first(self,val):
        newNode=Node(val)
        
        newNode.next =self.head
        self.head=newNode
    
    def insert_at_loc(self,val,loc):
        newNode=Node(val)
        if loc <= 0:
            print("enter the loc greater than zero")
        elif loc==1:
            # newNode=Node(val)
        
            newNode.next =self.head
            self.head=newNode
        else:
            temp=self.head
            cnt=0
            while temp !=0 and cnt < loc-1:
                temp=temp.next
                cnt+=1
            newNode.next=temp.next
            temp.next=newNode
        
    def delete_at_last(self):
        if self.head is None:
            print("no ele's to print ")
        else:
            temp=self.head
            while temp.next.next != None:
                temp=temp.next
            temp.next=None
        
    def delete_at_first(self):
        if self.head is None:
            print("no ele's to print ")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
    def delete_at_loc(self,loc):
        if loc <= 0:
            print("enter the loc greater than zero")
        elif loc==1:
            temp=self.head
            
            self.head=temp.next
        else:
            temp=self.head
            cnt=1
            while temp != None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            temp.next=temp.next.next

        

            
                
                
        
            
ob=single_linked()
print()
ob.insert_at_last(109)
ob.insert_at_last(9)
ob.insert_at_last(19)
ob.insert_at_last(10)
ob.display()
ob.insert_at_first(123)
ob.insert_at_first(144)
ob.insert_at_first(133)
ob.display()
ob.delete_at_first()
ob.display()
ob.delete_at_first()
ob.display()

        