class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.next = None


def printlevel(root):
    h = height(root)
    for i in range(1, h+1):
        printcurrlevel(root, i)


def printcurrlevel(root, level):
    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")

    if level > 1:
        printcurrlevel(root.left, level-1)
        printcurrlevel(root.right, level-1)


def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    if lheight > rheight:
        return lheight + 1

    else:
        return rheight + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printlevel(root)
