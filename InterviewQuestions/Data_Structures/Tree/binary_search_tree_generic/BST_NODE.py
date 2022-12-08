from random import randint

class BST_NODE:
    # constructor to initialize a BST_NODE
    def __init__(self,val):
        self.val = val
        # sets parent to `None`
        self.parent = None  
        # sets children to `None`
        self.leftChild = None
        self.rightChild = None 

    # insert implementation Iteratively 
    def insert_it(self,val):
        # originally root of the BST tree
        current = self
        # root has no parent nodes
        parent = None 
        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild
        
        if(val < parent.val):
            parent.leftChild = BST_NODE(val)
            parent.leftChild.parent = parent
        else:
            parent.rightChild = BST_NODE(val)
            parent.rightChild.parent = parent
        
    def insert_rec(self,val):
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert_rec(val)
            else:
                self.leftChild = BST_NODE(val)
                self.leftChild.parent = self
                return
        else:
            if self.rightChild:
                self.rightChild.insert_rec(val)
            else:
                self.rightChild = BST_NODE(val)
                self.rightChild.parent = self
                return 
    
    # search value iterative solution
    # 1.set the current node equal to root
    # 2.if the value is < `current node's value` move to left-sub-tree otherwise move to right-sub-tree
    # 3.repeat until the value at the `current node's value` == val or it becomes `None`
    # 4.return the `current_node` 
    def search_it(self,val):
        # Step 1
        current_node = self
        # Step 3
        while current_node:
            # step 3
            if current_node.val == val:
                # step 4
                print("Found "+ str(current_node.val)+" in BST!")
                return True 
            # step 2
            elif val < current_node.val:
                current_node = current_node.leftChild
            # step 2 
            else:
                current_node = current_node.rightChild
        # step 4 -- if not found
        print("Did not find "+ str(val)+" in BST!") 
        return False 
        
    # search value recursive solution
    def search_rec(self,val):
        if val < self.val:
            if self.leftChild:
                return self.leftChild.search_rec(val)
            else: 
                print("Did not find "+ str(val)+" in BST!")
                return False 
        elif val > self.val:
            if self.rightChild:
                return self.rightChild.search_rec(val)
            else:
                print("Did not find "+ str(val)+" in BST!")
                return False 
        else:
            print("Found "+ str(self.val)+" in BST!")
            return True 

    def delete(self,val):
        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val)+" Not Found!")
                return False 
        elif val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val)+" Not Found!")
                return False 
        else:
            # leaf node case
            if not self.leftChild and not self.rightChild:
                self = None
                return self
            # Only right child
            elif not self.leftChild:
                self = self.rightChild
                return self
            # Only left child
            elif not self.rightChild:
                self = self.leftChild
                return self
            # Node has left and right children
            # Navigate the left-sub-tree return the max value(right most node)
            # Navigate the right-sub-tree return the min value(left most node)
            # Utilize randomint from random
            else:
                choice = randint(0,1)
                # navigate left-sub-tree
                if choice == 0:
                    node = self.leftChild
                    while node.rightChild:
                        node = node.rightChild
                    self.val = node.val 
                    self.leftChild = self.leftChild.delete(self.val)
                else:
                    node = self.rightChild
                    while node.leftChild:
                        node = node.leftChild
                    self.val = node.val
                    self.rightChild = self.rightChild.delete(node.val)
        return self
    
    def is_leaf(self):
        if not self.leftChild and not self.rightChild:
            return True 
        else:
            return False
        