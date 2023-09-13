class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single_linked:
    def __init__(self):
        self.head=None
    
    #insert at last
    def insert_at_last(self,value):
        newNode=Node(value)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
        else:
            self.head=newNode
    def display(self):
        if self.head is None:
            print("no elements to display")
        else:
            temp=self.head
            while temp :
                print(temp.data,end=" --> " )
                temp=temp.next
            print()
    def insert_at_first(self,val):
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
    
    def insert_at_loc(self,val,loc):
        newNode=Node(val)
        if loc<=0:
            print("enter loc graeter than 0")
        elif loc==1:
            newNode.next=self.head
            self.head=newNode
        else:
            temp=self.head
            cnt=1
            while temp != None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            newNode.next=temp.next
            temp.next=newNode
        
                
    
    def length_of_ll(self):
        if self.head is None:
            print("no elements to count")
        else:
            temp=self.head
            cnt=0
            while temp:
                temp=temp.next
                cnt+=1
            print("length of linked list -->",cnt)

    
    def delet_at_last(self):
        if self.head is None:
            print("no elements to delete")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
    def delete_at_first(self):
        if self.head is None:
            print("no elements to delete")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
    def delete_at_loc(self,loc):
        if loc<=0:
            print("enter loc graeter than 0")
        elif loc==1:
            temp=self.head
            self.head=temp.next
            temp.next=None
        else:
            temp=self.head
            cnt=1
            while temp != None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            temp.next=temp.next.next
    
            
    
ob=Single_linked()
ob.insert_at_last(1453)
ob.insert_at_last(43)
ob.insert_at_last(143)
ob.insert_at_last(14)
ob.display()
ob.insert_at_first(10)
ob.insert_at_first(14)
ob.insert_at_first(12)
ob.display()
ob.length_of_ll()
ob.insert_at_loc(44,4)
ob.insert_at_loc(498,5)

ob.display()
ob.delet_at_last()
ob.display()
ob.delete_at_first()
ob.delete_at_loc(5)
ob.display()



