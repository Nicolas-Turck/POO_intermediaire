from vehicules import *
""""clas for create object bus with attributes 
    and use heritage of class vehicules"""
class Bus(Vehicules):
    stage = (1, 2)
    doors = (2, 3)
    def __init__(self, immats, numbers_doors, numb_stage, colors):
        """import attributs of constructor in class Vehicules"""
        Vehicules.__init__(self, immats, colors)
        self.__numbers_doors = numbers_doors
        self.__numbers_stage = numb_stage
        super().__init__(immats, colors)


    @property
    def numbers_doors(self):
        """get attributes"""
        return self.__numbers_doors
    @numbers_doors.setter
    def numbers_doors(self, numbers_doors):
        """return modify attributes"""
        if numbers_doors in Bus.doors:
            self.__numbers_doors = numbers_doors
        else:
            raise ValueError

    @property
    def numbers_stage(self):
        """get attributes"""
        return self.__numbers_stage
    @numbers_stage.setter
    def numbers_stage(self, numb_stage=None):
        """verify and return modify attributes"""
        if numb_stage in Bus.stage:
            self.__numbers_stage = numb_stage
        else:
            raise ValueError

    @property
    def color(self):
        """get attributes"""
        return self.__color
    @color.setter
    def color(self, colors):
        """return modify attributes"""
        self.__color = colors

