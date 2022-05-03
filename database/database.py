import mysql.connector
import random
import datetime
from database.customer import Customer
from database.employment import CustomerEmployment
from database.payment import Payment
from database.paymenthistory import PaymentHistory
from database.sale import VehicleSale
from database.salesperson import SalesPerson
from database.seller import Seller
from database.vehicle import Vehicle
from database.purchase import Purchase
from database.vehicleproblem import VehicleProblem
from database.vehiclepurchase import VehiclePurchase
from database.warranty import Warranty
from database.warrantyitem import WarrantyItem
from database.warrantyitemlist import WarrantyItemListEntry
from database.warrantysale import WarrantySale


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
        try:
            return Customer.fromNamedTuple(result)
        except:
            return None

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
            result = Seller.fromNamedTuple(cursor.fetchone())
        self.closeCursor(cursor)
        return result

    def getSellerById(self, seller_id):
        cursor = self.query("SELECT * FROM seller WHERE `seller_id` = '{}'".format(seller_id))
        result = None
        if cursor.rowcount > 0:
            result = Seller.fromNamedTuple(cursor.fetchone())
        self.closeCursor(cursor)
        return result

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
            if is_not_empty(customer_last_name):
                query += " `customer_last_name` = '{}'".format(customer_last_name)
                needsAnd = True

            if is_not_empty(customer_first_name):
                query = appendAndIfNeeded(query, needsAnd)
                query += " `customer_first_name` = '{}'".format(customer_first_name)
                needsAnd = True

            if is_not_empty(customer_taxpayer_id):
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

    def searchWarrantyItems(self, item_id=None, item_description=None):
        query = "SELECT * FROM warranty_item"

        if is_not_empty(item_id):
            # add where clauses
            query += " WHERE "
            if item_id is not None:
                query += " `item_id` = '{}'".format(item_id)

        if is_not_empty(item_description):
            # add where clauses
            query += " WHERE "
            if item_description is not None:
                query += " `item_description` = '{}'".format(item_description)

        cursor = self.query(query)
        result = []
        for row in cursor:
            result.append(WarrantyItem.fromNamedTuple(row))
        self.closeCursor(cursor)
        return result

    def searchVehicles(self, vehicle_make=None, vehicle_model=None, vehicle_year=None, vehicle_color=None,
                       vehicle_miles=None,
                       vehicle_condition=None, vehicle_style=None, vehicle_interior_color=None, vehicle_list_price=None,
                       vehicle_sale_price=None,
                       vehicle_sold=None,
                       vehicle_repaired=None):
        query = "SELECT * FROM vehicle"
        if is_not_empty(vehicle_make) or is_not_empty(vehicle_model) or is_not_empty(vehicle_year) or is_not_empty(
                vehicle_color) or is_not_empty(vehicle_miles) or is_not_empty(vehicle_condition) or is_not_empty(
            vehicle_style) or is_not_empty(vehicle_interior_color) or is_not_empty(vehicle_list_price) or is_not_empty(
            vehicle_sale_price) or is_not_empty(vehicle_sold) or is_not_empty(vehicle_repaired):
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
                isSold = 0
                if vehicle_sold:
                    isSold = 1
                query += " `vehicle_sold` = {}".format(isSold)
                needsAnd = True

            if is_not_empty(vehicle_repaired):
                query = appendAndIfNeeded(query, needsAnd)
                isRepaired = 0
                if vehicle_repaired:
                    isRepaired = 1
                query += " `vehicle_repaired` = {}".format(isRepaired)

        print(query)
        cursor = self.query(query)
        result = []
        for row in cursor:
            result.append(row)
        self.closeCursor(cursor)
        return result

    def insertCustomer(self, customer):
        query = """INSERT INTO `customer` (customer_phone, customer_last_name, customer_first_name, customer_address, 
        customer_city, customer_state, customer_zip, customer_gender, customer_dob, customer_taxpayer_id) VALUES ('{}', 
        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
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
        `vehicle_list_price`, `vehicle_sale_price`, `vehicle_sold`, `vehicle_repaired`) VALUES ('{}', '{}', '{}', '{}', '{}', 
        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            vehicle.vehicle_vin, vehicle.vehicle_make, vehicle.vehicle_model, vehicle.vehicle_year,
            vehicle.vehicle_color,
            vehicle.vehicle_miles, vehicle.vehicle_condition, vehicle.vehicle_style, vehicle.vehicle_interior_color,
            vehicle.vehicle_list_price, vehicle.vehicle_sale_price, vehicle.vehicle_sold, 1)
        cursor = self.query(query)
        self.cnx.commit()
        cursor.close()

    def purchase(self, purchase, vehiclepurchases):

        query = "INSERT into `purchase` (`purchase_date`, `seller_id`, `auction`) VALUES ('{}','{}', '{}')".format(
            purchase.purchase_date, purchase.seller_id, int(purchase.auction))
        cursor = self.query(query)

        purchase_id = cursor.lastrowid

        for i in range(0, len(vehiclepurchases)):
            vehicle = vehiclepurchases[i].vehicle
            isRepaired = 0
            if len(vehiclepurchases[i].vehicle_problems) == 0:
                isRepaired = 1
            else:
                isRepaired = 0

            isSold = 0
            if vehicle.vehicle_sold:
                isSold = 1
            query = """INSERT INTO `vehicle` (`vehicle_vin`, `vehicle_make`, `vehicle_model`, `vehicle_year`, 
                    `vehicle_color`, `vehicle_miles`, `vehicle_condition`, `vehicle_style`, `vehicle_interior_color`, 
                    `vehicle_list_price`, `vehicle_sale_price`, `vehicle_sold`, `vehicle_repaired`) VALUES ('{}', '{}', '{}', '{}', '{}', 
                    '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                vehicle.vehicle_vin, vehicle.vehicle_make, vehicle.vehicle_model, vehicle.vehicle_year,
                vehicle.vehicle_color,
                vehicle.vehicle_miles, vehicle.vehicle_condition, vehicle.vehicle_style, vehicle.vehicle_interior_color,
                vehicle.vehicle_list_price, vehicle.vehicle_sale_price, isSold, isRepaired)
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

    def getRemainingVehicleProblems(self, vehicle_id):
        query = "SELECT * from vehicle_problems WHERE vehicle_id ='{}' AND `actual_repair_cost` is NULL".format(
            vehicle_id)
        cursor = self.query(query)
        result = []
        if cursor.rowcount:
            for problem in cursor:
                result.append(VehicleProblem.fromNamedTuple(problem))
        cursor.close()
        return result

    def fixVehicleProblem(self, vehicle_id, vehicle_problem_id, cost):
        query = """UPDATE `vehicle_problems` SET `actual_repair_cost` = '{}' 
        WHERE `vehicle_id` = '{}' AND `problem_id` = {}""".format(cost, vehicle_id, vehicle_problem_id)
        self.query(query)

        query = "SELECT * from vehicle_problems WHERE vehicle_id ='{}' AND `actual_repair_cost` is NULL".format(
            vehicle_id)
        cursor = self.query(query)
        remainingRepairs = cursor.rowcount

        if remainingRepairs == 0:
            query = "UPDATE `vehicle` SET `vehicle_repaired` = '1' WHERE `vehicle_id` = '{}'".format(vehicle_id)
            self.query(query)

        self.cnx.commit()

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

        seller = self.getSellerById(purchase.seller_id)
        purchase.setSeller(seller)

        vehiclepurchases = self.getVehiclePurchases(purchase_id)

        print(purchase)

        for vp in vehiclepurchases:
            print(vp)
            vehicle = self.getVehicleById(vp.vehicle_id)
            vp.setVehicle(vehicle)
            print("  ", vehicle)

            problems = self.getVehicleProblems(purchase.purchase_id, vp.vehicle_id)
            vp.setVehicleProblems(problems)
            for problem in problems:
                print("    ", problem)

        purchase.setVehiclesPurchases(vehiclepurchases)
        return purchase

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
        query = "SELECT * FROM `customer` WHERE `customer_taxpayer_id` = {}".format(customer.customer_taxpayer_id)
        cursor = self.query(query)

        if cursor.rowcount == 0:
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
        else:
            customer_id = Customer.fromNamedTuple(cursor.fetchone()).customer_id

        cursor.close()

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
            query = """INSERT INTO `employment` (customer_id, employment_id, employer, title, supervisor, 
            supervisor_phone, employer_address, start_date, end_date) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', 
            '{}', '{}', '{}')""".format(
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
        vehicleSale = self.getVehicleSaleById(sale_id)

        vehicle = self.getVehicleById(vehicleSale.vehicle_id)
        vehicleSale.setVehicle(vehicle)

        customer = self.getCustomerById(vehicleSale.customer_id)
        vehicleSale.setCustomer(customer)

        history = self.getCustomerEmploymentHistory(customer.customer_id)
        vehicleSale.setCustomEmployment(history)

        print(vehicleSale)
        print("  ", customer)
        for item in history:
            print("    ", item)
        print("  ", vehicle)
        return vehicleSale

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

    def purchaseWarranty(self, warrantySale):

        customer = warrantySale.customer
        # we need to skip this insert if the customer exists
        query = """
        INSERT INTO `warranty_sale` (warranty_sale_id, vehicle_id, customer_id, co_signer_name, warranty_sale_date, total_cost,
                 monthly_cost, salesperson_id) VALUES ('{}', 
        '{}', '{}', '{}', '{}', '{}', '{}', '{}')
        """.format(
            warrantySale.warranty_sale_id, warrantySale.vehicle_id,
            warrantySale.customer_id, warrantySale.co_signer_name,
            warrantySale.warranty_sale_date, warrantySale.total_cost,
            warrantySale.monthly_cost, warrantySale.salesperson_id)

        cursor = self.query(query)
        warrantySaleId = cursor.lastrowid

        employmentIndex = 0
        for i in range(0, len(warrantySale.warranties)):
            warranty = warrantySale.warranties[i]
            employmentIndex += 1
            query = """INSERT INTO `warranty` (warranty_sale_id, warranty_start_date, warranty_length, warranty_cost, warranty_deductable) 
            VALUES ('{}', '{}', '{}', '{}', '{}')""".format(warrantySaleId,
                                                            warranty.warranty_start_date, warranty.warranty_length,
                                                            warranty.warranty_cost, warranty.warranty_deductable)
            cursor = self.query(query)
            warranty_id = cursor.lastrowid

            for j in range(0, len(warranty.warranty_item_list)):
                warranty_item_list = warranty.warranty_item_list[j]
                employmentIndex += 1
                query = """INSERT INTO `warranty_item_list` (warranty_sale_id, warranty_id, item_id) 
                VALUES ('{}', '{}', '{}')""".format(
                    warrantySaleId, warranty_id, warranty_item_list.item_id)
                cursor = self.query(query)
                warranty_item_list_id = cursor.lastrowid

        # commit these changes
        self.cnx.commit()
        return warrantySaleId

    def getWarrantyReport(self, warrantySaleId):
        warrantySale = self.getWarrantySaleById(warrantySaleId)

        vehicle = self.getVehicleById(warrantySale.vehicle_id)

        customer = self.getCustomerById(warrantySale.customer_id)

        salesPerson = self.getSalesPersonById(warrantySale.salesperson_id)
        warrantySale.setItems(vehicle, customer, salesPerson)

        print(warrantySale)
        print("  ", vehicle)
        print("  ", customer)
        print("  ", salesPerson)

        warranties = self.getWarrantyById(warrantySaleId)

        for warranty in warranties:
            print("    ", warranty)

            warrantyItems = self.getWarrantyItemList(warrantySaleId, warranty.warranty_id)

            for item in warrantyItems:
                print("      ", item)
                actualItems = self.searchWarrantyItems(item.item_id)
                warranty.addWarrantyItem(actualItems[0])

            warrantySale.addWarranty(warranty)
        return warrantySale

    def getWarrantySaleById(self, warrantySaleId):
        cursor = self.query("SELECT * FROM warranty_sale WHERE `warranty_sale_id` = {}".format(warrantySaleId))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        return WarrantySale.fromNamedTuple(result)

    def getWarrantyById(self, warrantySaleId):
        cursor = self.query("SELECT * FROM warranty WHERE `warranty_sale_id` = {}".format(warrantySaleId))
        result = []
        for warranty in cursor:
            result.append(Warranty.fromNamedTuple(warranty))
        self.closeCursor(cursor)
        return result

    def getWarrantyItemList(self, warrantySaleId, warranty_id):
        cursor = self.query("SELECT * FROM warranty_item_list WHERE `warranty_id` = {}".format(warranty_id))
        result = []
        for warranty in cursor:
            result.append(WarrantyItemListEntry.fromNamedTuple(warranty))
        self.closeCursor(cursor)
        return result

    def getPurchasesByCustomerId(self, customer_id):
        cursor = self.query("SELECT * FROM sale WHERE `customer_id` = {}".format(customer_id))
        result = []
        for warranty in cursor:
            result.append(VehicleSale.fromNamedTuple(warranty))
        self.closeCursor(cursor)
        return result

    def getPaymentInfoByCustomerId(self, customer_id):
        cursor = self.query("SELECT * FROM payment_history WHERE `customer_id` = {}".format(customer_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        try:
            return PaymentHistory.fromNamedTuple(result)
        except AttributeError:
            return None

    def getPaymentById(self, payment_id):
        cursor = self.query("SELECT * FROM payments WHERE `payment_id` = {}".format(payment_id))
        result = None
        if cursor.rowcount > 0:
            result = cursor.fetchone()
        self.closeCursor(cursor)
        try:
            return Payment.fromNamedTuple(result)
        except AttributeError:
            return None

    def getPayments(self, customer_id):
        cursor = self.query("SELECT * FROM payments WHERE `customer_id` = {}".format(customer_id))
        result = []
        for warranty in cursor:
            result.append(Payment.fromNamedTuple(warranty))
        self.closeCursor(cursor)
        return result

    def makePayment(self, payment):

        history = self.getPaymentInfoByCustomerId(payment.customer_id)

        query = "SELECT * from `payments` WHERE `customer_id` = {}".format(payment.customer_id)
        cursor = self.query(query)
        latePayments = 0
        daysLate = 0
        for p in cursor:
            if p.payment_paid_date > p.payment_date:
                latePayments += 1
                daysLate += (p.payment_paid_date - p.payment_date).days
        totalPayments = cursor.rowcount
        if latePayments != 0:
            averageDaysLate = daysLate // latePayments
        else:
            averageDaysLate = 0

        # we need to skip this insert if the customer exists
        query = """
        INSERT INTO `payments` (customer_id, vehicle_id, payment_date, payment_amount_due, payment_paid_date,
                 payment_amount, payment_bank_account) VALUES ('{}', 
        '{}', '{}', '{}', '{}', '{}', '{}')
        """.format(
            payment.customer_id, payment.vehicle_id,
            payment.payment_date,
            payment.payment_amount_due,
            payment.payment_paid_date,
            payment.payment_amount, payment.payment_bank_account)

        print(query)
        cursor = self.query(query)
        payment_id = cursor.lastrowid

        cursor = self.query("SELECT * FROM payment_history WHERE `customer_id` = {}".format(payment.customer_id))
        result = None
        if cursor.rowcount == 0:
            history = PaymentHistory(payment.customer_id, 0, 0)
            query = """INSERT into `payment_history` (`customer_id`, `number_late_payments`, `average_days_late`) 
            VALUES ('{}', {}, {})""".format(payment.customer_id, history.number_late_payments,
                                            history.average_days_late)
            self.query(query)

        # is this payment late?

        if payment.payment_date < payment.payment_paid_date:
            history.average_days_late = ((averageDaysLate * latePayments) + (
                    payment.payment_paid_date - payment.payment_date).days) / (latePayments + 1)
            history.number_late_payments = latePayments + 1

            query = """UPDATE `payment_history` SET `number_late_payments` = '{}', average_days_late = '{}' WHERE
                    `customer_id` = '{}'""".format(history.number_late_payments, history.average_days_late,
                                                   payment.customer_id)
            self.query(query)

        self.cnx.commit()

        return payment_id

    def getPaymentReport(self, payment_id):
        payment = self.getPaymentById(payment_id)
        print(payment)
        pass

    def getPaymentHistoryReport(self, customer_id):
        history = self.getPaymentInfoByCustomerId(customer_id)
        customer = self.getCustomerById(customer_id)
        print(history)
        payments = self.getPayments(customer_id)
        if history:
            history.setPayments(payments)
            history.setCustomer(customer)
        else:
            history = PaymentHistory(customer_id, 0, 0)
            history.setCustomer(customer)
        for payment in payments:
            print(payment)
        return history

    def getVehicleProblemById(self, problem_id, vehicle_id):
        query = "SELECT * from vehicle_problems WHERE problem_id = '{}' AND vehicle_id ='{}'".format(problem_id,
                                                                                                     vehicle_id)
        cursor = self.query(query)
        result = None
        if cursor.rowcount:
            result = VehicleProblem.fromNamedTuple(cursor.fetchone())
        cursor.close()
        return result

    def searchCustomersWithVehicles(self):
        query = "SELECT customer.* FROM sale INNER JOIN customer ON customer.customer_id=sale.customer_id"
        print(query)
        cursor = self.query(query)
        result = []
        for sale in cursor:
            result.append(Customer.fromNamedTuple(sale))
        self.closeCursor(cursor)
        return result

    def getVehicleByCustomerId(self, customer_id):
        query = """SELECT
        rmn_auto_sales.vehicle. * FROM
        rmn_auto_sales.sale
        INNER
        JOIN
        rmn_auto_sales.vehicle
        ON
        sale.vehicle_id = vehicle.vehicle_id
        WHERE
        sale.customer_id = {}""".format(customer_id)
        print(query)
        cursor = self.query(query)
        result = []
        for sale in cursor:
            result.append(Vehicle.fromNamedTuple(sale))
        self.closeCursor(cursor)
        return result

    def searchSellers(self):
        cursor = self.query("SELECT * FROM seller")
        results = []
        for seller in cursor:
            results.append(Seller.fromNamedTuple(seller))
        self.closeCursor(cursor)
        return results
