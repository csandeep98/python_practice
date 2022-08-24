class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowcommonancestor(root, data1, data2):
    if root is None:
        return 0

    if root.data == data1 or root.data == data2:
        return root.data

    left = lowcommonancestor(root.left, data1, data2)
    right = lowcommonancestor(root.right, data1, data2)

    if left != 0 and right != 0:
        print('LCA IS : ', root.data)

    if left != 0:
        return left

    elif right != 0:
        return right

    else:
        return 0


root = Node(12)
root.left = Node(4)
root.right = Node(25)
root.left.left = Node(13)
root.left.right = Node(9)
root.right.left = Node(16)
root.right.right = Node(32)
root.left.left.left = Node(2)
root.left.right.left = Node(26)
root.left.right.right = Node(22)

lowcommonancestor(root, 2, 22)
