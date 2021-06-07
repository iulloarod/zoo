class Animal:
    def __init__(self,name= "nombrame!",age=2,health=100,happyness=100):
        self.name= name
        self.age= age
        self.health = health
        self.happyness = happyness
    
    def display_info(self):
        print(f'Animal´s name:{self.name}. It´s Health is: {self.health}. It´s Happyness is: {self.happyness}')
        return self
    
    def feed_animal(self,kg_amount):
        self.health += kg_amount
        self.happyness += kg_amount
        return self


class Sheep(Animal):
    def __init__(self,wool_amount):
        self.wool_amount= wool_amount
        super().__init__(self,name,age,health,happyness)

    def feed_animal(self,kg_amount):
        self.health = kg_amount
        self.happyness = kg_amount *1.1
        return self


        
class Chicken(Animal):
    def __init__(self,tail):
        self.tail= tail
        super().__init__(self,name,age,health,happyness)

    def feed_animal(self,kg_amount):
        self.health = kg_amount*1.2
        self.happyness = kg_amount*1.3
        return self
        
class Traro(Animal):
    def __init__(self,crown):
        self.crown = crown
        super().__init__(self,name,age,health,happyness)
        return self

    def feed_animal(self,kg_amount):
        self.health = kg_amount*1.4
        self.happyness = kg_amount*1.1
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_sheep(self,name="nombrame!"):
        self.animals.append()
        return self

    def add_chicken(name="nombrame!"):
        self.animals.append()
        return self

    def add_traro(self,name="nombrame!"):
        self.append()
        return self

    # def print_all_info(self):
    #     print("-"*30, self.name, "-"*30)
    #     for animal in self.animals:
    #         animal.display_info()


Zoo.add_chicken()