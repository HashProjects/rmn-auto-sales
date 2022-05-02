#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 02, 2022 11:17:04 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import CarSaleForm_support

class VehicleSaleForm:
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

        top.geometry("917x641+424+138")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Vehicle Sale")
        top.configure(highlightcolor="black")

        self.top = top
        self.dateValue = tk.StringVar()
        self.totalDueValue = tk.StringVar()
        self.downPaymentValue = tk.StringVar()
        self.financedAmount = tk.StringVar()
        self.commissionValue = tk.StringVar()
        self.salesPersonValue = tk.StringVar()

        self.Sale = tk.Label(self.top)
        self.Sale.place(relx=0.022, rely=0.017, height=24, width=889)
        self.Sale.configure(activebackground="#f9f9f9")
        self.Sale.configure(anchor='w')
        self.Sale.configure(compound='left')
        self.Sale.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Sale.configure(text='''Vehicle Sale Information''')

        self.Date = tk.Label(self.top)
        self.Date.place(relx=0.022, rely=0.078, height=25, width=160)
        self.Date.configure(activebackground="#f9f9f9")
        self.Date.configure(anchor='w')
        self.Date.configure(compound='left')
        self.Date.configure(text='''Date''')

        self.TotalDue = tk.Label(self.top)
        self.TotalDue.place(relx=0.022, rely=0.14, height=25, width=160)
        self.TotalDue.configure(activebackground="#f9f9f9")
        self.TotalDue.configure(anchor='w')
        self.TotalDue.configure(compound='left')
        self.TotalDue.configure(text='''Total Due''')

        self.DownPayment = tk.Label(self.top)
        self.DownPayment.place(relx=0.022, rely=0.218, height=25, width=145)
        self.DownPayment.configure(activebackground="#f9f9f9")
        self.DownPayment.configure(anchor='w')
        self.DownPayment.configure(compound='left')
        self.DownPayment.configure(text='''Down Payment''')

        self.FinancedAmount = tk.Label(self.top)
        self.FinancedAmount.place(relx=0.022, rely=0.296, height=25, width=160)
        self.FinancedAmount.configure(activebackground="#f9f9f9")
        self.FinancedAmount.configure(anchor='w')
        self.FinancedAmount.configure(compound='left')
        self.FinancedAmount.configure(text='''Financed Amount''')

        self.DateEntry = tk.Entry(self.top)
        self.DateEntry.place(relx=0.218, rely=0.078, height=20, relwidth=0.168)
        self.DateEntry.configure(background="white")
        self.DateEntry.configure(font="TkFixedFont")
        self.DateEntry.configure(selectbackground="blue")
        self.DateEntry.configure(selectforeground="white")
        self.DateEntry.configure(textvariable=self.dateValue)

        self.TotalDueEntry = tk.Entry(self.top)
        self.TotalDueEntry.place(relx=0.218, rely=0.14, height=20
                , relwidth=0.168)
        self.TotalDueEntry.configure(background="white")
        self.TotalDueEntry.configure(font="TkFixedFont")
        self.TotalDueEntry.configure(selectbackground="blue")
        self.TotalDueEntry.configure(selectforeground="white")
        self.TotalDueEntry.configure(textvariable=self.totalDueValue)

        self.DownPaymentEntry = tk.Entry(self.top)
        self.DownPaymentEntry.place(relx=0.218, rely=0.218, height=20
                , relwidth=0.168)
        self.DownPaymentEntry.configure(background="white")
        self.DownPaymentEntry.configure(font="TkFixedFont")
        self.DownPaymentEntry.configure(selectbackground="blue")
        self.DownPaymentEntry.configure(selectforeground="white")
        self.DownPaymentEntry.configure(textvariable=self.downPaymentValue)

        self.FinancedAmountEntry = tk.Entry(self.top)
        self.FinancedAmountEntry.place(relx=0.218, rely=0.296, height=20
                , relwidth=0.168)
        self.FinancedAmountEntry.configure(background="white")
        self.FinancedAmountEntry.configure(font="TkFixedFont")
        self.FinancedAmountEntry.configure(selectbackground="blue")
        self.FinancedAmountEntry.configure(selectforeground="white")
        self.FinancedAmountEntry.configure(textvariable=self.financedAmount)

        self.Salesperson = tk.Label(self.top)
        self.Salesperson.place(relx=0.458, rely=0.078, height=25, width=145)
        self.Salesperson.configure(activebackground="#f9f9f9")
        self.Salesperson.configure(anchor='w')
        self.Salesperson.configure(compound='left')
        self.Salesperson.configure(text='''Salesperson''')

        self.CommissionEntry = tk.Entry(self.top)
        self.CommissionEntry.place(relx=0.622, rely=0.14, height=20
                , relwidth=0.168)
        self.CommissionEntry.configure(background="white")
        self.CommissionEntry.configure(font="TkFixedFont")
        self.CommissionEntry.configure(selectbackground="blue")
        self.CommissionEntry.configure(selectforeground="white")
        self.CommissionEntry.configure(textvariable=self.commissionValue)

        self.Commission = tk.Label(self.top)
        self.Commission.place(relx=0.458, rely=0.14, height=25, width=145)
        self.Commission.configure(activebackground="#f9f9f9")
        self.Commission.configure(anchor='w')
        self.Commission.configure(compound='left')
        self.Commission.configure(text='''Commission''')

        self.Customer = tk.Label(self.top)
        self.Customer.place(relx=0.011, rely=0.343, height=25, width=145)
        self.Customer.configure(activebackground="#f9f9f9")
        self.Customer.configure(anchor='w')
        self.Customer.configure(compound='left')
        self.Customer.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Customer.configure(text='''Customer''')

        self.CustomerDetailsText = tk.Text(self.top)
        self.CustomerDetailsText.place(relx=0.011, rely=0.39, relheight=0.231
                , relwidth=0.348)
        self.CustomerDetailsText.configure(background="white")
        self.CustomerDetailsText.configure(font="TkTextFont")
        self.CustomerDetailsText.configure(selectbackground="blue")
        self.CustomerDetailsText.configure(selectforeground="white")
        self.CustomerDetailsText.configure(wrap="word")

        self.SelectCustomer = tk.Button(self.top)
        self.SelectCustomer.place(relx=0.011, rely=0.624, height=24, width=147)
        self.SelectCustomer.configure(activebackground="#f9f9f9")
        self.SelectCustomer.configure(command=CarSaleForm_support.SelectCustomer)
        self.SelectCustomer.configure(compound='left')
        self.SelectCustomer.configure(pady="0")
        self.SelectCustomer.configure(text='''Select Customer''')

        self.CarDetailsText = tk.Text(self.top)
        self.CarDetailsText.place(relx=0.011, rely=0.718, relheight=0.22
                , relwidth=0.348)
        self.CarDetailsText.configure(background="white")
        self.CarDetailsText.configure(font="TkTextFont")
        self.CarDetailsText.configure(selectbackground="blue")
        self.CarDetailsText.configure(selectforeground="white")
        self.CarDetailsText.configure(wrap="word")

        self.SelectVehicle = tk.Button(self.top)
        self.SelectVehicle.place(relx=0.011, rely=0.952, height=24, width=147)
        self.SelectVehicle.configure(activebackground="#f9f9f9")
        self.SelectVehicle.configure(command=CarSaleForm_support.SelectVehicle)
        self.SelectVehicle.configure(compound='left')
        self.SelectVehicle.configure(pady="0")
        self.SelectVehicle.configure(text='''Select Vehicle''')

        self.Submit = tk.Button(self.top)
        self.Submit.place(relx=0.829, rely=0.952, height=24, width=147)
        self.Submit.configure(activebackground="#f9f9f9")
        self.Submit.configure(command=CarSaleForm_support.Submit)
        self.Submit.configure(compound='left')
        self.Submit.configure(pady="0")
        self.Submit.configure(text='''Submit''')

        self.AddWorkHistory = tk.Button(self.top)
        self.AddWorkHistory.place(relx=0.393, rely=0.849, height=24, width=147)
        self.AddWorkHistory.configure(activebackground="#f9f9f9")
        self.AddWorkHistory.configure(command=CarSaleForm_support.AddWorkHistory)
        self.AddWorkHistory.configure(compound='left')
        self.AddWorkHistory.configure(pady="0")
        self.AddWorkHistory.configure(text='''Add Work History''')

        self.Customer_1 = tk.Label(self.top)
        self.Customer_1.place(relx=0.382, rely=0.39, height=24, width=245)
        self.Customer_1.configure(activebackground="#f9f9f9")
        self.Customer_1.configure(anchor='w')
        self.Customer_1.configure(compound='left')
        self.Customer_1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Customer_1.configure(text='''Employment History''')

        self.Custom1 = CarSaleForm_support.Custom(self.top)
        self.Custom1.place(relx=0.382, rely=0.423, relheight=0.402
                , relwidth=0.606)

        self.Customer_2 = tk.Label(self.top)
        self.Customer_2.place(relx=0.011, rely=0.671, height=25, width=145)
        self.Customer_2.configure(activebackground="#f9f9f9")
        self.Customer_2.configure(anchor='w')
        self.Customer_2.configure(compound='left')
        self.Customer_2.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Customer_2.configure(text='''Vehicle''')

        self.SalesPersonComboBox = ttk.Combobox(self.top)
        self.SalesPersonComboBox.place(relx=0.622, rely=0.078, relheight=0.033
                , relwidth=0.249)
        self.SalesPersonComboBox.configure(textvariable=self.salesPersonValue)
        self.SalesPersonComboBox.configure(takefocus="")

def start_up():
    CarSaleForm_support.main()

if __name__ == '__main__':
    CarSaleForm_support.main()




