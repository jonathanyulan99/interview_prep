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

# Max heaps follow the `MAX-HEAP` property which means that the key/value at the parent node is always greater than the keys/values at the child nodes
# Heaps implemented via lists or using node/tree classses
# List are more space-efficient

class MaxHeap:
    def __init__(self):
        # contain the values of the heap
        self.heap = []

    # O(log(N)) -> maximum number or nodes that need to be swapped or traversed
    # appends the given value to the heap lists
    # function will swap the values at parent-child nodes until the heap property is restored
    def insert(self, val):
        self.heap.append(val)
        # append to the back, start from the back
        self.__percolateUp(len(self.heap)-1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if self.heap and len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            # delete the last input in our heap that was swapped
            del self.heap[-1]
            self._maxHeapify(0)
            return max
        elif self.heap and len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    # meant to be private method *Not enoforceable in Python*
    # restore the heap property going up from a given node to the root
    # index -> root
    def __percolateUp(self, index):
        parent_index = (index)-1//2
        if index <= 0:
            return
        # is the parent node currently smaller than the children node inserted
        elif self.heap[parent_index] < self.heap[index]:
            # store in temp variable
            tmp = self.heap[parent_index]
            # initiate the swap
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = tmp
            # recursively call and traverse by going to the parent index
            self.__percolateUp(self, parent_index)

    # meant to be private method *Not enoforceable in Python*
    # restore the heap property starting from a given node to the leaves
    # index -> leaves
    def _maxHeapify(self, index):
        left_child = 2*index + 1 
        right_child = 2*index + 2 
        parent = index 
        if len(self.heap) > left and self.heap[parent] < self.heap[left_child]:
            parent = left_child 
        if len(self.heap) > right and self.heap[parent] < self.heap[right_child]:
            parent = right_child
        if parent != index:
            # swap
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp 
            self._maxheapify(parent) 


heap = MaxHeap()
