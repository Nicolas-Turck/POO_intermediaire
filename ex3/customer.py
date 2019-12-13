from person import *
from product import *

class Customer(Person):


    def __init__(self, name, first_name, years):
        """method  of constructor of attributs
            and ask mother class with method super()"""
        super().__init__(name, first_name, years)
        self.basket = []
        self.totals = 0
        #self.product = products

    def add_elem(self, elem):
        """method for add elem in list customer"""
        #if other in Product.store:
        self.basket.append(elem)

    def __repr__(self):
        """display customer attributes with specials method of python """
        return "client:\n \
        name:{},\n\
        first name:{},\n\
        years:{},\n \
        basket:{},\n\
        totals:{},\n".format(self.name, self.first_name, self.years, self.basket, self.totals)