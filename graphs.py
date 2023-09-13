class Graph:
    def __init__(self):
        self.gdict={}
    
    #add vertex
    def addvertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex]=[]
        
        
    #Add edges
    def addedges(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            
    #display
    def display(self,vertex):
        print(vertex ,":",self.gdict[vertex])
    
    #Remove edge
    def rem_egde(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
        
        
    #remove vertex
    def rem_vertex(self,vertex):
        if vertex in self.gdict.keys():
            for val in self.gdict[vertex]:
                self.gdict[val].remove(vertex)
            del self.gdict[vertex]
            
    #breadth first search
    def bfs_traversing(self,vertex):
         
        visited =[vertex]
        queue =[vertex]
        while queue:
            dvertex =queue.pop(0)
            print(dvertex,end=" ")
            for adj_veretex in self.gdict[dvertex]:
                if adj_veretex not in visited:
                    visited.append(adj_veretex)
                    queue.append(adj_veretex)
                    
    #depth first searching 
    def dfs_traversel(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            rem_vertex =queue.pop()
            print(rem_vertex,end=" ")
            for adj_vertex in self.gdict[rem_vertex]:
                if adj_vertex not in visited:
                    visited.append(adj_vertex)
                    queue.append(adj_vertex)
ob=Graph()
ob.addvertex("A")
ob.addvertex("B")
ob.addvertex("C")
ob.addvertex("D")
ob.addvertex("E")

ob.addedges("A","B")
ob.addedges("A","C")
ob.addedges("C","D")
ob.addedges("B","D")
ob.addedges("B","E")
ob.addedges("D","E")

ob.display("A")
ob.display("B")
ob.display("C")
ob.display("D")
ob.display("E")
# ob.rem_vertex("C")
# print("heyyy")
# ob.display("A")
# ob.display("B")
# ob.display("C")

# ob.display("D")
# ob.display("E")
ob.bfs_traversing("A")
print()
ob.dfs_traversel("A")


