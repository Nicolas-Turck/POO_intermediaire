from person import *
from employee import *
from customer import *
from product import *

if __name__=='__main__':
    client1 = Customer("turck", "nicos", 34)
    employee1 = Employee("manager", "eder", "nunes", 34)
    macbook = Product("macbook", 1600)
    iphone = Product("iphone", 800)
    airpods = Product("airpods", 150)
    client1.__add__("iphone")
    client1.__add__("macbook")
    print(client1)
    print(employee1)