import mysql.connector
import random

class Vehicle:
    @classmethod
    def fromNamedTuple(cls, vehicle_info):
        return cls(vehicle_info.vehicle_id, vehicle_info.vehicle_vin, vehicle_info[2], vehicle_info[3], vehicle_info[4],
                   vehicle_info[5], vehicle_info[6], vehicle_info[7], vehicle_info[8], vehicle_info[9],
                   vehicle_info[10], vehicle_info[11], vehicle_info[12])

    def __init__(self,
                 vehicle_id, vehicle_vin, vehicle_make, vehicle_model, vehicle_year, vehicle_color, vehicle_miles,
                 vehicle_condition, vehicle_style, vehicle_interior_color, vehicle_list_price, vehicle_sale_price,
                 vehicle_sold=0):
        self.vehicle_id = vehicle_id
        self.vehicle_vin = vehicle_vin
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.vehicle_year = vehicle_year
        self.vehicle_color = vehicle_color
        self.vehicle_miles = vehicle_miles
        self.vehicle_condition = vehicle_condition
        self.vehicle_style = vehicle_style
        self.vehicle_interior_color = vehicle_interior_color
        self.vehicle_list_price = vehicle_list_price
        self.vehicle_sale_price = vehicle_sale_price
        self.vehicle_sold = vehicle_sold

    def __str__(self):
        return "Vehicle({}, {}, {}, {}, color={})".format(self.vehicle_id, self.vehicle_vin, self.vehicle_make,
                                                          self.vehicle_year, self.vehicle_color)


class Database:

    def __init__(self):
        self.username = 'admin'
        self.password = 'admin'
        self.host = '127.0.0.1'
        self.database = 'rmn_auto_sales'
        self.cnx = mysql.connector.connect(user=self.username, password=self.password, host=self.host,
                                           database=self.database)

    def close(self):
        self.cnx.close()

    def query(self, sql):
        cursor = self.cnx.cursor(named_tuple=True, buffered=True)
        cursor.execute(sql)
        return cursor

    def closeCursor(self, cursor):
        cursor.close()

    def getVehicleById(self, vehicle_id):
        cursor = self.query("SELECT * FROM vehicle WHERE `vehicle_id` = {}".format(vehicle_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return result

    def insertVehicle(self, vehicle):
        query = """INSERT INTO `vehicle` (`vehicle_vin`, `vehicle_make`, `vehicle_model`, `vehicle_year`, 
        `vehicle_color`, `vehicle_miles`, `vehicle_condition`, `vehicle_style`, `vehicle_interior_color`, 
        `vehicle_list_price`, `vehicle_sale_price`, `vehicle_sold`) VALUES ('{}', '{}', '{}', '{}', '{}', 
        '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            vehicle.vehicle_vin, vehicle.vehicle_make, vehicle.vehicle_model, vehicle.vehicle_year,
            vehicle.vehicle_color,
            vehicle.vehicle_miles, vehicle.vehicle_condition, vehicle.vehicle_style, vehicle.vehicle_interior_color,
            vehicle.vehicle_list_price, vehicle.vehicle_sale_price, vehicle.vehicle_sold)
        cursor = self.query(query)
        self.cnx.commit()
        cursor.close()



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



newCar = Vehicle(0, "{}N{}".format(random.randint(0, 178739393), random.randint(0,30)),
                 random.choice(["Infinity", "Toyota", "Ford", "GCM"]),
                "Car", random.randint(2010, 2022), "Red", random.randint(10000, 10000),
                 random.choice(["Good", "Fair", "Excellent"]), random.choice(["Sedan", "Van", "Coupe", "Truck"]),
                 random.randint(40, 100) * 100, random.randint(50, 110) * 100, 0)

db.insertVehicle(newCar)

print("----------------------------------------")
cursor = cursor = db.query("SELECT  * FROM vehicle")
for a in cursor:
    print(a)

db.closeCursor(cursor)

db.close()
