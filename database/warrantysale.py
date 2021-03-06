class WarrantySale:

    @classmethod
    def fromNamedTuple(cls, warranty_sale):
        return cls(warranty_sale.warranty_sale_id, warranty_sale.vehicle_id,
                   warranty_sale.customer_id, warranty_sale.co_signer_name,
                   warranty_sale.warranty_sale_date, warranty_sale.total_cost,
                   warranty_sale.monthly_cost, warranty_sale.salesperson_id)

    def __init__(self,
                 warranty_sale_id, vehicle_id, customer_id, co_signer_name, warranty_sale_date, total_cost,
                 monthly_cost, salesperson_id):
        self.warranty_sale_id = warranty_sale_id
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.co_signer_name = co_signer_name
        self.warranty_sale_date = warranty_sale_date
        self.total_cost = total_cost
        self.monthly_cost = monthly_cost
        self.salesperson_id = salesperson_id
        self.salesperson = None
        self.vehicle = None
        self.customer = None
        self.warranties = []

    def setItems(self, vehicle, customer, salesperson):
        self.vehicle = vehicle
        self.vehicle_id = vehicle.vehicle_id
        self.customer = customer
        self.customer_id = customer.customer_id
        self.salesperson = salesperson
        self.salesperson_id = salesperson.salesperson_id

    def addWarranty(self, warranty):
        self.warranties.append(warranty)

    def __str__(self):
        return "WarrantySale({}, {})".format(self.total_cost, self.monthly_cost)

    def getHtml(self):
        html = """
        <h1>Warranty Sale: {}</h1>
        <b>Date:</b> {}<br/>
        <b>Total Cost:</b> ${:.2f}<br/>
        <b>Monthly Cost:</b> ${:.2f}
        <p>Sales Person:</b> {}<br/>
        <h2>Customer Information</h2>
        {}
        <h2>Vehicle Information</h2>
        {}
        """.format(self.warranty_sale_id,
                   self.warranty_sale_date.strftime("%m/%d/%y"),
                   self.total_cost,
                   self.monthly_cost,
                   self.salesperson.salesperson_name,
                   self.customer.getHtml(),
                   self.vehicle.getHtml())
        index = 1
        for warranty in self.warranties:
            html += "<h2>Warranty {}</h2>".format(index)
            index += 1
            html += warranty.getHtml()

        return html
