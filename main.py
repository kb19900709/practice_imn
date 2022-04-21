from car_config import Bus, SchoolBus, Tank


def main():
    show_how_car_works()


def show_how_car_works():
    my_bus = Bus(1, 'yellow', 3000, 'toyota', 30)
    my_schoolBus = SchoolBus(2, 'blue', 1500, 'honda')
    my_tank = Tank(3, 'green', 5000, '???')

    car_list = [my_bus, my_schoolBus, my_tank] # List[Car]
    for each_car in car_list:
        print('------------------------------')
        each_car.move()
        each_car.stop()
        # if type(each_car) == Bus:
        #     each_car.route()
        #     each_car.pay()



def show_how_animal_works():
    # Selena will implemet here
    pass


if __name__ == '__main__':
    main()
