class Payment:

    @classmethod
    def fromNamedTuple(cls, payment):
        return cls(payment.customer_id, payment.payment_id, payment.vehicle_id,
                   payment.payment_date,
                   payment.payment_amount_due,
                   payment.payment_paid_date,
                   payment.payment_amount, payment.payment_bank_account)

    def __init__(self, customer_id, payment_id, vehicle_id, payment_date, payment_amount_due, payment_paid_date,
                 payment_amount, payment_bank_account):
        self.customer_id = customer_id
        self.payment_id = payment_id
        self.vehicle_id = vehicle_id
        self.payment_date = payment_date
        self.payment_amount_due = payment_amount_due
        self.payment_paid_date = payment_paid_date
        self.payment_amount = payment_amount
        self.payment_bank_account = payment_bank_account

    def __str__(self):
        return "Payment(paid on {} {}, due on {} {}, late={})".format(self.payment_paid_date.strftime("%m/%d/%y"), self.payment_amount,
                                                self.payment_date.strftime("%m/%d/%y"), self.payment_amount_due,
                                                self.isLate())

    def isLate(self):
        return self.payment_date < self.payment_paid_date
