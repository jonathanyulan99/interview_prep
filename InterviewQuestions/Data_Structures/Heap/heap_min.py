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


