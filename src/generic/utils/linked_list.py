class LinkedList(object):

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.__ptr = None
        self.current = None
        self.first = None
        self.last = None

    def __link_end_start(self):
        self.first.prev = self.last
        self.last.next = self.first

    def add(self, data):
        new_node = self.Node(data)
        new_node.prev = self.current
        if self.current:
            self.current.next = new_node
        self.current = new_node
        if not self.first:
            self.first = self.current
        self.last = self.current
        self.__link_end_start()

    def __iter__(self):
        self.__stop = False
        self.__ptr = self.first
        return self

    def next(self):
        if self.__stop:
            raise StopIteration
        if self.__ptr == self.last:
            self.__stop = True
        node = self.__ptr
        self.__ptr = self.__ptr.next
        return node

