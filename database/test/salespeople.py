import datetime
import random
import sys
import os

from database import vehicleproblem, vehicle, customer, employment, salesperson

# sys.path.insert(1, os.path.abspath("../.."))

from database.purchase import Purchase
from database.database import Database
from database.vehiclepurchase import VehiclePurchase
from database.seller import Seller

sp = salesperson.generateRandomSalesPerson()

DB = Database()


DB.insertSalesPerson(sp)

print(DB.searchSalesPeople(sp.salesperson_name)[0])

print("Display all sales people")
for person in DB.searchSalesPeople():
    print(person)

DB.close()
# except TypeError:
#    DB.close()