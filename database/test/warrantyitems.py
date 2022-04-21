import random
import sys
import os

from database.warrantyitem import WarrantyItem
from database.database import Database

# example program

db = Database()


warrantyitemlist = {
    "Tire": 100,
    "Drivetrain": 100,
    "Windows": 100,
    "Battery": 100,
    "Paint": 1000,
    "Headlights": 100,
    "Entire Vehicle": 2000
}

car = None
for k in warrantyitemlist:
    if db.getWarrantyItemByName(k) is None:
        db.insertWarrantyItem(WarrantyItem(0, k))

results = db.query("SELECT * FROM warranty_item")

for r in results:
    print(r)


db.close()
