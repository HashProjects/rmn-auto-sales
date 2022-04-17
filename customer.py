class Customer:
    @classmethod
    def fromNamedTuple(cls, namedTuple):
        return cls(namedTuple.customer_id, namedTuple.customer_phone, namedTuple.customer_last_name,
                   namedTuple.customer_first_name, namedTuple.customer_address, namedTuple.customer_city,
                   namedTuple.customer_state, namedTuple.customer_zip, namedTuple.customer_gender,
                   namedTuple.customer_dob, namedTuple.customer_taxpayer_id)

    def __init__(self,
                 customer_id, customer_phone, customer_last_name, customer_first_name, customer_address, customer_city,
                 customer_state, customer_zip, customer_gender, customer_dob, customer_taxpayer_id):
        self.customer_id = customer_id
        self.customer_phone = customer_phone
        self.customer_last_name = customer_last_name
        self.customer_first_name = customer_first_name
        self.customer_address = customer_address
        self.customer_city = customer_city
        self.customer_state = customer_state
        self.customer_zip = customer_zip
        self.customer_gender = customer_gender
        self.customer_dob = customer_dob
        self.customer_taxpayer_id = customer_taxpayer_id

    def __str__(self):
        return "Customer({} {}, dob={})".format(self.customer_first_name, self.customer_last_name, self.customer_dob)
