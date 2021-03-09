from DoublyLinkedList import Node


class DoublyNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):

        if self.head is None:
            self.head = DoublyNode(value)
            self.tail = self.head
            return

        self.tail.next = DoublyNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)
node = linked_list.head
while node:
    node = node.next

node = linked_list.tail
while node:
    node = node.previous


