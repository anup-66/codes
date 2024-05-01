def bst(node):
    if node.right==None and node.left==None:
        print(node.val)
        return
    bst(node.left)
    bst(node.right)