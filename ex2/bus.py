from vehicules import *
class Bus(Vehicules):

    def __init__(self, immats, numbers_doors, numb_stage, colors):
        Vehicules.__init__(self)
        self.__numbers_doors = numbers_doors
        self.__numbers_stage = numb_stage
        self.__immat = immats
        self.__color = colors

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
        if numbers_doors in doors:
            self.__numbers_doors = numbers_doors
        else:
            raise ValueError

    @property
    def numbers_stage(self):
        return self.__numbers_stage

    @numbers_stage.setter
    def numbers_stage(self, numb_stage=None):
        if numb_stage in Vehicules.stage:
            self.__numbers_stage = numb_stage
        else:
            raise ValueError

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, colors):
        self.__color = colors

    def display(self):
        print("...Bus:\nimmat:{}\ncolors:{}\nnumber doors:{}\nstage:{}".format(self.immat, self.__color, self.__numbers_doors, self.__numbers_stage) )