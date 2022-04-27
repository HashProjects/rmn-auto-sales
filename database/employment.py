import random


class CustomerEmployment:
    @classmethod
    def fromNamedTuple(cls, customer_employment):
        return cls(customer_employment.customer_id,
                   customer_employment.employment_id,
                   customer_employment.employer,
                   customer_employment.title,
                   customer_employment.supervisor,
                   customer_employment.supervisor_phone,
                   customer_employment.employer_address,
                   customer_employment.start_date,
                   customer_employment.end_date)

    def __init__(self,
                 customer_id, employment_id, employer, title, supervisor, supervisor_phone, employer_address,
                 start_date, end_date):
        self.customer_id = customer_id
        self.employment_id = employment_id
        self.employer = employer
        self.title = title
        self.supervisor = supervisor
        self.supervisor_phone = supervisor_phone
        self.employer_address = employer_address
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return "CustomerEmployment({}: {}, {})".format(self.employer, self.supervisor, self.supervisor_phone)

    def getText(self):
        return "{} {}: {}, {}".format(self.title, self.employer, self.supervisor, self.supervisor_phone)


def generateRandomEmployment(customer):
    return CustomerEmployment(0,
                              customer.customer_id,
                              random.choice(["3M", "Avery Denison", "Josephine Crab Shack", "Home Depot", "Lowes"]),
                              random.choice(["Janitor", "Teacher", "Engineer", "Professor"]),
                              random.choice(
                                  ["Smith", "Nyugen", "Biden", "Trump", "Harris", "Newsome", "Johnson"]) + ", " +
                              random.choice(
                                  ["Donald", "Joe", "Kamala", "Ted", "Loan", "Gavin", "Eric", "Mohit", "Sammy"]),
                              "{}-{}-{}".format(random.randint(100, 1000), random.randint(10, 100),
                                                random.randint(1000, 10000)),
                              "{} {} {}".format(random.randint(1000, 100000), random.choice(
                                  ["Mockingbird", "Wayne Street", "Kent", "Martin Luther King Jr"]),
                                                random.choice(["Lane", "Blvd", "Street", "Road"])) + " " +
                              random.choice(
                                  ["Fountain Valley", "Fullerton", "Placentia", "Orange", "Garden Grove", "Anaheim",
                                   "Newport Beach", "Irvine"]) + ", " +
                              random.choice(["Fountain Valley", "California", "Texas", "Florida", "Nevada"]) + " " +
                              str(random.randint(10000, 10000)),
                              random.choice(["2021-4-15", "2020-4-20", "2018-9-15"]),
                              random.choice(["2029-4-15", "2015-4-20", "2015-9-15"])
                              )
