import random


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

    def getText(self):
        return "{}, {}  \nPhone: {}\n" \
               "{}\n" \
               "{}, {} {}\n\n" \
               "Gender: {}, DOB: {}\n" \
               "SSN: {}\n".format(self.customer_last_name, self.customer_first_name, self.customer_phone,
                                  self.customer_address,
                                  self.customer_city, self.customer_state, self.customer_zip, self.customer_gender,
                                  self.customer_dob, self.customer_taxpayer_id)

    def getHtml(self):
        return """<b>LastName:</b> {}  <b>FirstName:</b>  {}  <b>Phone:</b> {}<br/>
        <b>Address</b>:<br/>
        {}<br/>
        {}, {} {}<br/>
        <b>Gender:</b>{}, <b>Date of Birth:</b>{}<br/>
        <b>SSN:</b> {}
        """.format(self.customer_last_name, self.customer_first_name, self.customer_phone, self.customer_address,
                   self.customer_city, self.customer_state, self.customer_zip, self.customer_gender,
                   self.customer_dob, self.customer_taxpayer_id)


def generateRandomCustomer():
    return Customer(0,
                    "{}-{}-{}".format(random.randint(100, 1000), random.randint(100, 1000),
                                      random.randint(1000, 10000)),
                    random.choice(["Smith", "Nyugen", "Biden", "Trump", "Harris", "Newsome", "Johnson"]),
                    random.choice(["Donald", "Joe", "Kamala", "Ted", "Loan", "Gavin", "Eric", "Mohit", "Sammy"]),
                    "{} {} {}".format(random.randint(1000, 100000), random.choice(
                        ["Mockingbird", "Wayne Street", "Kent", "Martin Luther King Jr"]),
                                      random.choice(["Lane", "Blvd", "Street", "Road"])),
                    random.choice(["Fountain Valley", "Fullerton", "Placentia", "Orange", "Garden Grove", "Anaheim",
                                   "Newport Beach", "Irvine"]),
                    random.choice(["Fountain Valley", "California", "Texas", "Florida", "Nevada"]),
                    random.randint(10000, 10000),
                    random.choice(["Male", "Female"]),
                    "{}-{}-{}".format(random.randint(1, 13), random.randint(1, 31), random.randint(1970, 2000)),
                    "{}-{}-{}".format(random.randint(100, 1000), random.randint(10, 100),
                                      random.randint(1000, 10000)))
