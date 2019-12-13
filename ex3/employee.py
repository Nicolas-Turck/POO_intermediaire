from person import *

class Employee(Person):

    def __init__(self, status, name, first_name, years):
        """method of constructor of constructor of attributs
            and ask mother class with method super()"""
        super().__init__(name, first_name, years)

        self.status = "employée"

    def __repr__(self):
        """display employee attributs with specials method of python"""
        return "employee :\n\
        name:{},\n\
        first name:{},\n\
        years:{},\n\
        status:{},".format(self.name, self.first_name, self.years,self.status)