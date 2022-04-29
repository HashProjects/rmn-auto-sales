class VehiclePurchase:
    @classmethod
    def fromNamedTuple(cls, vehicle_purchase):
        return cls(vehicle_purchase.purchase_id, vehicle_purchase.vehicle_id, vehicle_purchase.book_price, vehicle_purchase.price_paid)

    def __init__(self,
                 purchase_id, vehicle_id, book_price, price_paid):
        self.purchase_id = purchase_id
        self.vehicle_id = vehicle_id
        self.book_price = book_price
        self.price_paid = price_paid

        self.vehicle_problems = []
        self.vehicle = None

    def addProblem(self, problem):
        self.vehicle_problems.append(problem)

    def setVehicleProblems(self, problems):
        self.vehicle_problems = problems

    def __str__(self):
        return "VehiclePurchase({}, {}, {})".format(self.vehicle_id, self.book_price, self.price_paid)

    def setVehicle(self, newVehicle):
        self.vehicle = newVehicle

