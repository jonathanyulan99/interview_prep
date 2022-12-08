class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data == None:
            self.data = data
            
        else:
            if data < self.data:
                if self.left is None: 
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
                    
def in_order_print(root):
    if root is None:
        return 
    else:
        in_order_print(root.left)
        print(root.data)
        in_order_print(root.right)

def pre_order_print(root):
    if root is None:
        return 
    else:
        print(root.data)
        pre_order_print(root.left)
        pre_order_print(root.right)

def post_order_print(root):
    if root is None:
        return 
    else:
        post_order_print(root.left)
        post_order_print(root.right)
        print(root.data)

root = TreeNode(30)
root.insert(20)
root.insert(15)
root.insert(25)
root.insert(5)
root.insert(18)
root.insert(40)
root.insert(35)
root.insert(50)
root.insert(45)
root.insert(60) 

#in_order_print(root)
#pre_order_print(root)
post_order_print(root)