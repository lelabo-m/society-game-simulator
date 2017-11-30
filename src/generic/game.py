class Game(object):

    def __init__(self, player_template, number_of_player, turn=-1):
        self.__turn = 0
        self.actors = [player_template() for _ in range(number_of_player)]
        self.events = []
        self.__turn_events = []
        self.turn_limit = turn

    @property
    def turn_number(self):
        return self.__turn

    def __is_finished(self):
        return self.turn_number >= self.turn_limit if self.turn_number > 0 else False

    def is_finished(self):
        return True

    def __end(self):
        if self.is_finished():
            return True
        return self.__is_finished()

    def turn(self):
        pass

    def __new_turn(self):
        self.events.append(self.__turn_events)
        self.__turn_events = []
        self.__turn += 1
        self.turn()

    def loop(self):
        while not self.is_finished():
            self.__new_turn()

    def log(self, event):
        self.__turn_events.append(event)

    def analytics(self):
        pass