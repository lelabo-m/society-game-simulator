from .event import Event


class PlayerInteractionEvent(Event):

    def __init__(self, source, destination):
        super(Event, self).__init__("players", source)
        self.destination = destination

    def __repr__(self):
        return "PlayerInteractionEvent(type={}, source={}, destination={})".format(self.type, self.source, self.destination)
