class Product:
    store = {}

    def __init__(self,name, price):
        """class for create items in applestore """

        self.price = price
        self.name = name

    def add_store(self, key, values):
        """method for add items in store dictionnary """
        self.store.update({key: values})

