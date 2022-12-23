class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None 
        self.level = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        if not self.root:
            self.root = Node(val)
            return self.root 
        
        root = self.root 
        parent = None 
        
        while True:
            parent = root 
            if val < root.value:
                root = root.left 
                if not root:
                    parent.left = Node(val)
                    return root 
            else:
                root =root.right 
                if not root:
                    parent.right = Node(val)
                    return root 

def pre_order(root):
    if not root:
        return 
    print(root.value,end=' ')
    pre_order(root.left)
    pre_order(root.right)

def top_view(root):
    if not root:
        return
    
    queue = []
    mp = {}
    
    root.level = 0 
    
    queue.append(root)
    
    while len(queue) >= 1:
        root = queue.pop(0)
        
        if root.level not in mp:
            mp[root.level] = root.value 
        
        if root.left:
            root.left.level = root.level - 1 
            queue.append(root.left)
        
        if root.right:
            root.right.level = root.level + 1
            queue.append(root.right)
    
    for key in sorted(mp):
        print(mp[key],end=' ')
        
tree = BinarySearchTree()

for val in [1,2,5,3,6,4]:
    tree.insert(val)

pre_order(tree.root)
print()
top_view(tree.root)