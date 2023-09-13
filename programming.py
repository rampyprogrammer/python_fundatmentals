def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in the graph")
    else:
        node_count+=1
        nodes.append(v)
        for n in graphs:
            n.append(0)
        temp =[]
        for i in range(node_count):
            temp.append(0)
        graphs.append(temp)
        
        
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in nodes")
    elif v2 not in nodes:
        print(v2,"is not present in nodes")
    
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graphs[index1][index2] = 1
        graphs[index2][index1] = 1
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graphs[i][j],end=" ")
        print()
             
        
        
nodes=[]
graphs=[]
node_count = 0
print("before adding nodes")
print(nodes)
print(graphs)
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B")
add_edge("A","C")
print("after adding nodes")
print(nodes)
print(graphs)
print_graph()

