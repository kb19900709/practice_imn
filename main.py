from animal_config import Bear, Monkey, Tiger
from car_config import Bus, SchoolBus, Tank


def main():
    #show_how_car_works()
    show_how_animal_works()

# def show_how_car_works():
#     my_bus = Bus(1, 'yellow', 3000, 'toyota', 30)
#     my_schoolBus = SchoolBus(2, 'blue', 1500, 'honda')
#     my_tank = Tank(3, 'green', 5000, '???')

#     car_list = [my_bus, my_schoolBus, my_tank] # List[Car]
#     for each_car in car_list:
#         print('------------------------------')
#         each_car.move()
#         each_car.stop()
        # if type(each_car) == Bus:
        #     each_car.route()
        #     each_car.pay()



def show_how_animal_works():
    # Selena will implemet here
    monkey1 = Monkey(1, 'male', 35, 125, 'mammal', 'brown')
    monkey2 = Monkey(2, 'female', 75, 105, 'mammal', 'black')
    bear1 = Bear(3, 'male', 180, 200, 'mammal', 'white', 'ice')
    bear2 = Bear(4, 'male', 230, 300, 'mammal', 'brown', 'forest')
    tiger1 = Tiger(5, 'female', 100, 80, 'mammal')
    tiger2 = Tiger(6, 'male', 150, 90, 'mammal')

    animal_list = [monkey1, monkey2, bear1, bear2, tiger1, tiger2]
    for animal in animal_list:
        print(f"\n{animal.id}")
        print('-----------------------')
        animal.sleep()
        print('-----------------------')
        animal.cry()
        print('-----------------------')
        animal.pee()

    ###
    #   get field or get atrribute
    #
    #   monkey2.id
    #   monkey2.sex
    #   monkey2.weight
    #   monkey2.height
    #   monkey2.breed
    #   monkey2.flur_color
    #   -----------------------
    #   invoke a function from an instance
    #
    #   monkey2.eat()
    #   monkey2.sleep()    
    #   monkey2.my_name('selena')
    ###
       
    
if __name__ == '__main__':
    main()
