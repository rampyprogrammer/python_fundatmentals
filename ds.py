class tree:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
    
    #insertion
    def insert(self,val):
        if self.data:
            if val < self.data:
                if self.prev is None:
                    self.prev=tree(val)
                else:
                    self.prev.insert(val)
            elif val > self.data:
                if self.next is None:
                    self.next = tree(val)
                else:
                    self.next.insert(val)
        else:
            self.data = val 
    
    #pre_order_traversal
    def pre_order(self,root):
        if root:
            print(root.data,end=" - > ")
            self.pre_order(root.prev)
            self.pre_order(root.next)
          
            
    #inorder traversal
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.prev)
            print(root.data,end=" - > ")
            # print("hello")
            self.inorder_traversal(root.next)
            
root=tree(None)
root.insert(15)
root.insert(9)
root.insert(19)
root.insert(6)
root.insert(12)
root.insert(4)
root.insert(7)
root.insert(17)
root.insert(20)
root.pre_order(root)
print()
print("in_ordered")
root.inorder_traversal(root)

            
            
    
    