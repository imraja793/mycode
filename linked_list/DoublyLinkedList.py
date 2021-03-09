class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def traverse_list(self, node):
        current_node = node
        while current_node is not None:
            print(current_node.previous, "     ", current_node.value, "     ", current_node.next)
            current_node = current_node.next


# obj = Node(1)
# obj.next = Node(2)
# obj.next.next = Node(3)
# obj.next.previous = obj
# obj.next.next.previous = obj.next
#
# obj.traverse_list(obj)

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.previous = a
b.next = c
c.previous = b

a.traverse_list(a)

