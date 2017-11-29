from .event import Event


class DrawEvent(Event):

    def __init__(self, source, element):
        super(Event, self).__init__("draw", source)
        self.element = element

    def __repr__(self):
        return "DrawEvent(type={}, source={}, element={})".format(self.type, self.source, self.element)
