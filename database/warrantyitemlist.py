class WarrantyItemListEntry:

    @classmethod
    def fromNamedTuple(cls, warranty_item_list):
        return cls(warranty_item_list.warranty_sale_id, warranty_item_list.warranty_id, warranty_item_list.item_id)

    def __init__(self,
                 warranty_sale_id, warranty_id, item_id):
        self.warranty_sale_id = warranty_sale_id
        self.warranty_id = warranty_id
        self.item_id = item_id

    def __str__(self):
        return "WarrantyItemListEntry({}, {}, {})".format(self.warranty_sale_id, self.warranty_id, self.item_id)