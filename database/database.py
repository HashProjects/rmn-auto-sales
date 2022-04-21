import mysql.connector
import random

from database.customer import Customer
from database.employment import CustomerEmployment
from database.sale import VehicleSale
from database.salesperson import SalesPerson
from database.seller import Seller
from database.vehicle import Vehicle
from database.purchase import Purchase
from database.vehicleproblem import VehicleProblem
from database.vehiclepurchase import VehiclePurchase
from database.warrantyitem import WarrantyItem


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
        return Customer.fromNamedTuple(result)

    def getVehicleById(self, vehicle_id):
        cursor = self.query("SELECT * FROM vehicle WHERE `vehicle_id` = {}".format(vehicle_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return Vehicle.fromNamedTuple(result)

    def getSellerByTaxId(self, tax_id):
        cursor = self.query("SELECT * FROM seller WHERE `seller_tax_id` = '{}'".format(tax_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return Seller.fromNamedTuple(result)

    def getPurchaseById(self, purchase_id):
        cursor = self.query("SELECT * FROM purchase WHERE `purchase_id` = '{}'".format(purchase_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return Purchase.fromNamedTuple(result)

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

    def getSalesPersonById(self, salesperson_id):
        cursor = self.query("SELECT * FROM sales_people WHERE `salesperson_id` = {}".format(salesperson_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return SalesPerson.fromNamedTuple(result)

    def searchSalesPeople(self, salesperson_name=None, salesperson_phone=None):
        query = "SELECT * FROM sales_people"

        if is_not_empty(salesperson_name) or is_not_empty(salesperson_phone):
            # add where clauses
            query += " WHERE "
            needsAnd = False
            if salesperson_name is not None:
                query += " `salesperson_name` = '{}'".format(salesperson_name)
                needsAnd = True

            if salesperson_phone is not None:
                query = appendAndIfNeeded(query, needsAnd)
                query += " `salesperson_phone` = '{}'".format(salesperson_phone)
                needsAnd = True

        cursor = self.query(query)
        result = []
        for row in cursor:
            result.append(SalesPerson.fromNamedTuple(row))
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
        query = """INSERT INTO `customer` (customer_phone, customer_last_name, customer_first_name, customer_address, 
        customer_city, customer_state, customer_zip, customer_gender, customer_dob, customer_taxpayer_id) VALUES ('{
        }', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            customer.customer_phone, customer.customer_last_name,
            customer.customer_first_name, customer.customer_address, customer.customer_city,
            customer.customer_state, customer.customer_zip, customer.customer_gender,
            customer.customer_dob, customer.customer_taxpayer_id)
        cursor = self.query(query)
        self.cnx.commit()
        cursor.close()

    def insertSeller(self, seller):
        query = """INSERT INTO `seller` (seller_id, seller_name, seller_address, seller_city, seller_state, 
        seller_zip, seller_phone , seller_tax_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            seller.seller_id, seller.seller_name, seller.seller_address, seller.seller_city, seller.seller_state
            , seller.seller_zip, seller.seller_phone, seller.seller_tax_id)
        cursor = self.query(query)
        result = cursor.glastrowid
        self.cnx.commit()
        cursor.close()
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

    def purchase(self, purchase, vehicles, vehiclepurchases):

        query = "INSERT into `purchase` (`purchase_date`, `seller_id`, `auction`) VALUES ('{}','{}', '{}')".format(
            purchase.purchase_date, purchase.seller_id, int(purchase.auction))
        cursor = self.query(query)

        purchase_id = cursor.lastrowid

        for i in range(0, len(vehicles)):
            vehicle = vehicles[i]
            query = """INSERT INTO `vehicle` (`vehicle_vin`, `vehicle_make`, `vehicle_model`, `vehicle_year`, 
                    `vehicle_color`, `vehicle_miles`, `vehicle_condition`, `vehicle_style`, `vehicle_interior_color`, 
                    `vehicle_list_price`, `vehicle_sale_price`, `vehicle_sold`) VALUES ('{}', '{}', '{}', '{}', '{}', 
                    '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                vehicle.vehicle_vin, vehicle.vehicle_make, vehicle.vehicle_model, vehicle.vehicle_year,
                vehicle.vehicle_color,
                vehicle.vehicle_miles, vehicle.vehicle_condition, vehicle.vehicle_style, vehicle.vehicle_interior_color,
                vehicle.vehicle_list_price, vehicle.vehicle_sale_price, vehicle.vehicle_sold)
            cursor = self.query(query)
            vehicle_id = cursor.lastrowid

            query = """INSERT INTO `vehicle_purchase` (`purchase_id`, `vehicle_id`, `book_price`, `price_paid`) 
            VALUES ('{}', '{}', '{}', '{}')""".format(
                purchase_id, vehicle_id, vehiclepurchases[i].book_price, vehiclepurchases[i].price_paid)

            self.query(query)

            problems = vehiclepurchases[i].vehicle_problems
            problem_id = 1
            for vehicleproblem in problems:
                query = """INSERT INTO `vehicle_problems` (`purchase_id`, `vehicle_id`, `problem_id`, `problem_description`, `estimated_repair_cost`) 
                VALUES ('{}', '{}', '{}', '{}', '{}')""".format(purchase_id, vehicle_id, problem_id,
                                                                vehicleproblem.problem_description,
                                                                vehicleproblem.estimated_repair_cost)
                problem_id += 1
                self.query(query)

        # commit these changes
        self.cnx.commit()
        return purchase_id

    def getVehiclePurchases(self, purchase_id):
        query = "SELECT * from vehicle_purchase WHERE purchase_id = '{}'".format(purchase_id)
        cursor = self.query(query)
        result = []
        if cursor.rowcount:
            for vehiclePurchase in cursor:
                result.append(VehiclePurchase.fromNamedTuple(vehiclePurchase))
        cursor.close()
        return result

    def getVehicleProblems(self, purchase_id, vehicle_id):
        query = "SELECT * from vehicle_problems WHERE purchase_id = '{}' AND vehicle_id ='{}'".format(purchase_id,
                                                                                                      vehicle_id)
        cursor = self.query(query)
        result = []
        if cursor.rowcount:
            for problem in cursor:
                result.append(VehicleProblem.fromNamedTuple(problem))
        cursor.close()
        return result

    def insertSalesPerson(self, salesperson):
        query = """INSERT INTO `sales_people` (`salesperson_name`, `salesperson_phone`) VALUES ('{}', '{}')""".format(
            salesperson.salesperson_name, salesperson.salesperson_phone)
        cursor = self.query(query)
        result = cursor.lastrowid
        self.cnx.commit()
        cursor.close()
        return result

    def getPurchaseReport(self, purchase_id):
        purchase = self.getPurchaseById(purchase_id)

        vehiclepurchases = self.getVehiclePurchases(purchase_id)

        print(purchase)

        for vp in vehiclepurchases:
            print(vp)
            vehicle = self.getVehicleById(vp.vehicle_id)
            print("  ", vehicle)

            problems = self.getVehicleProblems(purchase.purchase_id, vp.vehicle_id)
            for problem in problems:
                print("    ", problem)

    def getWarrantyItemByName(self, warrantyItemName):
        cursor = self.query("SELECT * FROM warranty_item WHERE `item_description` = '{}'".format(warrantyItemName))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        if result is not None:
            return WarrantyItem.fromNamedTuple(result)
        else:
            return None

    def insertWarrantyItem(self, warranty_item):
        query = """INSERT INTO `warranty_item` (`item_description`) VALUES ('{}')""".format(
            warranty_item.item_description)
        cursor = self.query(query)
        self.cnx.commit()
        cursor.close()

    def sellVehicle(self, vehicleSale):

        customer = vehicleSale.customer
        # we need to skip this insert if the customer exists
        query = """
        INSERT INTO `customer` (customer_phone, customer_last_name, customer_first_name, customer_address, 
        customer_city, customer_state, customer_zip, customer_gender, customer_dob, customer_taxpayer_id) VALUES ('{}', 
        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
        """.format(
            customer.customer_phone, customer.customer_last_name,
            customer.customer_first_name, customer.customer_address, customer.customer_city,
            customer.customer_state, customer.customer_zip, customer.customer_gender,
            customer.customer_dob, customer.customer_taxpayer_id)

        cursor = self.query(query)
        customer_id = cursor.lastrowid

        query = """INSERT into `sale` (sale_id, sale_date, total_due, down_payment, financed_amount, 
        employee_id, employee_commission, vehicle_id, customer_id) VALUES ('{}','{}', 
        '{}','{}', '{}','{}', '{}','{}', '{}')""".format(vehicleSale.sale_id, vehicleSale.sale_date,
                                                         vehicleSale.total_due,
                                                         vehicleSale.down_payment, vehicleSale.financed_amount,
                                                         vehicleSale.employee_id,
                                                         vehicleSale.employee_commission, vehicleSale.vehicle_id,
                                                         customer_id)
        cursor = self.query(query)

        sale_id = cursor.lastrowid

        query = "UPDATE `vehicle` SET `vehicle_sold` = '1' WHERE `vehicle_id` = '{}'".format(vehicleSale.vehicle_id)
        self.query(query)

        employmentIndex = 0
        for i in range(0, len(vehicleSale.customer_employment)):
            customer_employment = vehicleSale.customer_employment[i]
            employmentIndex += 1
            query = """INSERT INTO `employment` (customer_id, employment_id, employer, title, supervisor, supervisor_phone, employer_address,
                 start_date, end_date) VALUES ('{}', '{}', '{}', '{}', '{}', 
                    '{}', '{}', '{}', '{}')""".format(
                customer_id,
                employmentIndex,
                customer_employment.employer,
                customer_employment.title,
                customer_employment.supervisor,
                customer_employment.supervisor_phone,
                customer_employment.employer_address,
                customer_employment.start_date,
                customer_employment.end_date)
            cursor = self.query(query)
            employment_id = cursor.lastrowid

        # commit these changes
        self.cnx.commit()
        return sale_id

    def getSaleReport(self, sale_id):
        sale = self.getVehicleSaleById(sale_id)

        vehicle = self.getVehicleById(sale.vehicle_id)

        customer = self.getCustomerById(sale.customer_id)

        history = self.getCustomerEmploymentHistory(customer.customer_id)

        print(sale)
        print("  ", customer)
        for item in history:
            print("    ", item)
        print("  ", vehicle)

    def getVehicleSaleById(self, sale_id):
        cursor = self.query("SELECT * FROM sale WHERE `sale_id` = {}".format(sale_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return VehicleSale.fromNamedTuple(result)

    def getCustomerEmploymentHistory(self, customerId):
        cursor = self.query("SELECT * FROM employment WHERE `customer_id` = {}".format(customerId))
        result = []
        for item in cursor:
            result.append(CustomerEmployment.fromNamedTuple(item))
        self.closeCursor(cursor)
        return result
