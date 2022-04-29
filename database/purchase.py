class Purchase:
    @classmethod
    def fromNamedTuple(cls, purchase):
        return cls(purchase.purchase_id, purchase.purchase_date, purchase.seller_id, purchase.auction)

    def __init__(self,
                 purchase_id, purchase_date, seller_id, auction):
        self.purchase_id = purchase_id
        self.purchase_date = purchase_date
        self.seller_id = seller_id
        self.auction = auction
        self.vehiclesPurchases = None
        self.seller = None


    def __str__(self):
        return "Purchase({}, auction={})".format(self.purchase_date, self.auction)

    def setVehiclesPurchases(self, vehiclesPurchases):
        self.vehiclesPurchases = vehiclesPurchases

    def setSeller(self, seller):
        self.seller = seller

    def getHtml(self):
        html = """
        <h1>Vehicle Purchase Report</h1>
        <h2>Seller Information</h2>
        {}
        <h2>Vehicle Information</h2>
        """.format(self.seller.getHtml())

        index = 1
        for vp in self.vehiclesPurchases:
            car = vp.vehicle
            html += "<h3>Vehicle {} - {} {} {}</h3>".format(index, car.vehicle_year, car.vehicle_make, car.vehicle_model)
            html += car.getHtml()

            html += "<h4>Problems</h4>"
            html += "<pre>{:<3} {:30} {}\n".format("#", "Description", "Est. Cost")
            for problem in vp.vehicle_problems:
                html += "{:<3} {:30} ${:.2f}\n".format(problem.problem_id, problem.problem_description, problem.estimated_repair_cost)
            html += "</pre>"
            index += 1

        return html
