class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
    
class circulur_double_link:
    def __init__(self):
        self.head=None
    
    def insert_at_last(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            newNode.prev=self.head
            newNode.next=self.head
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp
            newNode.next=self.head
            self.head.prev=newNode
    def display(self):
        if self.head is None:
            print("no elments to print")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
                if temp==self.head:
                    break
            print()
    def length(self):
        if self.head is None:
            print("no elements")
        else:
            temp=self.head
            count=0
            while temp:
                temp=temp.next
                count+=1
                if temp==self.head:
                    break
            print(count)
    def insert_at_first(self,val):
        newNode=Node(val)
        if self.head is None:
            print("no elements")
        else:
            temp =self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.head
            newNode.prev=temp
            self.head=newNode
            
            
    def insert_at_loc(self,loc,val):
        newNode=Node(val)
        if loc<=0:
            print("enter greater than Zero")
        elif loc==self.length()+1:
            self.insert_at_last(val)
        # elif loc==self.length():
        #     print("enter the loc less than",self.length()+1)
        elif loc==self.length():
            self.insert_at_last(val)
        elif loc==1:
            self.insert_at_first()
        elif self.head is None:
            self.head=newNode
            newNode.prev=self.head
            newNode.next=self.head
        else:
            temp=self.head
            cnt=1
            while temp.next!=None and cnt<loc-1:
                temp=temp.next  
                cnt+=1
            newNode.prev=temp
            newNode.next=temp.next
            temp.next=newNode
            newNode.next.prev=newNode
    def delete_at_last(self):
        if self.head is None:
            print("no elements")
        else:
            temp=self.head
            while temp.next.next !=None:
                temp=temp.next
            temp.next=self.head
            self.head.prev=temp
    def delete_at_first(self):
        if self.head is None:
            print("no elements to del")
        elif self.head.next==self.head:
            self.head =None
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
            self.head.prev=temp
    def delete_at_loc(self,loc):
        if self.head is None:
            print("no elements to del")
        elif self.head.next==self.head:
            self.head=None
        elif loc <=0:
            print("enter the loc greaterthan zero")
        elif loc==1:
            self.delete_at_first()
        elif loc==self.length():
            self.delete_at_last()
        else:
            temp=self.head
            conut=1
            while temp.next != None and conut<loc-1:
                temp=temp.next
                count+=1
            temp.next=temp.next.next
            temp.next.prev=temp
            
            
    
ob=circulur_double_link()
ob.insert_at_last(10)
ob.insert_at_last(199)
ob.insert_at_last(111)
ob.display()
ob.length()
ob.insert_at_first(2443)
ob.insert_at_first(43)
ob.insert_at_first(2)
ob.display()
ob.insert_at_loc(2,20)
ob.insert_at_loc(7,2990)
ob.display()


             