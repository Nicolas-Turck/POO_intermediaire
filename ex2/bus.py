class Bus:

    colors = "yellow"
    doors = (2,3)
    stage = (1,2)
    def __init__(self, immats, numbers_doors, numbers_stage):
        self.__numbers_doors = numbers_doors
        self.__numbers_stage = numbers_stage
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
        if numbers_doors in Bus.doors:
            self.__numbers_doors = numbers_doors
        else:
            raise ValueError

    @property
    def numbers_stage(self):
        return self.__numbers_stage

    @numbers_stage.setter
    def numbers_stage(self, numbers_stage):
        if numbers_stage in Bus.stage:
            self.__numbers_stage = numbers_stage
        else:
            raise ValueError

    def display(self):
        print("...Bus:\nimmat:{}\ncolors:{}\nnumber doors:{}\nstage:{}".format(self.immat, self.colors, self.__numbers_doors, self.__numbers_stage) )