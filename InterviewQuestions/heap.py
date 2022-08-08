'''

Every parent node, at most, can have only 2 children

Must be a complete tree. It must be filled from left to right and every level must be full, with the exception off the last level not needing to be full

Min-Heap: Every Parent's key must be smaller than its children nodes
Max-Heap: Every Parent's ky must be larger tahn its children nodes

'''
import sys
class heap: 
    def __init__(self,size_limit):
        self.current_size = 0 
        self.heap = [0]*(size_limit+1)
        self.heap[0] = (sys.maxsize+1)
        self.root = 1 

    def swap_nodes(self,node1,node2):
        self.heap[node1],self.heap[node2] = self.heap[node2],self.heap[node1]
        
    
        
    def get_root(self):
        return self.root 
    

    
    class heap_node:
        def __init__(self,data):
            self.data = data
            self.left = None 
            self.right = None
            
        def get_value(self):
            return self.data 
        
        def get_left(self):
            return self.left
        
        def get_right(self):
            return self.right 
        
        def set_left(self,value):
            self.left = value 
            
        def set_right(self,value):
            self.right = value 
            
        