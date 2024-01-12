import os

class Store():
    def __init__(self):
        self.shoes = []
    
    def addToStore(self,shoe):
        self.shoes.append(shoe)

    def displayShoes(self):
        os.system('clear')
        print("\nYour store contains: ")
        for item in self.shoes:
            print(item.get_shoe_details())

class Shoe:
    def __init__(self,color, brand):
        self.color = color
        self.brand = brand
        
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} shoes added to store!")

    def get_shoe_details(self):
        return f"Shoe: {self.color} {self.brand}"
    

class Converse(Shoe):
    def __init__(self, color,lowOrHighTop,tongueColor):
        super().__init__(color, brand="Converse")
        self.lowOrHighTop = lowOrHighTop
        self.tongueColor = tongueColor
    

    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.lowOrHighTop}-top {shoeType.tongueColor} tongue-color {self.brand} added to store!")

    def get_shoe_details(self):
        return f"Converse: {self.color} {self.lowOrHighTop}-top {self.tongueColor} tongue-color"
    

class CombatShoe(Shoe):
    def __init__(self, color, brand, militiaryBranch, jungleOrDesert):
        super().__init__(color, brand)
        self.militiaryBranch = militiaryBranch
        if jungleOrDesert == "None":
            self.jungleOrDesert=""
        else:
            self.jungleOrDesert = (f" {jungleOrDesert}-camo")

    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.militiaryBranch.upper()}{self.jungleOrDesert} combat boots added to store")


    def get_shoe_details(self):
        return f"Combat Shoe: {self.color} {self.brand} {self.militiaryBranch.upper()}{self.jungleOrDesert} combat boots"


class Sandal(Shoe):
    def __init__(self, color, brand, openOrClosedToe, waterproof):
        super().__init__(color, brand)
        self.openOrClosedToe = openOrClosedToe
        self.waterproof = waterproof
    
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.openOrClosedToe}-toe {self.waterproof} sandals added to store!")

    def get_shoe_details(self):
        return f"Sandal: {self.color} {self.brand} {self.openOrClosedToe}-toe {self.waterproof}"


class Vans(Shoe):
    def __init__(self, color,lowOrHighTop,lacedOrOpen):
        super().__init__(color, brand="Vans")
        self.lowOrHighTop = lowOrHighTop
        self.lacedOrOpen = lacedOrOpen

    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {self.lowOrHighTop}-top {self.lacedOrOpen} {shoeType.brand} added to the store!")

    def get_shoe_details(self):
        return f"Vans: {self.color} {self.lowOrHighTop}-top {self.lacedOrOpen}"



def main():
    store = Store()
    print("----WELCOME TO THE SHOE-STOP----")

    while True:
        print("\n\n1)Regular Shoes")
        print("2)Converse Shoes")
        print("3)Combat Shoes")
        print("4)Sandals")
        print("5)Vans")
        print("6)Display all shoes")


        choice = input("\nWhat do you want to add: ")

        if choice == '1':
            color = input("\nEnter color of shoe: ").capitalize()
            brand = input("Enter brand: ").capitalize()
            shoe = Shoe(color, brand)
            store.addToStore(shoe)
            shoe.add_shoe(shoe)
        
        elif choice=='2':
            print("\nWelcome to the Converse section!\n")
            color = input("Enter color of converse: ").capitalize()
            low_or_high = input("Is it Low or High Top? (Type 'Low' or 'High'): ").capitalize()
            tongue_col = input("What is the color of Tongue? (Type 'Blue', 'Green', 'Red', 'Yellow', 'Black': ").capitalize()
            converse = Converse(color, low_or_high, tongue_col)
            store.addToStore(converse)
            converse.add_shoe(converse)
            
        
        elif choice=='3':
            print("\nWelcome to Combat Shoes Section!\n")
            color = input("Enter color of combat shoe: ").capitalize()
            brand = input("Enter brand of shoe: ").capitalize()
            military_branch = input("Which branch does this belong to?(USAF/USMC/USN/USCG/USAR): ").capitalize()
            jd = input("Does it have Jungle or Desert camouflage? (Jungle/Desert/None): ").capitalize()
            combat_shoe = CombatShoe(color, brand, military_branch, jd)
            store.addToStore(combat_shoe)
            combat_shoe.add_shoe(combat_shoe)
        

        elif choice == '4':
            print("\nWelcome to the Sandals Section\n")
            color = input("Enter color of sandals: ").capitalize()
            brand = input("Enter brand of sandals: ").capitalize()
            openOrClosed = input("Open or closed toe? 'open' / 'closed' : ").lower()
            waterProof = input("Is it Waterproof? Type 'Yes'/'No': ").lower()
            if waterProof == 'yes':
                waterProof = 'Waterproof'
            elif waterProof == "no":
                waterProof = "Non waterproof"
            else:
                print("Invalid choice")
            sandal = Sandal(color, brand, openOrClosed, waterProof)
            store.addToStore(sandal)
            sandal.add_shoe(sandal)
        
        elif choice == "5":
            print("Welcome to the Vans Section!")
            color = input("Enter color of Vans: ").capitalize()
            low_or_high = input("High top or low top: ").capitalize()
            laces = input("Laced/Unlaced: ").capitalize()
            vans = Vans(color, low_or_high, laces)
            store.addToStore(vans)
            vans.add_shoe(vans)

        elif choice=="6":
            store.displayShoes()

        else:
            exit()


if __name__=="__main__":
    main()