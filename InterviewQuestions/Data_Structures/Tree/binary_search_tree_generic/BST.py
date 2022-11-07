from BST_TREE import BST_TREE

def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

'''When Using The Printing Traversals We Only Want to Change the Location of the print statement; it is always leftChild, rightChild...the printing only changes\
    in placement of the code pre-1st, in-2nd , and post-3rd'''

# print current node
# call preOrder() on left-sub-tree
# call preOrder() on post-sub-tree
def preOrderPrint(node):
    if node:
        print(node.val,end= "--")
        preOrderPrint(node.leftChild)
        preOrderPrint(node.rightChild)

# call postOrder() on left-sub-tree
# call postOrder() on right-sub-tree
# print current node
def postOrderPrint(node):
    if node:
        postOrderPrint(node.leftChild)
        postOrderPrint(node.rightChild)
        print(node.val, end = "--")

# call inOrderPrint() on left-sub-tree
# print current node value
# call inOrderPrint() on right-sub-tree
def inOrderPrint(node):
    if node:
        inOrderPrint(node.leftChild)
        print(node.val, end= '--')
        inOrderPrint(node.rightChild)

def smallestValue(root):
    while root.leftChild:
        root = root.leftChild
    return root.val

def largestValue(root):
    while root.rightChild:
        root = root.rightChild
    return root.val

def middleValue(root):
    return root.val  
        
bst = BST_TREE(6)
print("ROOT:", bst.root.val)
bst.insert_it(4)
bst.insert_it(9)
bst.insert_it(5)
bst.insert_it(2)
bst.insert_it(8)
bst.insert_it(12)
bst.insert_rec(15)
bst.insert_rec(17)
bst.insert_rec(1)
display(bst.root)
display(bst.root)
preOrderPrint(bst.root)
print('\n')
postOrderPrint(bst.root)
print('\n')
inOrderPrint(bst.root)
print('\n')
print(bst.search_it(8))
print(bst.search_rec(8))
print(bst.getRoot().val)
print(smallestValue(bst.getRoot()))
print(largestValue(bst.getRoot()))
print(middleValue(bst.getRoot()))
print(bst.getRoot().leftChild.leftChild.is_leaf())
print(bst.getRoot().leftChild.is_leaf())
print(bst.getRoot().rightChild.rightChild.is_leaf())
print(bst.getRoot().rightChild.is_leaf())
print(bst.get_height(bst.getRoot()))