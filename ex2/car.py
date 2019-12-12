class Car:
    immat = 249845
    colors = "blue"
    doors = (3,5)

    def __init__(self, numbers_doors):
        self.__numbers_doors = numbers_doors

    @property
    def numbers_doors(self):
        return self.__numbers_doors

    @numbers_doors.setter
    def numbers_doors(self, numbers_doors):
        if numbers_doors in Clio.doors:
            self.__numbers_doors = numbers_doors
        else:
            raise ValueError

    def display(self):
        print("car immat is {} and colors is {} number doors is {}".format(self.immat, self.colors, self.__numbers_doors) )

