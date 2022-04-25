class PaymentHistory:
    @classmethod
    def fromNamedTuple(cls, payment_history):
        return cls(payment_history.customer_id, payment_history.number_late_payments, payment_history.average_days_late)

    def __init__(self, customer_id, number_late_payments, average_days_late):
        self.customer_id = customer_id
        self.number_late_payments = number_late_payments
        self.average_days_late = average_days_late
        self.customer = None
        self.payments = None

    def setCustomer(self, customer):
        self.customer = customer

    def setPayments(self, payments):
        self.payments = payments

    def __str__(self):
        return "PaymentHistory({}: late: {} average: {})".format(self.customer_id, self.number_late_payments,
                                                                 self.average_days_late)

    def getHtml(self):
        html = "<h1>Payment History</h1>"

        html += """
                <p><b>Customer:</b> {} {} <b>Gender:</b> {} <b>DOB:</b> {} <b>Tax Payer ID:</b> {}</p>
                <b>Late Payments:</b> {}<br/>
                <b>Average Days Late:</b> {}
                """.format(self.customer.customer_first_name, self.customer.customer_last_name,
                           self.customer.customer_gender,
                           self.customer.customer_dob, self.customer.customer_taxpayer_id,
                           self.number_late_payments, self.average_days_late)

        html += "<pre>"
        html += """{:14} {:12} {:10} {:10} {:5} {:12}\n""".format("Payment Date", "Amount Due", "Paid Date", "Amount",
                                                                  "Late", "Bank Account")
        for payment in self.payments:
            lateValue = ""
            if payment.isLate():
                lateValue = "Late"
            html += """{:14} ${:<11,} {:10} ${:<9,} {:5} {:12}\n""".format(payment.payment_date.strftime("%m/%d/%y"),
                                                                           payment.payment_amount_due,
                                                                           payment.payment_paid_date.strftime(
                                                                               "%m/%d/%y"),
                                                                           payment.payment_amount,
                                                                           lateValue,
                                                                           payment.payment_bank_account)

        html += "</pre>"
        return html
