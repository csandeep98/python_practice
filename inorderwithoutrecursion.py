# print the inorder BST without using recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return

    stack = []
    curr = root
    while curr is not None or len(stack) > 0:
        while curr != None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.data)

        curr = curr.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(inorder(root))
