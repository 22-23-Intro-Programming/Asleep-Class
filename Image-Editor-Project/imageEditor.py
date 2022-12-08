

from Button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()
            
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r = r - 50
            g = g - 50
            b = b - 50
            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)
            
    return True

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()
            
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r = r + 50
            g = g + 50
            b = b + 50
            if r >= 255:
                r = 255
            if g >= 255:
                g = 255
            if b >= 255:
                b = 255
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)
            
    return True

def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()
            
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r2 = ((r + g + b) // 3)
            g2 = ((r + g + b) // 3)
            b2 = ((r + g + b) // 3)
            r = r2
            g = g2
            b = b2
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

            
    return True

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()
            
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            if ((r + g + b) // 3 > 128):
                r = r + 50
                g = g + 50
                b = b + 50
                if r >= 255:
                    r = 255
                if g >= 255:
                    g = 255
                if b >= 255:
                    b = 255
                newColor = color_rgb(r, g, b)
                img.setPixel(i, j, newColor)

            else:
                r = r - 50
                g = g - 50
                b = b - 50
                if r <= 0:
                    r = 0
                if g <= 0:
                    g = 0
                if b <= 0:
                    b = 0
                newColor = color_rgb(r, g, b)
                img.setPixel(i, j, newColor)

            

def main():

    win = GraphWin("Image Editor", 800, 800)

    img = Image(Point(400,400), "gundamHead.png")
    img.draw(win)
    b1 = Button(win, Point(0, 0), Point(200, 100), "cyan", "Darken")
    b2 = Button(win, Point(200, 0), Point(400, 100), "cyan", "Lighten")
    b3 = Button(win, Point(400, 0), Point(600, 100), "cyan","Grayscale")
    b4 = Button(win, Point(600, 0), Point(800, 100), "cyan","Contrast")
    QButton = Button(win, Point(650, 675), Point(800, 800), "red", "Quit")





               
            
                
            
                
                



            
            #img.setPixel(i, j, newColor)


   




    while True:
        m = win.getMouse()
        
        if b1.isClicked(m):
            print("Darkened")
            darken(img)
           

        if b2.isClicked(m):
            print("Lightened")
            lighten(img)
       
          

        if b3.isClicked(m):
            print("Grayscaled")
            grayscale(img)

        
        if b4.isClicked(m):
            print("Contrasted")
            contrast(img)

            

        elif QButton.isClicked(m):
            break

    win.close()

        


   
    






if __name__ == "__main__":
    main()
