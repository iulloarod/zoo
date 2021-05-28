class Animal:
    def __init__(self,name="",age=1,health=50,happyness=50):
        self.name= name
        self.age= age 
        self.health = health
        self.happyness = happyness
    
    def display_info(self):
        print(f'Animal´s name:{self.name}. It´s Health is: {self.health}. It´s Happyness is: {self.happyness}')
    
    def feed_animal(self,kg_amount):
        self.health += kg_amount
        self.happyness += kg_amount

class Sheep(Animal):
    def __init__(self,wool_amount):
        self.wool_amount= wool_amount
        super().__init__(self,name="",age=1,health=80,happyness=50)

    def feed_animal(self,kg_amount):
        self.health = kg_amount
        self.happyness = kg_amount *1.1

        
class Chicken(Animal):
    def __init__(self,tail):
        self.tail= tail
        super().__init__(self,name="",age=1,health=90,happyness=70)

    def feed_animal(self,kg_amount):
        self.health = kg_amount*1.2
        self.happyness = kg_amount*1.3
        
class Traro(Animal):
    def __init__(self,crown):
        self.crown = crown
        super().__init__(self,name="",age=1,health=70,happyness=100)

    def feed_animal(self,kg_amount):
        self.health = kg_amount*1.4
        self.happyness = kg_amount*1.1

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_sheep(self, name):
        self.animals.append( Sheep(name) )

    def add_chicken(self, name):
        self.animals.append( Chicken(name) )

    def add_traro(self, name):
        self.animals.append( Traro(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Nacho's Zoo")
zoo1.add_sheep("76")
zoo1.add_sheep("Tripleta")
zoo1.add_chicken("Flor_de_haba")
zoo1.add_chicken("Locura")
zoo1.add_traro("Leftraro")
zoo1.print_all_info()
