class Game(object):

    def __init__(self, players):
        self.turn = 0
        self.actors = players
        self.events = []

    def is_finished(self):
        pass

    def new_turn(self):
        pass

    def loop(self):
        while not self.is_finished():
            self.new_turn()

    def analytics(self):
        pass