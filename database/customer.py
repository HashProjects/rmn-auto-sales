class Customer:
    @classmethod
    def fromNamedTuple(cls, customer):
        return cls(customer.customer_id, customer.customer_phone, customer.customer_last_name,
                   customer.customer_first_name, customer.customer_address, customer.customer_city,
                   customer.customer_state, customer.customer_zip, customer.customer_gender,
                   customer.customer_dob, customer.customer_taxpayer_id)

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
