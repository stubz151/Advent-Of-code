from collections import defaultdict

from hackerRank.random_node import random_node


def clone_list(head):
    dict = defaultdict(lambda: random_node(0))
    dict[None] = None
    x = head
    while x:
        dict[x].value = x.value
        dict[x].next = dict[x.next]
        dict[x].random = dict[x.random]
        x = x.next
    return dict[head]


if __name__ == '__main__':
    head = random_node(0)
    head.next = random_node(1)
    head.next.next = random_node(2)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next
    cloned = clone_list(head)
    x = cloned
    while x:
        print(x.value)
        x = x.next
