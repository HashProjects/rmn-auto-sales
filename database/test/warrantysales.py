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
from database.warranty import Warranty
from database.warrantysale import WarrantySale


DB = Database()


customer = random.choice(DB.searchCustomers())
vehicles = DB.searchVehicles(vehicle_sold=False)
vehicle = random.choice(vehicles)
salespeople = DB.searchSalesPeople()
salesperson = random.choice(salespeople)

warranty = Warranty(0, 0, "2022-04-22", 24, 4000, 500)
warrantyItem = DB.searchWarrantyItems()
warranty.addWarrantyItem(random.choice(warrantyItem))

warrantySale = WarrantySale(0, 0, 0, "None", "2022-04-22", 1000, 100, 0)
warrantySale.setItems(vehicle, customer, salesperson)

warrantySale.addWarranty(warranty)



warrantySaleId = DB.purchaseWarranty(warrantySale)

DB.getWarrantyReport(warrantySaleId)

DB.close()
# except TypeError:
#    DB.close()
