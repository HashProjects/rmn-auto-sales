class PaymentHistory:
    @classmethod
    def fromNamedTupe(cls, payment_history):
        return cls(payment_history.customer_id, payment_history.number_late_payments, payment_history.average_days_late)

    def __init__(self, customer_id, number_late_payments, average_days_late):
        self.customer_id = customer_id
        self.number_late_payments = number_late_payments
        self.average_days_late = average_days_late
        self.customer = None

    def setCustomer(self, customer):
        self.customer = customer

    def __str__(self):
        return "PaymentHistory({}: late: {} average: {})".format(self.customer_id, self.number_late_payments,
                                                                 self.average_days_late)
