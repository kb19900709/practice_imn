from abc import abstractmethod, ABC

class Car(ABC):
    def __init__(self, id, color, size, brand):
        self.id = id
        self.color = color
        self.size = size
        self.brand = brand

    def stop(self):
        print(f'{self.id}/{self.brand} stop !!!')

    @abstractmethod
    def move(self):
        pass


class Bus(Car):
    def __init__(self, id, color, size, brand, capacity):
        super().__init__(id, color, size, brand)
        self.capacity = capacity

    def route(self):
        print("follow GPS")

    def pay(self):
        print("visa")

    def move(self):
        print("40km/hr")


class SchoolBus(Car):
    def move(self):
        print("30km/hr")


class Tank(Car):
    def move(self):
        print("60km/hr")
