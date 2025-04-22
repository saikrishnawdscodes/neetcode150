# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# TC : O(n)
# SC - O(n) - recursion stack

# Logic : you reverse the left and right subtree nodes - recursively all the way to the end.


# Beautiful freaking explanation from Gemini : 
# ================================================
# ================================================

# Let's break down how the recursion works in this invertTree solution, identify the break condition, and analyze its time and space complexity.

# How the Recursion Works:

# The invertTree function works by applying the "inversion" operation at each node of the binary tree. Here's a step-by-step breakdown of how the recursion unfolds:

# Initial Call: The function is initially called with the root of the binary tree.

# Base Case (Break Condition):

# Python

# if not root:
#     return None
# This is the crucial break condition for the recursion. If the current root is None (meaning we've reached beyond a leaf node or the initial tree was empty), the function simply returns None. This stops the recursive calls down that path.

# Swap Children:

# Python

# temp = root.left
# root.left = root.right
# root.right = temp
# For the current root node, this block of code swaps its left and right children. This is the core operation of inverting a tree at a single node.

# Recursive Calls:

# Python

# self.invertTree(root.left)
# self.invertTree(root.right)
# After swapping the children of the current root, the function recursively calls itself on the left child (root.left) and then on the right child (root.right).

# self.invertTree(root.left): This call will repeat the same process for the subtree rooted at the original right child (which is now the left child after the swap). It will go down the left subtree, swapping children at each node until it hits the base case (None).
# self.invertTree(root.right): Similarly, this call will repeat the process for the subtree rooted at the original left child (which is now the right child after the swap), going down the right subtree and swapping children.
# Return Root:

# Python

# return root
# After the recursive calls for both left and right subtrees have completed (meaning the entire subtree rooted at the current root has been inverted), the function returns the (now inverted) root node. This return value is then used by the calling function (its parent in the recursion).

# Think of it like a depth-first traversal:

# The recursion goes down the tree, processing each node. When it reaches a leaf or a None node, it starts to return. As it returns up the call stack, the swaps performed at each level accumulate, eventually inverting the entire tree.

# Example:

# Consider a simple tree:

#     1
#    / \
#   2   3
# invertTree(1) is called.
# root is not None. Swap 1.left (2) and 1.right (3). Tree becomes:
#     1
#    / \
#   3   2
# invertTree(3) is called.
# root (now 3) is not None. Swap 3.left (initially None) and 3.right (initially None). No change.
# invertTree(None) is called (from 3.left). Returns None.
# invertTree(None) is called (from 3.right). Returns None.
# invertTree(3) returns 3.
# invertTree(2) is called.
# root (now 2) is not None. Swap 2.left (initially None) and 2.right (initially None). No change.
# invertTree(None) is called (from 2.left). Returns None.
# invertTree(None) is called (from 2.right). Returns None.
# invertTree(2) returns 2.
# invertTree(1) returns 1 (the root of the now inverted tree).
# The final inverted tree is:

#     1
#    / \
#   3   2
# Time Complexity:

# The function visits each node in the binary tree exactly once. For each node, it performs a constant amount of work (swapping the left and right children).
# Therefore, the time complexity is O(N), where N is the number of nodes in the binary tree.
# Space Complexity:

# The space complexity of a recursive algorithm 1  is determined by the maximum depth of the recursion stack. In the case of a binary tree traversal (like this inversion), the depth of the recursion stack is related to the height of the tree.   
# 1.
# github.com
# github.com

# Worst Case (Skewed Tree): If the binary tree is heavily skewed (like a linked list), the height of the tree can be equal to N (the number of nodes). In this case, the recursion stack can go as deep as N, leading to a space complexity of O(N).

# 1
#  \
#   2
#    \
#     3
# For this tree, the recursive calls would be invertTree(1), invertTree(2), invertTree(3), invertTree(None). The stack depth is proportional to the number of nodes.

# Best Case (Balanced Tree): If the binary tree is balanced (like a complete binary tree), the height of the tree is approximately log₂(N). In this case, the maximum depth of the recursion stack would be proportional to the height, leading to a space complexity of O(log N).

#     2
#    / \
#   1   3
# The recursion depth here is much smaller compared to a skewed tree.

# In summary, the space complexity due to the recursive call stack is:

# O(N) in the worst case (skewed tree).
# O(log N) in the best case (balanced tree).
# When discussing the space complexity of tree algorithms using recursion, it's important to specify the worst-case scenario, which is often assumed unless stated otherwise. Therefore, the space complexity is typically considered O(H), where H is the height of the tree. In the worst case, H = N, and in the best case, H = log N.

# Therefore:

# Time Complexity: O(N)
# Space Complexity: O(H), which is O(N) in the worst case (skewed tree) and O(log N) in the best case (balanced tree) due to the recursion stack.