import random
import sys
import os

sys.path.insert(1, os.path.abspath(".."))
from vehicle import Vehicle
from database import Database

# example program

db = Database()

cursor = db.query("SELECT  * FROM vehicle WHERE `vehicle_year` = 2016")

car = None
for a in cursor:
    car = Vehicle.fromNamedTuple(a)
    print(car)
    print(a)
db.closeCursor(cursor)

car2 = db.getVehicleById(car.vehicle_id)
print(car2)

newCar = Vehicle(0, "{}N{}".format(random.randint(0, 178739393), random.randint(0, 30)),
                 random.choice(["Infinity", "Toyota", "Ford", "GCM"]),
                 "Car", random.randint(2010, 2022), "Red", random.randint(10000, 10000),
                 random.choice(["Good", "Fair", "Excellent"]), random.choice(["Sedan", "Van", "Coupe", "Truck"]),
                 random.randint(40, 100) * 100, random.randint(50, 110) * 100, 0)

# db.insertVehicle(newCar)

print("----------------------------------------")
cursor = cursor = db.query("SELECT  * FROM vehicle")
for a in cursor:
    print(a)

print("show Toyotas----------------------------")
toyotas = db.searchVehicles(vehicle_make="Toyota")
for c in toyotas:
    print(Vehicle.fromNamedTuple(c))

print("show 2018----------------------------")
toyotas = db.searchVehicles(vehicle_year="2018")
for c in toyotas:
    print(Vehicle.fromNamedTuple(c))

print("show Good Condition----------------------------")
toyotas = db.searchVehicles(vehicle_condition="Good")
for c in toyotas:
    print(Vehicle.fromNamedTuple(c))

print("show Good Condition and less than 10000-----------------")
toyotas = db.searchVehicles(vehicle_condition="Good", vehicle_list_price=10000)
for c in toyotas:
    print(Vehicle.fromNamedTuple(c))

db.closeCursor(cursor)

db.close()
