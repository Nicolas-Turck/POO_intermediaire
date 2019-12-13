from person import *
from employee import *
from customer import *
from product import *

if __name__=='__main__':

    client1 = Customer("turck", "nicos", 34)
    employee1 = Employee("manager", "eder", "nunes", 34)
    # create many items of store
    macbook = Product("macbook", 1600)
    macbook.add_store("macbook", 1600)
    iphone = Product("iphone", 800)
    iphone.add_store("iphone", 800)
    airpods = Product("airpods", 150)
    airpods.add_store("airpods", 150)
    #print(Product.store)
    # ask method for client add item in this basket
    client1.add_elem("iphone")
    client1.add_elem("macbook")
    print(client1)
    print(employee1)