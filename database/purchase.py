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

    def __str__(self):
        return "Purchase({}, auction={})".format(self.purchase_date, self.auction)
