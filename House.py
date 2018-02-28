from Graphics import *
import random
from Bomb import *

class House(object):
    """Create a House object"""
    destroyed = 0

    def __init__(self, x, y):
        self.centerX = x
        self.centerY = y
        self.width = random.randint(10, 30)
        self.height = random.randint(10, 30)
        self.house = Rectangle(Point(self.centerX - self.width//2, self.centerY - self.height//2), Point(self.centerX + self.width//2, self.centerY + self.height//2))
        self.isDestroyed = False
        self.color = "black"

    def drawHouse(self, win:GraphWin):
        """This will draw our house!"""
        self.house.setFill(self.color)
        self.house.draw(win)

    def getDistance(self, click:Point):
        """Returns the distance between the house center and the click point"""
        clickX = click.getX()
        clickY = click.getY()
        distance = ((clickX - self.centerX)**2 + (clickY - self.centerY)**2)**(1/2)
        return distance

    def isItHit(self, bomb:Bomb, click:Point):
        """See if a house is within the blast radius and if it is, turn that house red"""
        distance = self.getDistance(click)
        if distance <= bomb.radius:
            self.house.setFill("red")
            self.isDestroyed = True
            House.destroyed += 1

