
class Animal:
    # Selena will implemet here
    def __init__(self, id, sex, weight, height, breed):
        self.id = id
        self.sex = sex
        self.weight = weight
        self.height = height
        self.breed = breed

    def eat(self):
        print('please give me some noodle')

    def sleep(self):
        print('i am extremely tired')

    def cry(self):
        print (f'I become{self.weight} ,so fat')
        
    def pee(self):
        print('I drink too much water')


class monkey(Animal):
    def __init__(self, id, sex, weight, height, breed, flur_color):
        super(). __init__(id, sex, weight, height, breed)
        self.flur_color = flur_color
    
    def climb(self):
        print(f'i am  {self.flur_color} type , so i climb higher ')

    def sleep(self):
        print('is time to take a rest')


class bear(monkey):
    def __init__(self, id, sex, weight, height, breed, flur_color, habitat):
        super(). __init__(id, sex, weight, height, breed, flur_color)
        self.habitat = habitat

    def howl(self):
        print(f'this is my {self.habitat} ,leave me alone')

    def sleep (self):
        print('please be quiet')


class tiger(Animal):
    def sleep(self):
        print('Go away, i want to sleep now!')