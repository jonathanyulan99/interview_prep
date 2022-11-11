# The node values are stores such that all the parent nodes occur in the first half of the list 
# index_of_parent_nodes <= floor(total_nodes-1/2)
# the leaves exist in the rest of the list ... index_of_children_nodes > floor(total_nodes-1/2)

# list of n = 10 
# parents_nodes must exist in () <=floor(10-1/2)
# parent_nodes exist in 0-4
# Last Parent is @ floor(n-1/2) index

# children nodes must exist in () > floor(10-1/2)
# chilren_nodes exist in 5-9 ** remember index 0
# First Child is @ floor(n-1/2) + 1 index 

# Left Child at index Z is 2(Z) + 1 
# Right Child at index Z is 2(Z) + 2 

#           0  1  2  3  4  5  6  7  8  9 
# list = [100,60,80,30,50,70,75,20,10,40]
# N = 9
# Parents are 100,60,80,30,50 or <=(floor(9-1/2)) or <=4 or [O-4]
# Children are 70,75,20,10,40 or >(floor(9-1/2)) or >4 or [5 or 9]

# Heaps Are Not Sorted 
# Heaps are Complete Binary Trees
# THE ONLY key condition that a Heap follows is that the largest or smallest element is always placed at the top

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self,val:int):
        self.heap.append(val)
        self._percolateDown(len(self.heap)-1)
    
    def getMin(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def removeMin(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self._minHeapify(0)
            return min 
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min 
        else:
            return None 
                
    def _percolateDown(self,index:int):
        parent = (index-1)//2
        # base case
        # we are at the root already
        if index <= 0:
            return
        elif self.heap[index] < self.heap[parent]:
            # if smaller swap parent for index/child...now parent is new index/child
            # recursively call parent 
            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            self._percolateDown(parent)
            
    
    def _minHeapify(self,index:int):
        l_child = (2*index)+1
        r_child = (2*index)+2
        smallest = index
        if len(self.heap) > l_child and self.heap[l_child] < self.heap[smallest]:
            smallest = l_child
        if len(self.heap) > r_child and self.heap[r_child] < self.heap[smallest]:
            smallest = r_child
        if smallest != index:
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            self._minHeapify(smallest)
    
    def _buildHeap(self,arr:list):
        self.heap = arr 
        for i in range(len(self.heap)-1,-1,-1):
            self._minHeapify(i)
            
heap = MinHeap()
values = [8, 2, 9, 6, 1, 3, 5]
for value in values:
    heap.insert(value)
print(heap.getMin())
print(heap.heap)
heap2 = MinHeap()
heap2._buildHeap(values)
print(heap2.getMin())
print(heap2.heap)
