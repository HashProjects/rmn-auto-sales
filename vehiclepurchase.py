class VehiclePurchase:
    @classmethod
    def fromNamedTuple(cls, vehicle_purchase):
        return cls(vehicle_purchase.purchase_id, vehicle_purchase.vehicle_id, vehicle_purchase.book_price)

    def __init__(self,
                 purchase_id, vehicle_id, book_price, price_paid):
        self.purchase_id = purchase_id
        self.vehicle_id = vehicle_id
        self.book_price = book_price
        self.price_paid = price_paid