from  vehicules import  *
""""class for create object car with attributes 
    and use heritage of class vehicules"""
class Car(Vehicules):
    doors = (3, 5)

    def __init__(self, nunmbers_doors, immats, colors):
        """constructor of object and ask constructor of class vehicules"""
        self.numbers_doors = nunmbers_doors
        super().__init__(immats, colors)

    @property
    def numbers_doors(self):
        """get attributes"""
        return self.__numbers_doors

    @numbers_doors.setter
    def numbers_doors(self, numbers_doors):
        """verify attributes and retur it modify"""
        if numbers_doors in  Car.doors:
            self.__numbers_doors = numbers_doors
        else:
            self.__numbers_doors = False






