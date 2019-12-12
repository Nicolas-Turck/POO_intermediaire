from car import *
from bus import *
from vehicules import *
if __name__ == '__main__':
    car = Car(1000, 5, "blue")
    bus = Bus(2000,2, 1, "red")
    car.display()
    car.color = "green"
    car.display()
    bus.display()
    bus.numb_stage = 2
    bus.display()