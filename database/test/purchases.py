import sys
import os

from database import vehicleproblem, vehicle

sys.path.insert(1, os.path.abspath("../.."))

from database.purchase import Purchase
from database.database import Database
from database.vehiclepurchase import VehiclePurchase
from database.seller import Seller

newCar = vehicle.generateRandomVehicle()

newCar2 = vehicle.generateRandomVehicle()

seller = Seller(0, "Sam Used Car Lot", "3521 Mayberry Ave", "Phoenix", "Arizona", "87469", "585-228-2292",
                "11-19139391")

vehiclepurchase1 = VehiclePurchase(0, 0, 4000, 4000)
vehiclepurchase1.addProblem(vehicleproblem.generateRandomProblem())
vehiclepurchase1.addProblem(vehicleproblem.generateRandomProblem())
vehiclepurchase2 = VehiclePurchase(0, 1, 5000, 5000)
vehiclepurchase2.addProblem(vehicleproblem.generateRandomProblem())
vehiclepurchase2.addProblem(vehicleproblem.generateRandomProblem())
vehiclepurchase2.addProblem(vehicleproblem.generateRandomProblem())
DB = Database()

#try:

samUsedCarLot = DB.getSellerByTaxId('11-19139391')
if seller is None:
    seller_id = DB.insertSeller(seller)
else:
    seller_id = samUsedCarLot.seller_id

purchase = Purchase(0, "2022-04-19", seller_id, False)

purchase_id = DB.purchase(purchase, [newCar, newCar2], [vehiclepurchase1, vehiclepurchase2])

DB.getPurchaseReport(purchase_id)

DB.close()
#except TypeError:
#    DB.close()
