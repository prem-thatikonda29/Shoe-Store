import mysql.connector

class Shoe:
    def __init__(self,color, brand):
        self.color = color
        self.brand = brand
        
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} shoes added to store!")
    

class Converse(Shoe):
    def __init__(self, color,lowOrHighTop,tongueColor):
        super().__init__(color, brand="Converse")
        self.lowOrHighTop = lowOrHighTop
        self.tongueColor = tongueColor
    

    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.lowOrHighTop}-top {shoeType.tongueColor} tongue-color {self.brand} added to store!")


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


class Sandal(Shoe):
    def __init__(self, color, brand, openOrClosedToe, waterproof):
        super().__init__(color, brand)
        self.openOrClosedToe = openOrClosedToe
        self.waterproof = waterproof
    
    def add_shoe(self, shoeType):
        print(f"{shoeType.color} {shoeType.brand} {self.openOrClosedToe}-toe {self.waterproof} sandals added to store!")



class ShoeStoreDB:
    def __init__(self, host="localhost", user="your_username", password="your_password", database="shoe_store"):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS shoes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                color VARCHAR(255),
                brand VARCHAR(255),
                type VARCHAR(255),
                low_or_high_top VARCHAR(255),
                tongue_color VARCHAR(255),
                military_branch VARCHAR(255),
                jungle_or_desert VARCHAR(255),
                open_or_closed_toe VARCHAR(255),
                waterproof VARCHAR(255)
            )
        ''')
        self.conn.commit()

    def add_shoe_to_db(self, shoe):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO shoes (color, brand, type, low_or_high_top, tongue_color, military_branch, jungle_or_desert, open_or_closed_toe, waterproof)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (shoe.color, shoe.brand, type(shoe).__name__, getattr(shoe, 'lowOrHighTop', ''),
              getattr(shoe, 'tongueColor', ''), getattr(shoe, 'militiaryBranch', ''),
              getattr(shoe, 'jungleOrDesert', ''), getattr(shoe, 'openOrClosedToe', ''),
              getattr(shoe, 'waterproof', '')))
        self.conn.commit()

# Modify your main function to include database interaction

def main():
    print("----WELCOME TO THE SHOE-STOP(Admin Side)----")
    # Update the connection details as per your MySQL setup
    shoe_store_db = ShoeStoreDB(host="your_mysql_host", user="your_mysql_username", password="your_mysql_password", database="shoe_store")

    while True:
        print("\n\n1)Regular Shoes")
        print("2)Converse Shoes")
        print("3)Combat Shoes")
        print("4)Sandals")
        choice = int(input("\nWhat do you want to add: "))

        if choice == 1:
            color = input("\nEnter color of shoe: ").capitalize()
            brand = input("Enter brand: ").capitalize()
            shoe = Shoe(color, brand)
            shoe.add_shoe(shoe)
            shoe_store_db.add_shoe_to_db(shoe)
        
        elif choice==2:
            print("\nWelcome to the Converse section!\n")
            color = input("Enter color of converse: ").capitalize()
            low_or_high = input("Is it Low or High Top? (Type 'Low' or 'High'): ").capitalize()
            tongue_col = input("What is the color of Tongue? (Type 'Blue', 'Green', 'Red', 'Yellow', 'Black': ").capitalize()
            converse = Converse(color, low_or_high, tongue_col)
            converse.add_shoe(converse)
            shoe_store_db.add_shoe_to_db(converse)
            
        elif choice==3:
            print("\nWelcome to Combat Shoes Section!\n")
            color = input("Enter color of combat shoe: ").capitalize()
            brand = input("Enter brand of shoe: ").capitalize()
            military_branch = input("Which branch does this belong to?(USAF/USMC/USN/USCG/USAR): ").capitalize()
            jd = input("Does it have Jungle or Desert camouflage? (Jungle/Desert/None): ").capitalize()
            combat_shoe = CombatShoe(color, brand, military_branch, jd)
            combat_shoe.add_shoe(combat_shoe)
            shoe_store_db.add_shoe_to_db(combat_shoe)
        
        elif choice == 4:
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
            sandal.add_shoe(sandal)
            shoe_store_db.add_shoe_to_db(sandal)

if __name__ == "__main__":
    main()
