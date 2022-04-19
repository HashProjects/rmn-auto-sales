class SalesPerson:
    @classmethod
    def fromNamedTuple(cls, salesperson):
        return cls(salesperson.salesperson_id, salesperson.salesperson_name, salesperson.salesperson_phone)

    def __init__(self,
                 salesperson_id, salesperson_name, salesperson_phone):
        self.salesperson_id = salesperson_id
        self.salesperson_name = salesperson_name
        self.salesperson_phone = salesperson_phone

    def __str__(self):
        return "SalesPerson({}; {})".format(self.salesperson_name, self.salesperson_phone)
