class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None 
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0 
        parent = self.parent
        while parent:
            level+=1 
            parent = parent.parent
        return level 
        
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3 
        prefix = spaces + "|-->" if self.parent else "" 
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                child.print_tree()
    
def build_product_tree():
    root = TreeNode("Electronic")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("CellPhone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("vivo"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    print(tv.get_level())
    return root 
        
if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    pass