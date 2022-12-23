from node import Node

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#        A
#    B      C
#  D   E      F


'''Given a root node of the binary tree; I want you to depth-first-traversal to some collection and then print it out the values.

Depth-First-Traversal the key-takeaway is that you must go DEEPER first before going laterally across the tree. The A -> B -> D (bottom out) -> e -> c -> f. Depth First Search Utilizes a Stack, can only add/remove to the top fo the stack (Last-In-First-Out).'''


def depth_first_print_itr(root):
    '''Iterative Solution#1'''
    # linear data structure to keep track of the right, left children to visit before you visit a possible horizontal/sibling node
    if not root:
        return []
    stack = [root]
    result = []

    while len(stack) > 0:
        current_node = stack.pop()
        result.append(current_node.value+'-->')
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return result


print(*depth_first_print_itr(a))
print(depth_first_print_itr(None))

'''Recursive Solution'''
def depth_first_print_recursive(root):
    if not root:
        return []
    # sub tree values 
    right_sub_tree = depth_first_print_recursive(root.right)
    left_sub_tree = depth_first_print_recursive(root.left)
    # *right_sub_tree is an array of the recursive calls to get the subtrees 
    # * using this operator helps unpack the arrays 
    return [root.value,*right_sub_tree,*left_sub_tree]
    

print(depth_first_print_itr(a))

# differencing for unpacking an array in a list or collections data structure 
peeps = ['phelipe','phillip','josh','abby']
newPeeps = ['alvin', peeps, 'brian']
newPeeps = ['alvin',*peeps,'brian']
print(newPeeps)