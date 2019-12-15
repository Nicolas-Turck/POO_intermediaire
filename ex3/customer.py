from person import *
from product import *

class Customer(Person):
    """class for create client and saved is product
    in baket list and adding price in total """
    def __init__(self, name, first_name, years):
        """method  of constructor of attributs
            and ask mother class with method super()"""
        super().__init__(name, first_name, years)
        self.basket = []
        self.totals = 0

    def __add__(self, other):
        """method for add elem in list customer
        and adding price after verify if product is
        in dictionnay"""
        if other in Product.store:
            self.basket.append(other)
        for cle, valeur in Product.store.items():
                if cle == other:
                    self.totals += valeur

    def __repr__(self):
        """display customer attributes with specials method of python """
        return "client:\n \
        name:{},\n\
        first name:{},\n\
        years:{},\n \
        basket:{},\n\
        totals:{},\n".format(self.name, self.first_name, self.years, self.basket, self.totals)