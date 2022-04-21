
from config import Bus, Car, SchoolBus, Tank


def main():
    my_bus = Bus(3, 'yellow', 3000, '123456789', 30)
    my_schoolBus = SchoolBus(2, 'blue', 1500, 'edf')
    my_tank = Tank(3, 'green', 5000, 'mnbvcx')

    car_list = [my_bus, my_schoolBus, my_tank] # List[Car]
    for each_car in car_list:
        each_car.move()



if __name__ == '__main__':
    main()
