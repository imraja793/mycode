class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        else:
            previous_head = self.head
            self.head = Node(value)
            self.head.next = previous_head
        return

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

        return node

    def search(self, value):
        if self.head is None:
            return None
        node = self.head

        while node.next:
            if node.next.value == value:
                print(f"we get the value", value)
                return (node.next)
            node = node.next

    def get_linked_list(self, head):
        if self.head is None:
            return 0
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        else:
            node = self.head
            while node.next:
                if node.next.value == value:
                    node.next = node.next.next
                    return
                node = node.next

    def pop_front(self):
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None
        return

    def pop(self):
        node = self.head.value
        self.head = self.head.next
        return node

    def insert(self, value, position):
        node = self.head
        position_of_node = 0
        if position == position_of_node:
            self.head = Node(value)
            self.head.next = node
            return
        while node:
            previous_node = node
            updated_node = node.next
            if position_of_node == position - 1:
                previous_node.next = Node(value)
                previous_node.next.next = updated_node
                return 0
            node = node.next
            position_of_node += 1
            if node.next is None:
                node.next = Node(value)
                return

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def to_list(self):
        node = self.head
        new_list = []
        while node:
            new_list.append(node.value)
            node = node.next
        return new_list


# obj = LinkedList()
# obj.append(5)
# obj.append(6)
# obj.append(7)
# obj.append(1)
# obj.prepend(7)

# obj.append(4)
# obj.append(3)
# obj.prepend(10)
# obj.get_linked_list(obj)
# obj.search(1)
# obj.search(7)
# obj.search(10)
# obj.remove(7)
# obj.remove(3)
# print('-'*100)
# obj.size()
# obj.to_list()
# obj.insert("raja", 5)
# obj.get_linked_list(obj)

# obj.get_linked_list(obj)
# obj.pop()
# print('-'*100)
# obj.get_linked_list(obj)
# obj.pop_front()
# obj.insert(8, 2)
# print('-'*100)
# obj.get_linked_list(obj)


if __name__ == '__main__':
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"



