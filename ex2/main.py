from car import *
from bus import *

if __name__ == '__main__':
    car = Car(3, "blue")
    bus = Bus(2, 1)
    car.display()
    car.color = "green"
    car.display()
    bus.display()
    bus.numbers_stage = 2
    bus.display()