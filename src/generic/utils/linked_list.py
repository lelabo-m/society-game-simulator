class LinkedList(object):

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.current = None
        self.first = None
        self.last = None

    def add(self, data):
        new_node = self.Node(data)
        new_node.prev = self.current
        if self.current:
            self.current.next = new_node
        self.current = new_node
        if not self.first:
            self.first = self.current
        self.last = self.current

    def link_end_start(self):
        self.first.prev
