import numpy as np
import matplotlib.pyplot as plt
from Objects import World
from Objects import Creature

# File will organize all the code and be the general script for running. Possibly have a mock game loop for running?
# Python is pretty procedural from what I know but its possible there is some OOP support or that we can hack it
# together with some clever file imports and arrays

# initial vars?
initParams = [1,1,1] # 1. speed 2. size 3. sense
creatureNumber = 1
stepNumber = 1000
creatures = []

for i in range(creatureNumber):
    creatures.append(Creature.Creature(initParams, [1, 1]))

world = World.World(10, creatures)

# Next section should deal with iterating the world, idk how i would determine the endpoint or how to define what a"day"
# is yet

for i in range(stepNumber):
    world.update()
