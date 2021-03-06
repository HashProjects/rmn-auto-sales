#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 02, 2022 11:32:14 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import AddCustomerPaymentForm_support

class AddCustomerPaymentForm:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("792x757+133+161")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Add Customer Payment Form")
        top.configure(highlightcolor="black")

        self.top = top
        self.paymentDueValue = tk.StringVar()
        self.amountDueValue = tk.StringVar()
        self.paidDateValue = tk.StringVar()
        self.amuntPaidValue = tk.StringVar()
        self.bankAccountValue = tk.StringVar()
        self.customerValue = tk.StringVar()

        self.SelectACustomer = tk.Label(self.top)
        self.SelectACustomer.place(relx=0.014, rely=0.018, height=28, width=426)
        self.SelectACustomer.configure(activebackground="#f9f9f9")
        self.SelectACustomer.configure(anchor='w')
        self.SelectACustomer.configure(compound='left')
        self.SelectACustomer.configure(text='''Select a customer to enter payments:''')

        self.Customer = tk.Label(self.top)
        self.Customer.place(relx=0.025, rely=0.066, height=29, width=105)
        self.Customer.configure(activebackground="#f9f9f9")
        self.Customer.configure(anchor='w')
        self.Customer.configure(compound='left')
        self.Customer.configure(text='''Customer''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.342, height=29, width=193)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label1.configure(text='''Payment History''')

        self.PaymentDate = tk.Label(self.top)
        self.PaymentDate.place(relx=0.013, rely=0.198, height=28, width=145)
        self.PaymentDate.configure(activebackground="#f9f9f9")
        self.PaymentDate.configure(anchor='w')
        self.PaymentDate.configure(compound='left')
        self.PaymentDate.configure(text='''Payment Date''')

        self.Due = tk.Label(self.top)
        self.Due.place(relx=0.227, rely=0.198, height=28, width=111)
        self.Due.configure(activebackground="#f9f9f9")
        self.Due.configure(anchor='w')
        self.Due.configure(compound='left')
        self.Due.configure(text='''Amount Due''')

        self.PaidDate = tk.Label(self.top)
        self.PaidDate.place(relx=0.366, rely=0.185, height=28, width=105)
        self.PaidDate.configure(activebackground="#f9f9f9")
        self.PaidDate.configure(anchor='w')
        self.PaidDate.configure(compound='left')
        self.PaidDate.configure(text='''Paid Date''')

        self.Amount = tk.Label(self.top)
        self.Amount.place(relx=0.543, rely=0.185, height=28, width=105)
        self.Amount.configure(activebackground="#f9f9f9")
        self.Amount.configure(anchor='w')
        self.Amount.configure(compound='left')
        self.Amount.configure(text='''Amount''')

        self.BankAmount = tk.Label(self.top)
        self.BankAmount.place(relx=0.682, rely=0.185, height=28, width=105)
        self.BankAmount.configure(activebackground="#f9f9f9")
        self.BankAmount.configure(anchor='w')
        self.BankAmount.configure(compound='left')
        self.BankAmount.configure(text='''Bank Account''')

        self.AddMore = tk.Button(self.top)
        self.AddMore.place(relx=0.859, rely=0.238, height=34, width=107)
        self.AddMore.configure(activebackground="#f9f9f9")
        self.AddMore.configure(command=AddCustomerPaymentForm_support.AddPayment)
        self.AddMore.configure(compound='left')
        self.AddMore.configure(pady="0")
        self.AddMore.configure(text='''Add''')

        self.PaymentDateEntry = tk.Entry(self.top)
        self.PaymentDateEntry.place(relx=0.013, rely=0.238, height=30
                , relwidth=0.169)
        self.PaymentDateEntry.configure(background="white")
        self.PaymentDateEntry.configure(font="TkFixedFont")
        self.PaymentDateEntry.configure(selectbackground="blue")
        self.PaymentDateEntry.configure(selectforeground="white")
        self.PaymentDateEntry.configure(textvariable=self.paymentDueValue)

        self.DueEntry = tk.Entry(self.top)
        self.DueEntry.place(relx=0.215, rely=0.238, height=30, relwidth=0.131)
        self.DueEntry.configure(background="white")
        self.DueEntry.configure(font="TkFixedFont")
        self.DueEntry.configure(selectbackground="blue")
        self.DueEntry.configure(selectforeground="white")
        self.DueEntry.configure(textvariable=self.amountDueValue)

        self.PaidDateEntry = tk.Entry(self.top)
        self.PaidDateEntry.place(relx=0.366, rely=0.238, height=30
                , relwidth=0.157)
        self.PaidDateEntry.configure(background="white")
        self.PaidDateEntry.configure(font="TkFixedFont")
        self.PaidDateEntry.configure(selectbackground="blue")
        self.PaidDateEntry.configure(selectforeground="white")
        self.PaidDateEntry.configure(textvariable=self.paidDateValue)

        self.AmountEntry = tk.Entry(self.top)
        self.AmountEntry.place(relx=0.543, rely=0.238, height=30, relwidth=0.119)

        self.AmountEntry.configure(background="white")
        self.AmountEntry.configure(font="TkFixedFont")
        self.AmountEntry.configure(selectbackground="blue")
        self.AmountEntry.configure(selectforeground="white")
        self.AmountEntry.configure(textvariable=self.amuntPaidValue)

        self.BankAmountEntry = tk.Entry(self.top)
        self.BankAmountEntry.place(relx=0.682, rely=0.238, height=30
                , relwidth=0.144)
        self.BankAmountEntry.configure(background="white")
        self.BankAmountEntry.configure(font="TkFixedFont")
        self.BankAmountEntry.configure(selectbackground="blue")
        self.BankAmountEntry.configure(selectforeground="white")
        self.BankAmountEntry.configure(textvariable=self.bankAccountValue)

        self.Custom1 = AddCustomerPaymentForm_support.Custom(self.top)
        self.Custom1.place(relx=0.014, rely=0.606, relheight=0.38
                , relwidth=0.972)

        self.CustomerComboBox = ttk.Combobox(self.top)
        self.CustomerComboBox.place(relx=0.182, rely=0.071, relheight=0.034
                , relwidth=0.36)
        self.CustomerComboBox.configure(textvariable=self.customerValue)
        self.CustomerComboBox.configure(takefocus="")

        self.Custom4 = AddCustomerPaymentForm_support.CustomHtmlLabel(self.top)
        self.Custom4.place(relx=0.014, rely=0.376, relheight=0.206
                , relwidth=0.973)

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.013, rely=0.145,  relwidth=0.972)

        self.TLabel4 = ttk.Label(self.top)
        self.TLabel4.place(relx=0.013, rely=0.159, height=19, width=180)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Add Customer Payment''')
        self.TLabel4.configure(compound='left')

def start_up():
    AddCustomerPaymentForm_support.main()

if __name__ == '__main__':
    AddCustomerPaymentForm_support.main()




