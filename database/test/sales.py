import datetime
import random
import sys
import os

from database import vehicleproblem, vehicle, customer, employment, sale

# sys.path.insert(1, os.path.abspath("../.."))

from database.purchase import Purchase
from database.database import Database
from database.sale import VehicleSale
from database.customer import Customer
from database.vehiclepurchase import VehiclePurchase
from database.seller import Seller

newCustomer = customer.generateRandomCustomer()

employmentHistory = []
employmentHistory.append(employment.generateRandomEmployment(newCustomer))
employmentHistory.append(employment.generateRandomEmployment(newCustomer))

DB = Database()

vehicles = DB.searchVehicles(vehicle_sold=False)
vehicle = random.choice(vehicles)

salespeople = DB.searchSalesPeople()
salesperson = random.choice(salespeople)

vehicleSale = VehicleSale(0, "2022-4-21", vehicle.vehicle_list_price + 3000, vehicle.vehicle_list_price, 3000,
                          salesperson.salesperson_id,
                          1000, 0, 0)
vehicleSale.setVehicle(vehicle)
vehicleSale.setCustomer(newCustomer)
vehicleSale.setCustomEmployment(employmentHistory)

sale_id = DB.sellVehicle(vehicleSale)

DB.getSaleReport(sale_id)

DB.close()
# except TypeError:
#    DB.close()
