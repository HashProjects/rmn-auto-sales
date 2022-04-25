import datetime
import random
import sys
import os

from database import vehicleproblem, vehicle, customer, employment, sale

# sys.path.insert(1, os.path.abspath("../.."))
from database.payment import Payment

from database.purchase import Purchase
from database.database import Database
from database.sale import VehicleSale
from database.customer import Customer
from database.vehiclepurchase import VehiclePurchase
from database.seller import Seller

DB = Database()


#customer = random.choice(DB.searchCustomers())

#purchase = random.choice(DB.getPurchasesByCustomerId(customer.customer_id))

cursor = DB.query("SELECT * FROM sale")
result = []
for warranty in cursor:
    result.append(VehicleSale.fromNamedTuple(warranty))
DB.closeCursor(cursor)

sale = random.choice(result)
customer = DB.getCustomerById(sale.customer_id)


datePaid = datetime.date.today()
change = random.randint(-5, 6)
if datePaid.day + change < 0:
    change = 0
elif datePaid.day + change > 28:
    change = 0
datePaid = datePaid.replace(datePaid.year, datePaid.month, datePaid.day + change)
payment = Payment(customer.customer_id, 0, sale.vehicle_id, datetime.date.today(), 1000, datePaid, 1000, "389383-93939")

payment_id = DB.makePayment(payment)

DB.getPaymentReport(payment_id)

DB.getPaymentHistoryReport(customer.customer_id)

DB.close()
# except TypeError:
#    DB.close()
