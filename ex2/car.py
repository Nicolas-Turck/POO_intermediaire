class Car:


    doors = (3,5)

    def __init__(self, numbers_doors, colors):
        self.__numbers_doors = numbers_doors
        self.__color = colors
        self.__immat = 54766

    @property
    def numbers_doors(self):
        return self.__numbers_doors

    @numbers_doors.setter
    def numbers_doors(self, numbers_doors):
        if numbers_doors in Car.doors:
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

