from graphics import *
import random

class fish:
    def __init__(self, pos, win):

        self.point = Point(pos[0]*20+40, pos[1]*20+90)
        self.image = Circle(self.point, 10)
        self.image.draw(win)
        
        self.x = pos[0]
        self.y = pos[1]
        #fish values and characteristics

    def getPos(self):
        return [self.x, self.y]
    
    def randomMove(self):
        L = [1,2,3,4]
        c = random.choice(L)
        newPos = [self.x,self.y]
        if c == 1:
            if newPos[1]-1 > 0:
                newPos[1] = newPos[1] - 1
            else:
                newPos[1] = newPos[1] + 1
        if c == 2:
            if newPos[1]+1 < 21:
                newPos[1] = newPos[1] + 1
            else:
                newPos[1] = newPos[1] - 1
        if c == 3:
            if newPos[0]-1 > 0:
                newPos[0] = newPos[0] - 1
            else:
                newPos[0] = newPos[0] + 1
        if c == 4:
            if newPos[0]+1 < 21:
                newPos[0] = newPos[0] + 1
            else:
                newPos[0] = newPos[0] - 1
            
        
        return newPos
    #move chooser

    

    def movePos(self, newPos):
        
        point2 = Point(int(newPos[0])*20 + 40, int(newPos[1])*20+90)
        diffX = point2.getX() - self.point.getX()
        diffY = point2.getY() - self.point.getY()
        self.image.move(diffX, diffY)
        self.point = point2
        self.x = newPos[0]
        self.y = newPos[1]

        #move executor

        
        
