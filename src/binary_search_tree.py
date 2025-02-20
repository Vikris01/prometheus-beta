class TreeNode:
    def __init__(self, key):
        """
        Initialize a new tree node with a given key.
        
        :param key: The value/key of the node
        """
        self.key = key
        self.left = None
        self.right = None

def insert_bst(root, key):
    """
    Insert a new node with the given key into a binary search tree.
    
    :param root: The root of the binary search tree (or subtree)
    :param key: The key to be inserted
    :return: The root of the updated binary search tree
    """
    # If the tree is empty, create a new node
    if root is None:
        return TreeNode(key)
    
    # Otherwise, recursively insert into the appropriate subtree
    if key < root.key:
        # If key is less than current node, insert in the left subtree
        root.left = insert_bst(root.left, key)
    elif key > root.key:
        # If key is greater than current node, insert in the right subtree
        root.right = insert_bst(root.right, key)
    
    # If key is equal to current node's key, do nothing (no duplicates)
    return root

def inorder_traversal(root):
    """
    Perform an inorder traversal of the binary search tree.
    
    :param root: The root of the binary search tree
    :return: List of keys in sorted order
    """
    result = []
    
    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append(node.key)
            _inorder(node.right)
    
    _inorder(root)
    return result