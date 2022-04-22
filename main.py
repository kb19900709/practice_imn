from animal_config import bear, monkey, tiger
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
    monkey1 = monkey(1, 'male', 35, 125, 'mammal', 'brown')
    monkey2 = monkey(2, 'female', 75, 105, 'mammal', 'black')
    bear1 = bear(3, 'male', 180, 200, 'mammal', 'white', 'ice')
    bear2 = bear(4, 'male', 230, 300, 'mammal', 'brown', 'forest')
    tiger1 = tiger(5, 'female', 100, 80, 'mammal')
    tiger2 = tiger(6, 'male', 150, 90, 'mammal')

    animal_list = [monkey1, monkey2, bear1, bear2, tiger1, tiger2]
    for animal in animal_list:
        print(f"\n{animal.id}")
        print('-----------------------')
        animal.sleep()
        print('-----------------------')
        animal.cry()
        print('-----------------------')
        animal.pee()
       
    
if __name__ == '__main__':
    main()
