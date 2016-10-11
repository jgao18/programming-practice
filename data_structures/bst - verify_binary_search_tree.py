# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    return check(root, float("-inf"), float("inf"))

def check(node, minimum, maximum):
    if node is None:
        return True
    
    if ((node.data <= minimum) or (node.data >= maximum)):
        return False
    else:
        return check(node.left, minimum, node.data) and check(node.right, node.data, maximum)
