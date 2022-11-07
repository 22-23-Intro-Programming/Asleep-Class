def main():

    greetings()


def greetings():
    x=input("What's your name\n")
    print("Hey "+ x + "Nice to meet you!")
if __name__== "__main__":
    greetings()


def multiple(int1, int2):
    print("Check Multiple")
    if ((int1) % (int2) == 0):
        print(str(int1) + " is a multiple of " + str(int2))
    else:
        print(str(int1) + " is not a multiple of " + str(int2))
    

def Palindrome(pe):
    return pe == pe[::-1]
 
 
pe = input("Enter a potential Palindrome\n")
ans = Palindrome(pe)
 
if ans:
    print("Yes, that is a Palindrome!")
else:
    print("No, that is not a Palindrome!")
    
