import os

from hackerRank.node import node


def traverse(root):
    cur_queue = []
    next_queue = []
    n = root
    cur_queue.append(n)
    while len(cur_queue) > 0:
        n = cur_queue.pop(0)
        print(str(n.value) + " ",  end="")
        if n.left is not None:
            next_queue.append(n.left)
        if n.right is not None:
            next_queue.append(n.right)
        if len(cur_queue) == 0:
            cur_queue, next_queue = next_queue, cur_queue
            print("")


if __name__ == '__main__':
    head = node(100)
    head.left = node(50)
    head.right = node(200)
    head.left.left = node(25)
    head.left.right = node(75)
    head.right.right = node(350)
    traverse(head)
