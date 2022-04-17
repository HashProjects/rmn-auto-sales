import random
import sys
import os

sys.path.insert(1, os.path.abspath(".."))
from customer import Customer
from database import Database

# example program

db = Database()

cursor = db.query("SELECT  * FROM customer")

car = None
for a in cursor:
    car = Customer.fromNamedTuple(a)
    print(car)
    print(a)
db.closeCursor(cursor)

if car is not None:
    car2 = db.getCustomerById(car.customer_id)
    print(car2)

newCustomer = Customer(0,
    "{}-{}-{}".format(random.randint(100, 1000), random.randint(100, 1000), random.randint(1000, 10000)),
                       random.choice(["Smith", "Nyugen", "Biden", "Trump", "Harris", "Newsome", "Johnson"]),
                       random.choice(["Donald", "Joe", "Kamala", "Ted", "Loan", "Gavin", "Eric", "Mohit", "Sammy"]),
                       "{} {} {}".format(random.randint(1000, 100000), random.choice(
                           ["Mockingbird", "Wayne Street", "Kent", "Martin Luther King Jr"]),
                                         random.choice(["Lane", "Blvd", "Street", "Road"])),
                       random.choice(["Fountain Valley", "Fullerton", "Placentia", "Orange", "Garden Grove", "Anaheim",
                                      "Newport Beach", "Irvine"]),
                       random.choice(["Fountain Valley", "California", "Texas", "Florida", "Nevada"]),
                       random.randint(10000, 10000),
                       random.choice(["Male", "Female"]),
                       "{}-{}-{}".format(random.randint(1, 13), random.randint(1, 31), random.randint(1970, 2000)),
                       "{}-{}-{}".format(random.randint(100, 1000), random.randint(10, 100),
                                         random.randint(1000, 10000)))

db.insertCustomer(newCustomer)

print("show all----------------------------")
customers = db.searchCustomers()
for c in customers:
    print(Customer.fromNamedTuple(c))


print("show Lastname Smith----------------------------")
customers = db.searchCustomers(customer_last_name="Smith")
for c in customers:
    print(Customer.fromNamedTuple(c))

print("show tax-payer id ----------------------------")
customers = db.searchCustomers(customer_taxpayer_id="876-14-6154")
for c in customers:
    print(Customer.fromNamedTuple(c))


db.closeCursor(cursor)

db.close()
