def con7(l):
    # l is a list
    for i in range(len(l)-1):
        if l[i] == 7:
            if l[i+1] == 7:
                return True
                #return stops the method
    return False
def sumNot0(l):

    total = 0
    for x in l:
        if x == 0:
            break
        total = total + x
    return total
    
def sum2notthrough3(l):
     
    total = 0
    addition = True
    
    for i in range(len(l)):
        if l[i] == 2: 
            
            addition = False 
         

        if addition == True:
            total = total + l[i]
        
           
        if addition == False:
            total = total + 0
            if l[i] == 3:
                addition = True
        

        

    return total
            
   
    

def main():
    print(con7([1, 3, 7, 9, 7]))
    print(con7([1, 4, 7, 7]))
    print(con7([1, 5, 7, 7, 8]))

    print(sumNot0([1, 5, 7, 0, 8]))
    print(sumNot0([1, 3, 0, 6, 8]))
    print(sum2notthrough3([1, 5, 6, 2, 99, 56, 3]))8
    print(sum2notthrough3([4, 2, 7, 3, 69, 5, 2]))
    print(sum2notthrough3([1, 9, 2, 1, 4, 3, 25, 5]))



if(__name__ == "__main__"):
   main()
