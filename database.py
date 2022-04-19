import mysql.connector
import random
from vehicle import Vehicle


def appendAndIfNeeded(query, needsAnd):
    if needsAnd:
        return query + " AND "
    return query


def is_not_empty(value):
    try:
        return value is not None and len(value) > 0
    except TypeError:
        return True


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

    def getCustomerById(self, customer_id):
        cursor = self.query("SELECT * FROM customer WHERE `customer_id` = {}".format(customer_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return result

    def getVehicleById(self, vehicle_id):
        cursor = self.query("SELECT * FROM vehicle WHERE `vehicle_id` = {}".format(vehicle_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return result

    def searchCustomers(self, customer_last_name=None, customer_first_name=None, customer_taxpayer_id=None):
        query = "SELECT * FROM customer"

        if is_not_empty(customer_last_name) or is_not_empty(customer_first_name) or is_not_empty(customer_taxpayer_id):
            # add where clauses
            query += " WHERE "
            needsAnd = False
            if customer_last_name is not None:
                query += " `customer_last_name` = '{}'".format(customer_last_name)
                needsAnd = True

            if customer_first_name is not None:
                query = appendAndIfNeeded(query, needsAnd)
                query += " `customer_first_name` = '{}'".format(customer_first_name)
                needsAnd = True

            if customer_taxpayer_id is not None:
                query = appendAndIfNeeded(query, needsAnd)
                query += " `customer_taxpayer_id` = '{}'".format(customer_taxpayer_id)

        print(query)
        cursor = self.query(query)
        result = []
        for row in cursor:
            result.append(row)
        self.closeCursor(cursor)
        return result

    def searchVehicles(self, vehicle_make=None, vehicle_model=None, vehicle_year=None, vehicle_color=None,
                       vehicle_miles=None,
                       vehicle_condition=None, vehicle_style=None, vehicle_interior_color=None, vehicle_list_price=None,
                       vehicle_sale_price=None,
                       vehicle_sold=None):
        query = "SELECT * FROM vehicle"
        if is_not_empty(vehicle_make) or is_not_empty(vehicle_model) or is_not_empty(vehicle_year) or is_not_empty(
                vehicle_color) or is_not_empty(vehicle_miles) or is_not_empty(vehicle_condition) or is_not_empty(
            vehicle_style) or is_not_empty(vehicle_interior_color) or is_not_empty(vehicle_list_price) or is_not_empty(
            vehicle_sale_price) or is_not_empty(vehicle_sold):
            # add where clauses
            query += " WHERE "
            needsAnd = False
            if is_not_empty(vehicle_make):
                query += " `vehicle_make` = '{}'".format(vehicle_make)
                needsAnd = True

            if is_not_empty(vehicle_model):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_model` = '{}'".format(vehicle_model)
                needsAnd = True

            if is_not_empty(vehicle_year):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_year` = '{}'".format(vehicle_year)
                needsAnd = True

            if is_not_empty(vehicle_color):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_color` = '{}'".format(vehicle_color)
                needsAnd = True

            if is_not_empty(vehicle_miles):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_miles` <= '{}'".format(vehicle_miles)
                needsAnd = True

            if is_not_empty(vehicle_condition):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_condition` = '{}'".format(vehicle_condition)
                needsAnd = True

            if is_not_empty(vehicle_style):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_style` = '{}'".format(vehicle_style)
                needsAnd = True

            if is_not_empty(vehicle_interior_color):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_interior_color` = '{}'".format(vehicle_interior_color)
                needsAnd = True

            if is_not_empty(vehicle_list_price):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_list_price` <= '{}'".format(vehicle_list_price)
                needsAnd = True

            if is_not_empty(vehicle_sale_price):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_sale_price` = '{}'".format(vehicle_sale_price)
                needsAnd = True

            if is_not_empty(vehicle_sold):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `vehicle_sold` = '{}'".format(vehicle_sold)

        print(query)
        cursor = self.query(query)
        result = []
        for row in cursor:
            result.append(row)
        self.closeCursor(cursor)
        return result

    def insertCustomer(self, customer):
        query = """INSERT INTO `customer` (customer_phone, customer_last_name, customer_first_name, customer_address, customer_city,
                 customer_state, customer_zip, customer_gender, customer_dob, customer_taxpayer_id) VALUES ('{}', '{}', '{}', '{}', '{}', 
        '{}', '{}', '{}', '{}', '{}')""".format(
            customer.customer_phone, customer.customer_last_name,
            customer.customer_first_name, customer.customer_address, customer.customer_city,
            customer.customer_state, customer.customer_zip, customer.customer_gender,
            customer.customer_dob, customer.customer_taxpayer_id)
        cursor = self.query(query)
        self.cnx.commit()
        cursor.close()

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
