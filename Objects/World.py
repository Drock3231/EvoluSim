# should maybe contain list of creatures?
import Creature

class World:

    placeholder = 0

    def __init__(self, size, creatures):
        self.size = size
        self.creatures = creatures

    def update(self):
        for i in range(len(self.creatures)):
            self.creatures[i].update()

