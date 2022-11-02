from avl_node import avlNode
'''AVL Tree is a Binary Search Tree such that for every internal node v of the tree T, the heights of v's children can differ at most by 1.\
   To put it simply, for each Node, the height of the left and right subtrees in an AVL Tree can differ at most by one or the tree is `balanced`.

   In case of binary search trees, the time complexity of all three basic operations, Insertion, Deletion, and Search, take O(h)time, where “h” is the height of the Binary Search Tree. The worst case time complexity is O(n), for skewed BSTs, where “n” is the number of nodes in the tree.

   However, in the best case, when the tree is completely balanced, the time complexity for basic operations is O(log(n)).

   A valid AVL Tree follows the property of each node having a difference of height of thier subtrees at most being one.

   Unbalanced AVL Tree -> the tree has a node which has a left-right subtree height difference greater (>1) than one.

   node u - unbalanced node
   node c - child node of node u
   node g - grandchild node of node u

   Insertion
   Case1:Left-Left:Node C is the left-child of Node U, and Node G is left-child of Node C:Rotate Node U to the Right

   Case2:Left-Right:Node C is the left-child of Node U, and Node G is the right-child of Node C:Rotate Node C to the Left then Rotate Node U to the Right

   Case3:Right-Right:Node C is the right-child of Node U, and Node G is the right-child of Node C:Rotate Node U to the Left

   Case4:Right-Left:Node C is the right-child of Node U, and Node G is the left-child of Node C:Rotate Node C to the Right then Rotate Node U to the Left

   Deletion
   '''

class avlTree:

      def insert(self, root, value):
            if not root:
               return avlNode(value)
            elif value < root.value:
                   root.leftChild = self.insert(root.leftChild, value)
            else:
                   root.rightChild = self.insert(root.rightChild, value)

            # update height
            # height of root node or height of the tree
            root.height = 1 + max(self.getHeight(root.leftChild),self.getHeight(root.rightChild))

            # balance factor
            balance = self.getBalance(root)

            # if Unbalanced
            # Case 1 left-left
            # Unbalanced Node rotate Right
            if balance > 1 and value < root.leftChild.value:
                  return self.rightRotate(root)

            # Case 2 right-right
            # Unbalanced Node rotate Left
            if balance < -1 and value > root.rightChild.value:
                  return self.leftRotate(root)

            # Case 3 left-right
            # Child Node of Unbalanced Node Rotates Left, and Unbalanced Node Rotates Right
            if balance > 1 and value > root.leftChild.value:
                  root.leftChild = self.leftRotate(root.leftChild)
                  return self.rightRotate(root)

            # Case 4 Right-Left
            # Children Node of Unbalanced Node Rotates Right and then Unbalanced Node rotates Left
            if balance < -1 and value < root.rightChild.value:
                  root.rightChild = self.rightRotate(root.rightChild)
                  return self.leftRotate(root)

            return root

      def leftRotate(self,node):
             
             #new root is right now 
             right = node.rightChild
             left_rightNode = right.leftChild
             
             right.leftChild = node
             node.rightChild = left_rightNode
             
             node.height = 1 + max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))
             right.height = 1 + max(self.getHeight(right.leftChild),self.getHeight(right.rightChild))
             
             return right
      
      def rightRotate(self,node):
             
             #new root is left now 
             left = node.leftChild
             right_leftNode = left.rightChild
             
             left.rightChild = node 
             node.leftChild = right_leftNode
             
             node.height = 1 + max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))
             left.height = 1 + max(self.getHeight(left.leftChild),self.getHeight(left.rightChild))
             
             return left

      def getHeight(self,node):
            if not node:
               return 0
            else:
               return node.height 
      
      def getBalance(self,node):
            if not node:
               return 0
            else:
               return self.getHeight(node.leftChild) - self.getHeight(node.rightChild)
      
      def preOrder(self,node):
            if not node:
               return 
                
            print(node.value,end="-")
            self.preOrder(node.leftChild)
            self.preOrder(node.rightChild)

      def postOrder(self,node):
            if not node:
               return 
               
            self.postOrder(node.leftChild)
            self.postOrder(node.rightChild)
            print(node.value,end="-")
            
      def inOrder(self,node):
            if not node:
               return 
               
            self.inOrder(node.leftChild)
            print(node.value,end="-")
            self.inOrder(node.rightChild)

myTree = avlTree()
root = None 

root = myTree.insert(root,10)
root = myTree.insert(root,20)
root = myTree.insert(root,30)
root = myTree.insert(root,40)
root = myTree.insert(root,50)
root = myTree.insert(root,25)

myTree.preOrder(root)
print('\n')
myTree.postOrder(root)
print('\n')
myTree.inOrder(root)
             
          
                
                 