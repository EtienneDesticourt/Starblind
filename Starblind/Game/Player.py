from Game.Entity import Entity


class Player(Entity):
    """Implements player behaviour"""
    def __init__(self, rect):
        super(Player, self).__init__(rect, "player")
        #Intentions to better deal with event actions
        self.goingLeft  = False
        self.goingRight = False
        self.goingUp    = False
        self.goingDown  = False

    def updateSpeed(self):
        #TODO: Adjust for max speed and identical speed going diagonals
        if self.goingLeft and self.goingRight:
            self.speed[0] = 0
        elif self.goingLeft:
            self.speed[0] = -2
        elif self.goingRight:
            self.speed[0] = 2
        else:
            self.speed[0] = 0

        if self.goingUp and self.goingDown:
            self.speed[1] = 0
        elif self.goingUp:
            self.speed[1] = -2
        elif self.goingDown:
            self.speed[1] = 2
        else:
            self.speed[1] = 0



