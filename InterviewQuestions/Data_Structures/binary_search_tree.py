'''
BSTree Requirements:
    Every Node has at Most 2 Children Nodes *Same as Binary Tree*
    Every Value in left subtree at EVERY NODE is less
    Every Value in right subtree at Every Node is greater
    NO DUPLICATE VALUES ARE ALLOWED (ALL ELEMENTS ARE UNIQUE)

Search Complexity Of A BST:
    Every iteration we reduce the search space by 1/2
    
    if N = 8 : 8->4->2->1 
    Versus O(N): 8->7...->1
    
    log 8 = 3 *Base 2* 
    O(log N)

'''

class BSTNode:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


    