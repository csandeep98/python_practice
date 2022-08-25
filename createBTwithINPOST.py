

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def Utilfunc(inorder, post, start, end):
    global mp, index

    if start > end:
        return None

    current = post[index]
    node = Node(current)
    index -= 1

    if start == end:
        # this means that the node has no children
        return node

    Iindex = mp[current]

    node.right = Utilfunc(inorder, post, index+1, end)
    node.left = Utilfunc(inorder, post, start, index-1)

    return node


def buildTree(inorder, post, lenn):
    global index

    for i in range(lenn):
        mp[inorder[i]] = i

    index = lenn - 1

    return Utilfunc(inorder, post, 0, lenn-1)


def preOrder(node):

    if (node == None):
        return

    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


inorder = [4, 8, 2, 5, 1, 6, 3, 7]
post = [8, 4, 5, 2, 6, 7, 3, 1]
n = len(inorder)
mp, index = {}, 0

root = buildTree(inorder, post, n)

print("Preorder of the constructed tree :")

preOrder(root)
