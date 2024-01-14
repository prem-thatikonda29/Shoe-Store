from flask import Flask, render_template, request

app = Flask(__name__)

class Store():
    def __init__(self):
        self.shoes = []
    
    def addToStore(self, shoe):
        self.shoes.append(shoe)

    def displayShoes(self):
        return [item.get_shoe_details() for item in self.shoes]

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


store = Store()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_shoe', methods=['POST'])
def add_shoe():
    choice = request.form['choice']
    
    if choice == '1':
        color = request.form['color'].capitalize()
        brand = request.form['brand'].capitalize()
        shoe = Shoe(color, brand)
        store.addToStore(shoe)
        shoe.add_shoe(shoe)
        
    elif choice=='2':
        color = request.form['color'].capitalize()
        lowOrHigh = request.form['low/high'].capitalize()
        tongue = request.form['tongue'].capitalize()
        converse = Converse(color,lowOrHigh,tongue)
        store.addToStore(converse)
        converse.add_shoe(converse)

    elif choice=='3':
        color = request.form['color'].capitalize()
        

    return render_template('index.html')

@app.route('/display_shoes')
def display_shoes():
    shoes = store.displayShoes()
    return render_template('display_shoes.html', shoes=shoes)

if __name__ == "__main__":
    app.run(debug=True)
