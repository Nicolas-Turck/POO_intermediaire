from  vehicules import  *

class Car(Vehicules):


    def __init__(self, immats, numbers_doors, colors):
        Vehicules.__init__(self)
        self.__numbers_doors = numbers_doors
        self.__color = colors
        self.__immat = immats

    @property
    def immat(self):
        return self.__immat
    @immat.setter
    def immat(self, immats):
        self.__immat = immats


    @property
    def numbers_doors(self):
        return self.__numbers_doors

    @numbers_doors.setter
    def numbers_doors(self, numbers_doors):

        if numbers_doors in Vehicules.doors:
            self.__numbers_doors = numbers_doors
        else:
            raise ValueError

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, colors=None):
        self.__color = colors

    def display(self):
        print("...Car: \nimmat: {} \ncolors: {} \nnumber doors: {}".format(self.__immat, self.__color, self.__numbers_doors) )

