import pytest
from src.binary_search_tree import TreeNode, insert_bst, inorder_traversal

def test_insert_into_empty_tree():
    """Test inserting into an empty tree."""
    root = None
    root = insert_bst(root, 5)
    assert root.key == 5
    assert root.left is None
    assert root.right is None

def test_insert_multiple_elements():
    """Test inserting multiple elements maintaining BST properties."""
    root = None
    keys = [5, 3, 7, 1, 4, 6, 8]
    for key in keys:
        root = insert_bst(root, key)
    
    # Check inorder traversal to verify BST property
    assert inorder_traversal(root) == [1, 3, 4, 5, 6, 7, 8]

def test_insert_duplicate_elements():
    """Test that duplicate elements are not added."""
    root = None
    root = insert_bst(root, 5)
    root = insert_bst(root, 5)
    
    # Check that only one element exists
    assert inorder_traversal(root) == [5]

def test_insert_left_subtree():
    """Test inserting elements in the left subtree."""
    root = None
    root = insert_bst(root, 5)
    root = insert_bst(root, 3)
    root = insert_bst(root, 1)
    
    assert root.key == 5
    assert root.left.key == 3
    assert root.left.left.key == 1

def test_insert_right_subtree():
    """Test inserting elements in the right subtree."""
    root = None
    root = insert_bst(root, 5)
    root = insert_bst(root, 7)
    root = insert_bst(root, 9)
    
    assert root.key == 5
    assert root.right.key == 7
    assert root.right.right.key == 9