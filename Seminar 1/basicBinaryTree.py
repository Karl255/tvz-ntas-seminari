class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


def addItem(root, item):
    if not root:
        root = Node(item)
        return root
    if root.value >= item:
        root.left = addItem(root.left, item)
    elif root.value <= item:
        root.right = addItem(root.right, item)

    if root.right and root.left:
        root.height = max(root.right.height, root.left.height) + 1
    elif root.left:
        root.height = root.left.height + 1
    elif root.right:
        root.height = root.right.height + 1
    return root
