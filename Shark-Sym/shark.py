from graphics import *

class shark:
    def __init__(self, pos, win):

        self.point = Point(pos[0]*20+40, pos[1]*20+90)
        self.image = Circle(self.point, 10)
        self.image.draw(win)
        self.image.setFill(color_rgb(0,0,255))
        self.x = pos[0]
        self.y = pos[1]
        #shark values and characteristics
        #shark movement would be here based off of the fish movement

    def getPos(self):
        return [self.x, self.y]
