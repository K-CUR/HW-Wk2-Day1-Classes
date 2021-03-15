class Team:

    def __init__(self, name, players, coach):
        self.players = players
        self.coach = coach
        self.name = name
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, selected_player):
        for player in self.players:
            if player == selected_player:
                return True
        return False

    def points(self):
        return self.points

    def play_game(self, result):
        if result == True:
            self.points += 3
