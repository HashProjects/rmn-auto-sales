class VehicleSale:

    @classmethod
    def fromNamedTuple(cls, sale):
        return cls(sale.sale_id, sale.sale_date, sale.total_due, sale.down_payment, sale.financed_amount,
                   sale.employee_id,
                   sale.employee_commission, sale.vehicle_id, sale.customer_id)

    def __init__(self,
                 sale_id, sale_date, total_due, down_payment, financed_amount, employee_id,
                 employee_commission, vehicle_id, customer_id):
        self.sale_id = sale_id
        self.sale_date = sale_date
        self.total_due = total_due
        self.down_payment = down_payment
        self.financed_amount = financed_amount
        self.employee_id = employee_id
        self.employee_commission = employee_commission
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.vehicle = None
        self.customer = None
        self.customer_employment = None

    def setVehicle(self, vehicle):
        self.vehicle = vehicle
        self.vehicle_id = vehicle.vehicle_id

    def setCustomer(self, customer):
        self.customer = customer
        self.customer_id = customer.customer_id

    def setCustomEmployment(self, customer_employment):
        self.customer_employment = customer_employment

    def __str__(self):
        return "Sale({}: {})".format(self.sale_date, self.total_due)

    def getHtml(self):
        return """<h1>Vehicle Sale Report</h1>
        <b>Date</b>: {}<br/>
        <b>Total Due:</b> {}<br/>
        <b>Down Payment:</b> {}<br/>
        <h2>Customer Information</h2>
        {}
        <h2>Vehicle Sold</h2>
        {} 
        """.format(self.sale_date.strftime("%m/%d/%y"), self.total_due, self.down_payment, self.customer.getHtml(),
                   self.vehicle.getHtml())
