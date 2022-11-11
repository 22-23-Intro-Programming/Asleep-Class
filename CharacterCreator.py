from graphics import*

from Button import*

def main():

    win = GraphWin("Character Creator", 800, 800)
    Face = Oval(Point(100,100), Point (500,700))
    Face.draw(win)

    eyes1 = Button(win, Point(525, 100), Point(625, 175), "cyan", "Big Eyes")

    eyes2 = Button(win, Point(650, 100), Point(750, 175), "blue", "Small Eyes")

    mouth1 = Button(win, Point(525, 225), Point(625, 300), "pink", "Neutral Mouth")

    mouth2 = Button(win, Point(650, 225), Point(750, 300), "orange", "Surprised Mouth")

    nose1 = Button(win, Point(525, 350), Point(625, 425), "yellow", "Sharp Nose")

    nose2 = Button(win, Point(650, 350), Point(750, 425), "purple","Blunt Nose")

    QButton = Button(win, Point(600, 625), Point(750, 725), "red", "Quit")
    

    #big eyes
    Eye1 = Circle(Point(250,200), 50)
    Eye2 = Circle(Point(450,200), 50)
    #small eyes
    eye1 = Circle(Point(250,200), 20)
    eye2 = Circle(Point(450,200), 20)
    #neutral mouth
    Mouth1 = Line(Point(250,500), Point(450,500))
    #surprised mouth
    Mouth2 = Oval(Point(275,500), Point(425, 700))
    #sharp nose
    Nose1 = Polygon(Point(350,400), Point(300,300), Point(400,300))
    #blunt nose
    Nose2 = Rectangle(Point(300,300), Point(400,450))
    
    
    
    while True:
        m = win.getMouse()
        if eyes1.isClicked(m):
            print("Big Eyes")
            eye1.undraw()
            eye2.undraw()
            Eye1.undraw()
            Eye2.undraw()

            Eye1.draw(win)
            Eye2.draw(win)

        elif  eyes2.isClicked(m):
            print("Small Eyes")
            eye1.undraw()
            eye2.undraw()
            Eye1.undraw()
            Eye2.undraw()

            eye1.draw(win)
            eye2.draw(win)

        if mouth1.isClicked(m):
            print("Straight Face")
            Mouth1.undraw()
            Mouth2.undraw()
            
            Mouth1.draw(win)

        elif mouth2.isClicked(m):
            print("Surprised Face")
            Mouth1.undraw()
            Mouth2.undraw()
            
            Mouth2.draw(win)

        if nose1.isClicked(m):
            print("Straight Face")
            Nose1.undraw()
            Nose2.undraw()
            
            Nose1.draw(win)

        elif nose2.isClicked(m):
            print("Surprised Face")
            Nose1.undraw()
            Nose2.undraw()
            
            Nose2.draw(win)
            

        elif QButton.isClicked(m):
            break

    win.close()

        


   
    






if __name__ == "__main__":
    main()
