class Warranty:
    @classmethod
    def fromNamedTuple(cls, warranty):
        return cls(warranty.warranty_sale_id, warranty.warranty_id, warranty.warranty_start_date, warranty.warranty_length,
                   warranty.warranty_cost, warranty.warranty_deductable)

    def __init__(self, warranty_sale_id,
                 warranty_id, warranty_start_date, warranty_length, warranty_cost, warranty_deductable):
        self.warranty_sale_id = warranty_sale_id
        self.warranty_id = warranty_id
        self.warranty_start_date = warranty_start_date
        self.warranty_length = warranty_length
        self.warranty_cost = warranty_cost
        self.warranty_deductable = warranty_deductable
        self.warranty_item_list = []

    def addWarrantyItem(self, item):
        self.warranty_item_list.append(item)

    def __str__(self):
        return "Warranty({})".format(self.warranty_start_date)

    def getHtml(self):
        html = """
        <b>Date:</b> {}<br/>
        <b>Length:</b> {}<br/>
        <b>Total Cost:</b> ${:.2f}<br/>
        <b>Deductible:</b> ${:.2f}
        <h3>Warranty Items Covered</h3>
        """.format(self.warranty_start_date.strftime("%m/%d/%y"), self.warranty_length,
                   float(self.warranty_cost), float(self.warranty_deductable))

        html += "<pre>{:<3} {}\n".format("#", "Description")
        for item in self.warranty_item_list:
            html += "{:<3} {}\n".format(item.item_id, item.item_description)
        html += "</pre>"
        return html
