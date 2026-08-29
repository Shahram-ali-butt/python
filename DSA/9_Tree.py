'''
Array, Linked List, Stack, Queue are Linear Data Structures
Tree and Graphs are Non-Linear data Structures

-- Types of Trees
1) Binary Tree: Maximum number of children of any node are 2
2) Binary Search Tree: Maximum 2 children of each node. The nodes of left sub-tree are smaller 
                       than right sub-tree
3) Strict Binary Tree (Full Binary Tree): Each node can have only 0 or exactly 2 child nodes
4) Complete Binary Tree: Child nodes can be from 0 upto 2. Nodes are attached from left to right. 
                         Next level can't be reached if previous level isn't full.
5) Skew Binary Tree: Just like a LL. Go in a straight line either in left or Right.
                     Sub-Types are Right-Skew and Left-Skew Tree.
6) Degenerate Tree: If nodes are going in a Zig-Zag, it is called a Degenerate Tree.
5) Extended Binary Tree: Even if a B.T is incomplete in some places, it is made a Strict B.T by 
                         adding Dummy Nodes. Moreover, each leaf node is padded with dummy nodes as well.
'''

# DLL Implementation of Tree 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeTraversal:
    @staticmethod
    def preorder(root: Node):
        if root != None:
            print(root.data, end=" ")
            TreeTraversal.preorder(root.left)
            TreeTraversal.preorder(root.right)

    @staticmethod
    def postorder(root: Node):
        if root != None:
            TreeTraversal.postorder(root.left)
            TreeTraversal.postorder(root.right)
            print(root.data, end=" ")

    @staticmethod
    def inorder(root: Node):
        if root != None:
            TreeTraversal.inorder(root.left)
            print(root.data, end=" ")
            TreeTraversal.inorder(root.right)

'''
        Test Tree
            1
        ---------
        |       |
        3       5
     -------     ----
     |     |        |
     2     4        8
'''

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

TreeTraversal.preorder(root)
print()
TreeTraversal.postorder(root)
print()
TreeTraversal.inorder(root)
        