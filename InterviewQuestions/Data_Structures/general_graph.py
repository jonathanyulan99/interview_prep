#Display graph vertices
#Display graph edges
#Add A Vertex
#Add an Edge
# Creating A Graph

'''

Vertex: Node interchangeable
Edge: Connection between a Vertex|Node 
Node: Vertex interchangeable

Two(2) Types of Graph:
    Directed Graphs
    Undirected Graphs: bidirectional

Vertex = V = [a,b,c,d,e]
Edges = E = [ab,ac,bd,cd,de]    

Represented in Python w/ Adjacency List w/implementation of a dictionary 

graph = {
    a: [b,c],
    b: [a,d],
    c: [a,d],
    d: [b,c,e]
    e: [d]
}

'''

graph = {
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','d'],
    'd':['b','c','e'],
    'e':['d']
}

#vertices 
print(graph.keys())

#edges 
edges = []
for vertex in graph:
    for edge in graph[vertex]:
        if {vertex, edge} not in edges:
            edges.append({vertex,edge})
            
print(edges)
        
#given a specific vertex lets get the edges 
