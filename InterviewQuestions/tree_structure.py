class tree_node:
    def __init__(self,data):
        ## data is represented whatever way you'd like 
        ## data 
        self.data = data 
        ## children is a list []
        ## tree is a recursive data structure 
        self.children = [] 
        ## parent property stores the parent of the individual parent node
        self.parent = None 
    
    ## no checks for duplicate(s)
    ## simple add_child
    def add_child(self,child):
        ## child is an instance of tree_node class
        ## child that is added, gets its parent set 
        child.parent = self 
        self.children.append(child)
        
    def print_tree(self):
        ## nice little tip to remember based on a function_call() you can add whitespace
        ## ' ' one space
        ## multiplied by the times .get_level() is called
        ## and finally multiplied by the amount of space we'd like here being three
        spaces = ' ' * self.get_level() * 2
        ## ternary operator 
        prefix = spaces + "|---> " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        level = 0
        p = self.parent 
        while p:
            level += 1 
            p = p.parent 
        
        return level 

def build_product_tree():
    root = tree_node("Electronics")
    laptop = tree_node("Laptop")
    laptop.add_child(tree_node("Mac"))
    laptop.add_child(tree_node("Microsoft"))
    phone = tree_node("Phone")
    phone.add_child(tree_node("AT&A"))
    phone.add_child(tree_node("Verizon"))
    tv = tree_node("TV")
    tv.add_child(tree_node("Samsung"))
    tv.add_child(tree_node("LG"))
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    print(tv.get_level())
    return root 

if __name__ == '__main__':
    root = build_product_tree()
    print(root.get_level())
    root.print_tree()
    pass