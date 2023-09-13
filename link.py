class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Single_linked:
    def __init__(self):
        self.head=None
        
    def insert_at_last(self,value):
        newNode=Node(value)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
        else:
           self.head=newNode
            
    #display elememnt
    def display(self):
        if self.head is None:
            print("no elelments in single linked list")
            
        else:
            temp=self.head
            while temp != None:
                print(temp.data,end="-->")
                temp=temp.next
            print()
        
    #length of ll
    def length_ll(self):
        if self.head is None:
            print("no ele to count")
        else:
            temp=self.head
            cnt=0
            while temp != None:
                cnt+=1
                temp=temp.next
            return cnt
        
    def insert_at_first(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
        
        
ob=Single_linked()
ob.insert_at_last(10)
ob.display()
ob.insert_at_last(120)
ob.insert_at_last(126)
ob.display()
print(ob.length_ll())
ob.insert_at_first(500)
ob.insert_at_first(524)
ob.insert_at_first(1234)
ob.display()

            