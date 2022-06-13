## binary search tree is each TreeNode has at most two children
## those children on the left side of each Node are less than
## those children on the right side of each Node are greater than
## O(log N) to search for an item due to the splitting at half
## criteria makes it so that no number can be inputted twice and must be unique

##TWO(2) Tyes of Search for Tree(s)
## BREADTH FIRST SEARCH

## DEPTH FIRST SEARCH
    ## in-order traversal
    ## [7,12,14,15,20,23,27,88]
    ## pre-order traversal
    ## [15,12,7,14,27,20,23,88]
    ## post-order traversal 
    ## [7,14,12,23,20,88,27,15]


''''    15
    12       27
  7   14   20    88
            23
'''
## In-Order Traversal 
## base-node 
## root-15 
## node is in-order
## left subtree than yourself than right subtree

## Pre-Order
## node than left subtree than right subtree
## Post-Order 
## left subtree than right subtree than node


from numpy import number


class BinarySearchTreeNode:
    def __init__(self,data):
        ## left child
        self.left = None
        ## right child
        self.right = None
        ## data 
        self.data = data 
    
    def add_child(self,data):
        ## the data already exsist
        if data == self.data:
            return
        
        ## add data in left subtree
        if data < self.data:
            ## need to check if left subtree node exsist
            if self.left:
                self.left.add_child(data)
            ## self does not have a left child so can insert here
            else:
                self.left = BinarySearchTreeNode(data)
        ## add data in the right subtree
        else:
            ## tree node is greater than value and right subtree/node/child exist 
           if self.right:
               ## recursively call the right child w/ self.right.add_child(data) this will go to your right subtree
               ## and tree to recursively add the data in that tree 
               self.right.add_child(data)
           else:
               ## this case is when their is no longer a right child/subtree/node
               ## in that case the right child is the BinarySearchTreeNode(data)
               ## this data has no children and thus its left,right children are instantiated to None
               self.right = BinarySearchTreeNode(data)
    
    ## in_order_traversal is how we can sort in O(log n) time    
    def in_order_traversal(self):
        elements = []
        if self.left:
            ## this self.left is the recursive way to traverse down the tree
            ## recursion ends when the self.left no longer runs
            elements += self.left.in_order_traversal()
            ## visit left, node, right 
            ## lsubtree, node , rsubtree
            
        ## visits the base node after we exit our recursion
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        ## self.data is the node 
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements 
    
    def pos_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.pos_order_traversal()
        if self.right:
            elements += self.right.pos_order_traversal()
        elements.append(self.data)
        return elements 

    def search(self,value):
        ## base case 
        if self.data == value:
            return True 
        
        ## left subtree case 
        if self.data > value:
            if self.left:
                return self.left.search(value)
            else:
                return False 
        if self.data < value:
            if self.right:
                return self.right.search(value)
            else:
                return False 
    
    def find_min(self):
        if self:
            if self.left:
                return self.left.find_min()
            return self.data
        else:
            return None 
    
    def find_max(self):
        if self:
        #     sorted_list = self.in_order_traversal()
        # ## in_order_traversal sorts our list 
        # ## We know that after being sorted greatest max will be found in furthers right subtree Node
        # ##return max(self.in_order_traversal()) --> one liner
        #     return sorted_list[-1]
            if self.right:
                return self.right.find_max()
            return self.data
        else:
            return None 
    
    def calc_sum(self):
        if self:
            return sum(list(self.in_order_traversal()))
        else: 
            return 0 
    
    def is_leaf(self,value):
        if self.data == value:
            if self.left or self.right:
                return False
            else: 
                return True 
        
        ## check before to make sure it's in our tree first
        # returns None when not in tree 
        if self.left==None and self.right==None:
            return None 
        
        #searches and iterates through the left of the nodes 
        #if < then search in left subtree 
        #if > then search in right subtree
        if value < self.data: 
            return self.left.is_leaf(value)
        if value > self.data:
            return self.right.is_leaf(value)
        
        
                
    ## Deletion of node can happen in three cases 
    #1st Case: Deletion of the Node w/no children\
        # remove the node from the original parent.right_child
    #2nd Case: Deletion of the Node w/one child\
        # Replace the child with the removed node 
    #3rd Case: Deletion of the Node w/two children \
        # RebalanceCase requires for the BST properties hold true \
            # 3rd Case: Trickiest; all elements should be unique and for a given node the elements in the left subtree \
                # go to your right_subtree and find the minimum value and then replace it 
                # the node you are trying to delete, you are trying to replace with the minimum\
                    #After just then remove it by keeping all the same data in proper order and unique  
            # 3rd Case: LETS LOOK AT LEFT SUBTREE instead \
                # find the maximum of our left_subtree vs the minimum in our right_subtree example
                # maximum value in the left subtree are going to be less than all the values at that point \
                    # all the leftover elements in the left subtree are still smaller than the replaced node 
    def delete_node(self,val):
        # check to see if the value < self.data which is our starting point or ROOT
        # CASE 1 
        if val < self.data: 
            # check to see if our ROOT has a left child or left subtree 
            if self.left:
                ## assign a new LEFT subtree
                self.left = self.left.delete_node(val)
        elif val > self.data:
            # check for right child|subtree 
            if self.right:
                ## assign a new RIGHT subtree
                self.right = self.right.delete_node(val)
        # else case automatically triggers in python
        # this else case below fires when we find our node which matches our value 
        else:
            # this reaches our last data point 
            if self.left is None and self.right is None:
                return None 
            # here you have right but not left child 
            if self.left is None:
                return self.right
            if self.right is None: 
                return self.right 

            # for CASE 3 
            # rememeber we are looking for the minimum value at the node we are trying to delete 
            # then we resave that data with self.data resaved as our min_value from right subtree
            min_val = self.right.find_min()
            self.data = min_val 
            
            # ****HOW WE DELETE AND REATTACH OUR NEW SUBTREE minus the minimum_value() we took earlier to replace**
            # create a new right subtree 
            self.right = self.right.delete_node(min_val) 
            
            # ALSO FOR CASE 3
            # LEFT SUBTREE ALTERNATIVE METHOD WITH MAX
            # max_value = self.left.find_max()
            # self.data = max_value 
            # self.left = self.left.delete_node(max_value)
        return self 
    
    def delete_node_left(self,value):
        if value < self.data: 
            if self.left:
                self.left = self.left.delete_node_left(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node_left(value)
        else:
            if self.left==None and self.right==None:
                return None
            elif self.left==None:
                return self.right
            elif self.right==None:
                return self.right

            max_value = self.left.find_max()
            self.data = max_value 
            
            self.left = self.left.delete_node_left(max_value)
        return self 
    
            
            
    
 
        
                 

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    numbers_tree_2 = build_tree(numbers)
    print(numbers_tree.search(4))
    print(numbers_tree.search(69))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(sum(numbers))
    print(numbers_tree.calc_sum())
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.pos_order_traversal())
    print(numbers_tree.is_leaf(34))
    print(numbers_tree.is_leaf(99))
    print(numbers_tree.is_leaf(17))
    numbers_tree.delete_node(9)
    numbers_tree_2.delete_node_left(17)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree_2.in_order_traversal())