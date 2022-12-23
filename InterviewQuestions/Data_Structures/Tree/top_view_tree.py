class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None 
        self.level = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    

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
            mp[root.level] = root.info 
        
        if root.left:
            root.left.level = root.level - 1 
            queue.append(root.left)
        
        if root.right:
            root.right.level = root.level + 1
            queue.append(root.right)
    
    for key,value in sorted(mp):
        print(value,end=' ')