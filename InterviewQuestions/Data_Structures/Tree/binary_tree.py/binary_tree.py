'''
Binary Tree: 1) At Most 2 children per node 2) exactly 1 root 3) exactly 1 path b/w root and any node
'''
from node import Node 

class BinaryTree:
    def __init__(self,root):
        self.root = root
        

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 

#       A 
#    B     C
#  D  E     F
