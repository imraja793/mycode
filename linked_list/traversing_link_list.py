class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def traverse_list(self, node):
        current_node = node
        while current_node is not None:
            print(current_node.value, current_node.next)
            current_node = current_node.next

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

head.traverse_list(head)