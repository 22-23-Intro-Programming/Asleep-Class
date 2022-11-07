def CurrencyConverter():

    print("Please enter which type of currency you have. Choose from the list:")
    print("1. United States Dollar")
    print("2. Pound Sterling")
    print("3. Japanese Yen")
    x = input("4. Indian Rupee \n \n")

    y = input("Please enter how much money you have \n")

    print("Please enter which type of currency you would like to convert to. Choose from the list:")
    print("1. United States Dollar")
    print("2. Pound Sterling")
    print("3. Japanese Yen")
    z = input("4. Indian Rupee \n \n")

    y = float(y)
    
    if x == "1":
        USD = {"Pound Sterling": 0.87,"Japanese Yen": 148.21, "Indian Rupee": 82.60}
        w = USD.get("Pound Sterling")
        e = USD.get("Japanese Yen")
        r = USD.get("Indian Rupee")
        if z == "2":
            print(str(y*float(w)) + " Pounds")
        if z == "3":
            print(str(y*float(e)) + " Yen")
        if z == "4":
            print(str(y*float(r)) + " Rupee")
    if x == "2":
        Pound = {"United States Dollar": 1.14,"Japanese Yen": 169.66, "Indian Rupee": 94.57}
        t = Pound.get("United States Dollar")
        u = Pound.get("Japanese Yen")
        i = Pound.get("Indian Rupee")
        if z == "1":
            print(str(y*float(t)) + " Dollars")
        if z == "3":
            print(str(y*float(u)) + " Yen")
        if z == "4":
            print(str(y*float(i)) + " Rupee")
    if x == "3":
        Yen = {"Pound Sterling": 0.0059,"United States Dollar": 0.0067, "Indian Rupee": 0.56}
        s = Yen.get("United States Dollar")
        d = Yen.get("Pound Sterling")
        f = Yen.get("Indian Rupee")
        if z == "1":
            print(str(y*float(s)) + " Dollars")
        if z == "2":
            print(str(y*float(d)) + " Pounds")
        if z == "4":
            print(str(y*float(f)) + " Rupee")
    if x == "4":
        Rupee = {"Pound Sterling": 0.011,"Japanese Yen": 1.79, "United States Dollar": 0.012}
        h = Rupee.get("United States Dollar")
        j = Rupee.get("Pound Sterling")
        k = Rupee.get("Japanese Yen")
        if z == "1":
            print(str(y*float(h)) + " Dollars")
        if z == "2":
            print(str(y*float(j)) + " Pounds")
        if z == "3":
            print(str(y*float(k)) + " Yen")


def GroceryList(l):

    groceryList = {"apple": 1.50,
                   "orange": 1.00,
                   "banana": 1.00,
                   "bagel": 1.25,
                   "cabbage": 1.50,
                   "spinach": 4.25,
                   "milk": 2.75,
                   "eggs": 3.25,
                   "cake": 8.00,
                   "pasta":3.50}

    total = 0
    
    for i in l:
    
        total = total+(groceryList.get(i))

    print(str(total) + "$")
        
        
        
    
        



def main():

    #CurrencyConverter()

    GroceryList(["orange", "cabbage", "cake", "pasta"])


if __name__ == "__main__":
    main()
