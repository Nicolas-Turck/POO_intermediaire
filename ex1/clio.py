class Clio:
    """create attributes of classe"""
    colors = {"noir": 123456, "bleu": 654321}
    doors = (3,5)
    price_range = [8000, 30000]
    price = 12000

    def __init__(self, numbers_doors, color, color_numbers):
        """create attributes of object"""
        self.__numbers_doors = numbers_doors
        self.__color_numbers = color_numbers
        self.__color = color
    
    @property
    def numbers_doors(self):
        """method for get attributes"""
        return self.__numbers_doors

    @numbers_doors.setter
    def numbers_doors(self, numbers_doors):
        """method for change attributes """
        if numbers_doors in Clio.doors:
            self.__numbers_doors = numbers_doors
        else:
            raise ValueError
    
    @property
    def color(self):
        """method for get attributes"""
        return self.__color

    @color.setter
    def color(self, coor):
        """method for verify and change attributes"""
        if color in Clio.colors.keys():
            self.__color = color
        else :
            raise ValueError
    
    @property
    def color_numbers(self):
        """method for get attributes """
        return self.__color_numbers

    @color_numbers.setter
    def color_numbers(self, color):
        """method for change attributes"""
        for  keys, values in colors.items():
            if self.__color_numbers == color.values:
                    self.__color_numbers = values
        #if self.__color in Clio.colors.keys():
            #self.__color_numbers += Clio.colors.values()
            else:
                raise ValueError

  

    @classmethod
    def check_price(cls):
        
        if cls.price_range[0] <= price <= cls.price_range[1]:
            return cls.price
        else:
            raise ValueError
