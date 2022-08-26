# distance between 2 given nodes in a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findLca(root, node1, node2):
    if root is None:
        return root

    if root.data == node1 or root.data == node2:
        return root

    left = findLca(root.left, node1, node2)
    right = findLca(root.right, node1, node2)

    if left and right:
        return root

    if left != 0:
        return left

    else:
        return right


def find_root_from_ancestor_node(root, data):
    # if we reach beyond leaf node

    if root is None:
        return -1

    if root.data == data:
        return 0

    left = find_root_from_ancestor_node(root.left, data)
    right = find_root_from_ancestor_node(root.right, data)

    distance = max(left, right)

    return distance + 1 if distance >= 0 else -1


def find_distance_between_nodes(root, n1, n2):
    lca = findLca(root, n1, n2)

    return find_root_from_ancestor_node(lca, n1) + find_root_from_ancestor_node(lca, n2) if lca else -1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(find_distance_between_nodes(root, 4, 5))
