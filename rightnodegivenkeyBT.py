# program to print the right node of a given tree in Binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def RightNode(root, value, level):
    if root is None:
        return

    if root.data == value:
        desiredlevel = level
        return None

    if desiredlevel != 0:
        if level == desiredlevel:
            return root

    left = RightNode(root.left, value, level+1)

    if left is not None:
        return left

    return RightNode(root.right, value, level+1)


root = Node(10)
root.left = Node(2)
root.right = Node(6)
root.right.right = Node(5)
root.left.left = Node(8)
root.left.right = Node(4)

RightNode(root, 10, 0)
