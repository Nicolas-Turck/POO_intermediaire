from car import *
from bus import *
from vehicules import *
if __name__ == '__main__':
    car = Car(7, 1000,"blue")
    bus = Bus(2000, 2, 1, "red")
    print(car.__dict__)
    print(bus.__dict__)
    car.color = "green"
    bus.numbers_stage = 2
    print(car.__dict__)
    print(bus.__dict__)