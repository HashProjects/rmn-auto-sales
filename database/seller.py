class Seller:
    @classmethod
    def fromNamedTuple(cls, seller):
        return cls(seller.seller_id, seller.seller_name, seller.seller_address, seller.seller_city, seller.seller_state
                   , seller.seller_zip, seller.seller_phone, seller.seller_tax_id)

    def __init__(self, seller_id, seller_name, seller_address, seller_city, seller_state, seller_zip, seller_phone
                 , seller_tax_id):
        self.seller_id = seller_id
        self.seller_name = seller_name
        self.seller_address = seller_address
        self.seller_city = seller_city
        self.seller_state = seller_state
        self.seller_zip = seller_zip
        self.seller_phone = seller_phone
        self.seller_tax_id = seller_tax_id

    def __str__(self):
        return "Seller({}, {})".format(self.seller_name, self.seller_tax_id)

    def getHtml(self):
        return """<b>Name:</b> {}</b>
          <b>Phone:</b> {}<br/>
          <b>Address:</b><br/>
          {}<br/>
          {}, {} {}<br/>
          <b>TaxID:</b> {}
          """.format(self.seller_name, self.seller_phone, self.seller_address,
                     self.seller_city, self.seller_state, self.seller_zip, self.seller_tax_id)
