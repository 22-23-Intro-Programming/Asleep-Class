def main():
    
    print(camelcase())
        
    '''print(fact(3))'''

    '''print(double())'''

def fact(x):
    product = 1
    for i in range(x):
        product = (product * (x-i))
    return product

def double():
    ans = input("please enter a phrase you would like to 'double'\n")
    res = ""
    for l in ans:
        res = res + l + l
    return res

def camelcase():
    cam = input("please enter a filename\n")
    cam = cam.title()
    cam = cam.replace("/","-")
    cam = cam.replace(" ","")
    cam = cam.replace(cam[0],cam[0].lower())
    return cam
    
    
        
        
        
    
     
    
        
    
    
    
if(__name__ == "__main__"):
    main()
