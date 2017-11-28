class Event(object):

    def __init__(self, type, source, destination):
        self.type = type
        self.source = source
        self.destination = destination

    def __repr__(self):
        return "Event(type={}, source={}, destination={})".format(self.type, self.source, self.destination)
