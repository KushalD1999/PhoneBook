from node import Node


class SingleLinkedList:

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __str__(self):
        result = ""
        curr = self._head
        while curr:
            result += str(curr.get_element()) + "-->"
            curr = curr.get_next()
        return result[:-3]

    def _set_list(self, head, tail, size):
        self._head = head
        self._tail = tail
        self._size = size

    # def __set_list(self, node_list_head):
    #     self._head = node_list_head
    #     self._list_size = 0
    #     curr = node_list_head
    #     while curr.get_next():
    #         curr = curr.get_next()
    #         self._list_size += 1
    #     self._tail = curr

    # existing methods below

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def set_head(self, head):
        self._head = head

    def set_tail(self, tail):
        self._tail = tail

    def is_empty(self):
        return self._size == 0 and not self._head and not self._tail

    def size(self):
        return self._size

    def add_first(self, element):
        node = Node(element, self._head)
        self._head = node
        if self._size == 0:
            self._tail = node
        self._size += 1

    def add_last(self, element):
        if self._size == 0:
            self.add_first(element)
        else:
            node = Node(element)
            self._tail.set_next(node)
            self._tail = node
            self._size += 1

    def remove_first(self):
        element = None
        # if SLL is not empty
        if (self._head is not None):
            # get the first node
            node = self._head
            # let head point to the second node
            self._head = self._head.get_next()
            # decrement the size
            self._size -= 1
            # set the _next of previous head to point to None (for garbage collection purpose)
            node.set_next(None)
            # get the element stored in the node
            element = node.get_element()
        # return the element of the removed node
        return element
