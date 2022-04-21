

class WarrantyItem:
    @classmethod
    def fromNamedTuple(cls, warranty_item):
        return cls(warranty_item.item_id, warranty_item.item_description)

    def __init__(self,
                 item_id, item_description):
        self.item_id = item_id
        self.item_description = item_description

    def __str__(self):
        return "WarrantyItem({} {})".format(self.item_id, self.item_description)
