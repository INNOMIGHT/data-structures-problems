import sys
import os
os.path.abspath('../DataStructuresProblems')
sys.path.append(os.path.abspath('../DataStructuresProblems'))


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


def validate_bst(root, _min=-sys.maxsize, _max=sys.maxsize):
    if root is None:
        return True
    if (
            _min <= root.value <= _max and
            validate_bst(root.left_child, _min, root.value) and
            validate_bst(root.right_child, root.value, _max)):
        return True
    else:
        return False


# Test Case
root = Node(5)
root.left_child = Node(3)
root.right_child = Node(7)
print(validate_bst(root))
