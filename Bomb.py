from Graphics import *

class Bomb(object):
    """This creates a bomb object"""

    def __init__(self, center:Point, blastRadius = 200):
        self.center = center
        self.radius = blastRadius
        self.color = "red"
        self.blast = Circle(self.center, self.radius)

    def drawBomb(self, win):
        """Draws the bomb"""
        self.blast.setOutline(self.color)
        self.blast.setWidth(3)
        self.blast.draw(win)


