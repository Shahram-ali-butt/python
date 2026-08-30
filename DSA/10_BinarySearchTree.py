'''Inorder Traversal of BST prints nodes in increasinng order'''
# Note: Implement deletion with predecessor

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Grouped related functions in a class. Can be used without a class
class BST:
    @staticmethod
    def insert(root, value):
        if root == None:
            return Node(value)
        if root.data == value:
            return root
        if root.data > value:
            root.left = BST.insert(root.left, value)
        else:
            root.right = BST.insert(root.right, value)
        return root

    @staticmethod
    def search(root: Node, value):
        if root == None:
            print("Value not found")
            return
        if root.data == value:
            print("Value was found")
            return
        if root.data > value:
            root.left = BST.search(root.left, value)
        else:
            root.right = BST.search(root.right, value)

    @staticmethod
    def delete(root: Node, value):
        if root == None:
            return root
        elif root.data < value:
            root.right = BST.delete(root.right, value)
        elif root.data > value:
            root.left = BST.delete(root.left, value)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                succ = BST.inorder_successor(root)
                root.data = succ.data
                # print("\nRoot and Root.right", root.data, root.right.data)
                root.right = BST.delete(root.right, succ.data)
        return root
    # =====================================================================
    # Inorder Successor & Predecessor
    # =====================================================================

    @staticmethod
    def inorder_successor(node: Node):
        if node == None:
            return None
        else:
            node = node.right
            while(node != None and node.left != None): node = node.left
            return node

    @staticmethod
    def inorder_predecessor(node: Node):
        if node.left == None or node == None:
            return None
        else:
            node = node.left
            while(node.right != None): node = node.right
            return node

    # =====================================================================
    # Different Types of Traversal
    # =====================================================================

    @staticmethod
    def inorder(root: Node):
        if root != None:
            BST.inorder(root.left)
            print(root.data, end=" ")
            BST.inorder(root.right)

    @staticmethod
    def preorder(root: Node):
        if root != None:
            print(root.data, end=" ")
            BST.preorder(root.left)
            BST.preorder(root.right)
    
    @staticmethod
    def postorder(root: Node):
        if root != None:
            BST.postorder(root.left)
            BST.postorder(root.right)
            print(root.data, end=" ")

# =====================================================================
# Usage
# =====================================================================

'''
            20
        ----------
        |        |
        15       30
     -------     -----
     |     |         |
    12     18        40     
'''
root = BST.insert(None, 20)
BST.insert(root, 15)
BST.insert(root, 30)
BST.insert(root, 40)
BST.insert(root, 12)
BST.insert(root, 18)
# BST.insert(root, 16)

# BST.inorder(root) # print in increasing order
# print("\n",root.data) # Print root

## Search for element in a tree
# BST.search(root, 18)
# BST.search(root, 123)

## Inorder successor and predecessor
# print(BST.inorder_successor(root.left).data)
# print(BST.inorder_predecessor(root.left).data)

## Deletion
# BST.delete(root, 18)
# BST.inorder(root)
