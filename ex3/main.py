from person import *
from employee import *
from customer import *
from product import *

if __name__=='__main__':
    # create two person a client and employee
    client1 = Customer("turck", "nicos", 34)
    employee1 = Employee("manager", "eder", "nunes", 34)
    # create many items of store
    macbook = Product("macbook", 1600)
    macbook.add_store("macbook", 1600)
    iphone = Product("iphone", 800)
    iphone.add_store("iphone", 800)
    airpods = Product("airpods", 150)
    airpods.add_store("airpods", 150)
    print(Product.store)
    client1 + "airpods"
    print(client1)
    client1 + "iphone"
    print(client1)
    print(employee1)
    print(employee1 >= "manager")
    print(employee1 >= "employée")