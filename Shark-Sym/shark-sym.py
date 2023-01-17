from graphics import *
from Button import *
from Fish import *
from Shark import *


def main():
    
    win = GraphWin("Shark Simulator", 600, 600)
    x = 50
    y = 100
    for i in range(21):
        
        VLine = Line(Point(x,100),Point(x,500))
        VLine.draw(win)
        x = x + 20
    for j in range(21):
        
        VLine = Line(Point(50,y),Point(450,y))
        VLine.draw(win)
        y = y + 20
    #grid creator
    B = Button(win, Point(475,100), Point(575,150), "tomato", "Run")
    B2 = Button(win, Point(475,200 ), Point(575,250), "tomato", "Step")
    B3 = Button(win, Point(475,300 ), Point(575,350), "tomato", "Quit")
    #button creator

    
    
    F1 = fish((1,1),win)
    F2 = fish((3,3),win)
    F3 = fish((4,4),win)
    #fish spawns, random would have been integrated here 
    
    S = shark((10,10),win)
     #shark spawns, random would have been integrated here

    
        
    
        

    

    while True:
        m = win.getMouse()

        if B2.isClicked(m):
            
            sPos = shark.getPos(S)
            f1Pos = fish.getPos(F1)
            f2Pos = fish.getPos(F2)
            f3Pos = fish.getPos(F3)
            
            f1posDif = abs(sPos[0]-f1Pos[0]) + abs(sPos[1]-f1Pos[1])
            f2posDif = abs(sPos[0]-f2Pos[0]) + abs(sPos[1]-f2Pos[1])
            f3posDif = abs(sPos[0]-f3Pos[0]) + abs(sPos[1]-f3Pos[1])

            if f1posDif < f2posDif:
                if f1posDif < f3posDif:
                    print("sharkchasef1")
                elif f1posDif == f3posDif:
                    print("sharkrandomf13")
                else:
                    print("sharkchasef3")
            elif f1posDif == f2posDif:
                    print("sharkrandomf12")
            else:
                if f2posDif < f3posDif:
                    print("sharkchasef2")
                elif f2posDif == f3posDif:
                    print("sharkrandomf23")
                else:
                    print("sharkchasef3")
                #distance detector
            
            
            

            

            
            if f1posDif < 10:
                if sPos[0]-f1Pos[0] > 0: #if the shark is right of the fish
                    if sPos[1]-f1Pos[1] > 0: #if the shark is below the fish
                        if sPos[0] - f1Pos[0] > sPos[1]-f1Pos[1]: #if the shark is more right than below the fish
                            if f1Pos[0]-1 > 0:
                                f1newPos[0] = f1Pos[0] - 1
                            elif f1Pos[1]-1 > 0:
                                f1newPos[1] = f1Pos[1] - 1
                        else:
                            if f1Pos[1]-1 > 0:
                                f1newPos[1] = f1Pos[1] - 1
                            elif f1Pos[0]-1 > 0:
                                f1newPos[0] = f1Pos[0] - 1
                    else:
                        if sPos[0]-f1Pos[0] > f1Pos[1]-sPos[1]:
                            if f1Pos[0]-1 > 0:
                                f1newPos[0] = f1Pos[0] - 1
                            elif f1Pos[1]+1 < 20:
                                f1newPos[1] = f1Pos[1] + 1
                        else:
                            if f1Pos[1]+1 < 20:
                                f1newPos[1] = f1Pos[1] + 1
                            elif f1Pos[0]-1 > 0:
                                f1newPos[0] = f1Pos[0] - 1
                           
                else:
                    if sPos[1]-f1Pos[1] > 0: #if the shark is below the fish
                        if f1Pos[0] - sPos[0] > sPos[1]-f1Pos[1]: #if the shark is more left than below the fish
                            f1newPos[0] = f1Pos[0] + 1
                        else:
                            f1newPos[1] = f1Pos[1] -1
                    else:
                        if sPos[0]-f1Pos[0] > f1Pos[1]-sPos[1]:
                            f1newPos[0] = f1Pos[0] - 1
                        else:
                            f1newPos[1] = f1Pos[1] + 1
            else:
                f1newPos = F1.randomMove()
                            
            if f2posDif < 10:
                if sPos[0]-f2Pos[0] > 0: #if the shark is right of the fish
                    if sPos[1]-f2Pos[1] > 0: #if the shark is below the fish
                        if sPos[0] - f2Pos[0] > sPos[1]-f2Pos[1]: #if the shark is more right than below the fish
                            if f2Pos[0]-1 > 0:
                                f2newPos[0] = f2Pos[0] - 1
                            elif f2Pos[1]-1 > 0:
                                f2newPos[1] = f2Pos[1] - 1
                        else:
                            if f2Pos[1]-1 > 0:
                                f2newPos[1] = f2Pos[1] - 1
                            elif f2Pos[0]-1 > 0:
                                f2newPos[0] = f2Pos[0] - 1
                    else:
                        if sPos[0]-f2Pos[0] > f2Pos[1]-sPos[1]:
                            if f2Pos[0]-1 > 0:
                                f2newPos[0] = f2Pos[0] - 1
                            elif f2Pos[1]+1 < 20:
                                f2newPos[1] = f2Pos[1] + 1
                        else:
                            if f2Pos[1]+1 < 20:
                                f2newPos[1] = f2Pos[1] + 1
                            elif f2Pos[0]-1 > 0:
                                f2newPos[0] = f2Pos[0] - 1
                           
                else:
                    if sPos[1]-f2Pos[1] > 0: #if the shark is below the fish
                        if f2Pos[0] - sPos[0] > sPos[1]-f2Pos[1]: #if the shark is more left than below the fish
                            f2newPos[0] = f2Pos[0] + 1
                        else:
                            f2newPos[1] = f2Pos[1] -1
                    else:
                        if sPos[0]-f2Pos[0] > f2Pos[1]-sPos[1]:
                            f2newPos[0] = f2Pos[0] - 1
                        else:
                            f2newPos[1] = f2Pos[1] + 1
            else:
                f2newPos = F2.randomMove()

            if f3posDif < 10:
                if sPos[0]-f3Pos[0] > 0: #if the shark is right of the fish
                    if sPos[1]-f3Pos[1] > 0: #if the shark is below the fish
                        if sPos[0] - f3Pos[0] > sPos[1]-f3Pos[1]: #if the shark is more right than below the fish
                            if f3Pos[0]-1 > 0:
                                f3newPos[0] = f3Pos[0] - 1
                            elif f3Pos[1]-1 > 0:
                                f3newPos[1] = f3Pos[1] - 1
                        else:
                            if f3Pos[1]-1 > 0:
                                f3newPos[1] = f3Pos[1] - 1
                            elif f3Pos[0]-1 > 0:
                                f3newPos[0] = f3Pos[0] - 1
                    else:
                        if sPos[0]-f3Pos[0] > f3Pos[1]-sPos[1]:
                            if f3Pos[0]-1 > 0:
                                f3newPos[0] = f3Pos[0] - 1
                            elif f3Pos[1]+1 < 20:
                                f3newPos[1] = f3Pos[1] + 1
                        else:
                            if f3Pos[1]+1 < 20:
                                f3newPos[1] = f3Pos[1] + 1
                            elif f3Pos[0]-1 > 0:
                                f3newPos[0] = f3Pos[0] - 1
                           
                else:
                    if sPos[1]-f3Pos[1] > 0: #if the shark is below the fish
                        if f3Pos[0] - sPos[0] > sPos[1]-f3Pos[1]: #if the shark is more left than below the fish
                            f3newPos[0] = f3Pos[0] + 1
                        else:
                            f3newPos[1] = f3Pos[1] -1
                    else:
                        if sPos[0]-f3Pos[0] > f3Pos[1]-sPos[1]:
                            f3newPos[0] = f3Pos[0] - 1
                        else:
                            f3newPos[1] = f3Pos[1] + 1
            else:
                f3newPos = F3.randomMove() 
                    
                
            
            
            
                
            
                
            F1.movePos(f1newPos)
            F2.movePos(f2newPos)
            F3.movePos(f3newPos)

    
        



if __name__ == "__main__":
    main()
        
                
