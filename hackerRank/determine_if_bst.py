import os

from hackerRank.node import node



def check_nodes(node, min_val, max_val):
    if node.value < min_val or node.value > max_val:
        return False
    else:
        if node.left is None and node.right is None:
            return True
        if node.left is None:
            return check_nodes(node.right, node.value, 99999)
        if node.right is None:
            return check_nodes(node.left, -1, node.value)
        return check_nodes(node.left, -1, node.value) and check_nodes(node.right, node.value, 9999)


def traverse(root):
    return check_nodes(root, -1, 9999)


if __name__ == '__main__':
    head = node(100)
    head.left = node(50)
    head.right = node(200)
    head.left.left = node(25)
    head.left.right = node(75)
    head.right.right = node(350)
    print(traverse(head))

