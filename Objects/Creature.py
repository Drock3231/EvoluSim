# needs to have pathfinding to search for food and junk

class Creature:

    def __init__(self, initParams, pos):
        self.size = initParams[0]
        self.speed = initParams[1]
        self.sense = initParams[2]
        self.pos = pos

    def update(self):
        self.updatePOS()

    def updatePOS(self):
        print "???"