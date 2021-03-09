
"""
Problem Statement
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete
the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def to_list(head):
    node = head
    new_list = []
    while node:
        new_list.append(node.value)
        node = node.next
    print(new_list)
    return head


def create_ll(value):
    head = Node(value[0])
    node = head
    for data in value[1:]:
        node.next = Node(data)
        node = node.next
    return head


def retain_i_skip_j(head, i, j):
    trim_link_list = None
    node = head
    flag = 0
    while node:
        for rounds in range(i):
            if node.value == head.value:
                trim_link_list = Node(head.value)
            else:
                while trim_link_list.next:
                    trim_link_list = trim_link_list.next
                trim_link_list.next = Node(node.value)
                node = node.next
                # node = node.next
        for data in range(j):
            node = node.next
        node = node.next
    return trim_link_list


head = create_ll([1, 2, 6, 8, 3, 4, 5, 6])
to_list(head)
print("8" * 100)
to_list(retain_i_skip_j(head, 1, 4))