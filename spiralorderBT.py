class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# here the idea is to use 2 stacks to push peek and pop


def printSpiral(root):

    if root is None:
        return
    # create the stacks
    s1 = []
    s2 = []
    # push the root to s1
    s1.append(root)

    while (len(s1) != 0 or len(s2) != 0):
        while(len(s1) != 0):
            n1 = s1[-1]
            s1.pop()
            print(n1.data)
            if n1.right:
                s2.append(n1.right)
            if n1.left:
                s2.append(n1.left)

        while (len(s2) != 0):
            n2 = s2[-1]
            s2.pop()
            print(n2.data)
            if n2.left:
                s1.append(n2.left)
            if n2.right:
                s1.append(n2.right)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(7)
root.left.right = newNode(6)
root.right.left = newNode(5)
root.right.right = newNode(4)
print("Spiral Order traversal of",
      "binary tree is ")
printSpiral(root)
