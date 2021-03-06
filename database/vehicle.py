import mysql.connector
import random


class Vehicle:
    @classmethod
    def fromNamedTuple(cls, vehicle_info):
        return cls(vehicle_info.vehicle_id, vehicle_info.vehicle_vin, vehicle_info[2], vehicle_info[3], vehicle_info[4],
                   vehicle_info[5], vehicle_info[6], vehicle_info[7], vehicle_info[8], vehicle_info[9],
                   vehicle_info[10], vehicle_info[11], vehicle_info[12], vehicle_info.vehicle_repaired)

    def __init__(self,
                 vehicle_id, vehicle_vin, vehicle_make, vehicle_model, vehicle_year, vehicle_color, vehicle_miles,
                 vehicle_condition, vehicle_style, vehicle_interior_color, vehicle_list_price, vehicle_sale_price,
                 vehicle_sold=0, vehicle_repaired=0):
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
        self.vehicle_repaired = vehicle_repaired

    def __str__(self):
        return "Vehicle({}, {}, {} {}, {}, color={}, condition={}, list={}, sold={}, repaired={})".format(
            self.vehicle_id,
            self.vehicle_vin,
            self.vehicle_make,
            self.vehicle_model,
            self.vehicle_year,
            self.vehicle_color,
            self.vehicle_condition,
            self.vehicle_list_price,
            self.vehicle_sold,
            self.vehicle_repaired)

    def getHtml(self):
        html = """<p><b>Year:</b> {} <b>Make:</b> {} <b>Model:</b> {}<br/>
                  <b>VIN:</b> {}<br/>
                  <b>Color:</b> {}<br/>
                  <b>Miles:</b>{:,}<br/>
                  <b>Condition:</b> {}<br/>
                  <b>Style:</b> {}<br/>
                  <b>Interior:</b> {}<br/>
                  <b>List Price:</b> {}
                  </p>
        """.format(self.vehicle_year, self.vehicle_make, self.vehicle_model,
                   self.vehicle_vin, self.vehicle_color, self.vehicle_miles,
                   self.vehicle_condition, self.vehicle_style,
                   self.vehicle_interior_color, self.vehicle_list_price)

        return html

    def getText(self):
        html = "Year: {} Make: {} Model: {}\n" \
               "VIN: {}\n" \
               "Color: {} \nMiles: {:,}\n Condition: {}\n Style: {}\n Interior: {}\n List:{}".format(self.vehicle_year, self.vehicle_make, self.vehicle_model,
                                          self.vehicle_vin, self.vehicle_color, self.vehicle_miles,
                                          self.vehicle_condition, self.vehicle_style,
                                          self.vehicle_interior_color, self.vehicle_list_price)

        return html


realCars = {
    "Ct200h": "Lexus",
    "Accord": "Honda",
    "Camry": "Toyota",
    "LX": "Lexus",
    "Civic": "Honda",
    "HR-V": "Honda",
    "CR-V": "Honda",
    "Corolla": "Toyota",
    "RAV4": "Toyota",
    "Venza": "Toyota",
    "Tacoma": "Toyota",
    "Sienna": "Toyota",
    "Yaris": "Toyota",
    "Blazer": "Chevy",
    "Mustang": "Ford",
    "Astro": "Chevy",
    "Q30": "Infinity"
}


def generateRandomVehicle():
    listModels = []
    for k in realCars.keys():
        listModels.append(k)

    model = random.choice(listModels)
    return Vehicle(0, "{}N{}".format(random.randint(0, 178739393), random.randint(0, 30)),
                   realCars[model],
                   model, random.randint(2010, 2022),
                   random.choice(["Red", "Blue", "Silver", "White", "Black"]),
                   random.randint(10000, 10000),
                   random.choice(["Good", "Fair", "Excellent"]),
                   random.choice(["Sedan", "Van", "Coupe", "Truck"]),
                   random.choice(["Brown", "Gray", "Black"]),
                   random.randint(40, 100) * 100, random.randint(50, 110) * 100, random.randint(50, 110) * 100)
