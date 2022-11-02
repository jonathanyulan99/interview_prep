from BST_NODE import BST_NODE
# BST Tree is a Binary Tree and has the BST Property 
# Binary Tree is a tree in which all the nodes have 0 - 2 children 
# BST Property AllNodeValue(left_SubTree) <= NodeValue(Current_Node) < AllNodeValues(Right_Subtree)
class BST_TREE:
    # constructor to initialize the Binary Search Tree
    def __init__(self,root):
        self.root = BST_NODE(root)
    
    def setRoot(self,value):
        self.root = BST_NODE(value) 
    
    def getRoot(self):
        return self.root
    
    # Start from root
    # check if value to be inserted is greater than the root/current node's value
    # if greater than continue on right subtree, otherwise continue on left subtree
    # repeat until you find a node that has no right/left child to move into 
    # insert the given value there and update the parent node
    # iteratively inserted 
    def insert_it(self,val):
        if self.root:
            self.root.insert_it(val)
        else:
            self.root = BST_NODE(val)
    
    # recursively inserted 
    def insert_rec(self,val):
        if self.root:
            self.root.insert_rec(val)
        else:
            self.root = BST_NODE(val)
            return True 
    
    def search_it(self,val):
        if self.root:
            return self.root.search_it(val)
        else:
            print("Value Not in BST!")
            return False
    
    def search_rec(self,val):
        if self.root:
            return self.root.search_rec(val)
        else:
            print("Value Not in BST!")
            return False 
    
    def delete(self,val):
        if self.root:
            self.root.delete(val)
        else:
            return False
    
    

            