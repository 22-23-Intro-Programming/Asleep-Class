class Dog:

    def __init__(self):
        self.hair = "fluffy"
        self.age = "4"
        self.color = "black"
        self.name = "Finn"

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    

def main():

    D = Dog()

    print("What is the Dog's name")

    print(D.getName())

if __name__ == "__main__":
    main()
