
class Animal:
    # valuable = (data source) -> maybe from a function or construction or specify a value like a str or int
    #
    # for example :
    # valuable = ClassName(args..)
    # monkey1 = Monkey(1, 'male', 35, 125, 'mammal', 'brown')
    # 
    # valuable = function_name()
    # valuable = '123' or 123 or []
    #
    # for every function in a class, the first arguement must be self, which means the reference of the instance
    #
    # (arguement or parampter)
    #
    # def -> for create a function
    # to use a function, you need to add valuable.function_name(args...)

    # construction: __init__
    def __init__(self, id, sex, weight, height, breed):
        # (field or attribute)
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
    
    def my_name(self, str):
        return str


class Monkey(Animal):
    def __init__(self, id, sex, weight, height, breed, flur_color):
        super(). __init__(id, sex, weight, height, breed)
        self.flur_color = flur_color
    
    def climb(self):
        print(f'i am  {self.flur_color} type , so i climb higher ')

    def sleep(self):
        print('is time to take a rest')


class Bear(Monkey):
    def __init__(self, id, sex, weight, height, breed, flur_color, habitat):
        super(). __init__(id, sex, weight, height, breed, flur_color)
        self.habitat = habitat

    def howl(self):
        print(f'this is my {self.habitat} ,leave me alone')

    def sleep (self):
        print('please be quiet')


class Tiger(Animal):
    def sleep(self):
        print('Go away, i want to sleep now!')