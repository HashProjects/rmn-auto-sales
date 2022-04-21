class Warranty:
    @classmethod
    def fromNamedTuple(cls, warranty):
        return cls(warranty.warranty_id, warranty.warranty_start_date, warranty.warranty_length,
                   warranty.warranty_cost, warranty.warranty_deductable)

    def __init__(self,
                 warranty_id, warranty_start_date, warranty_length, warranty_cost, warranty_deductable):
        self.warranty_id = warranty_id
        self.warranty_start_date = warranty_start_date
        self.warranty_length = warranty_length
        self.warranty_cost = warranty_cost
        self.warranty_deductable = warranty_deductable

    def __str__(self):
        return "Warranty({})".format(self.warranty_start_date)
