import uuid


class Actor(object):

    def __init__(self):
        self.id = uuid.uuid4()

    def behavior(self):
        pass
