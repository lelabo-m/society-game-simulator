class Event(object):

    def __init__(self, type, source):
        self.type = type
        self.source = source

    def __repr__(self):
        return "Event(type={}, source={})".format(self.type, self.source)
