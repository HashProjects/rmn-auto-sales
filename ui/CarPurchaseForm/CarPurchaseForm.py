#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 03, 2022 02:12:42 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import CarPurchaseForm_support

class CarPurchaseForm:
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

        top.geometry("937x714+731+120")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Car Purchase Form")
        top.configure(highlightcolor="black")

        self.top = top
        self.vehicleTitleValue = tk.StringVar()
        self.dateValue = tk.StringVar()
        self.locationValue = tk.StringVar()
        self.makeValue = tk.StringVar()
        self.modleValue = tk.StringVar()
        self.yearValue = tk.StringVar()
        self.milesValue = tk.StringVar()
        self.conditionValue = tk.StringVar()
        self.listPriceValue = tk.StringVar()
        self.salePriceValue = tk.StringVar()
        self.styleValue = tk.StringVar()
        self.interiorValue = tk.StringVar()
        self.taxIDValue = tk.StringVar()
        self.vinValue = tk.StringVar()
        self.colorValue = tk.StringVar()
        self.bookValue = tk.StringVar()
        self.sellerValue = tk.StringVar()

        self.Purchase = tk.Label(self.top)
        self.Purchase.place(relx=0.013, rely=0.018, height=27, width=130)
        self.Purchase.configure(activebackground="#f9f9f9")
        self.Purchase.configure(anchor='w')
        self.Purchase.configure(compound='left')
        self.Purchase.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Purchase.configure(text='''Purchase''')

        self.Date = tk.Label(self.top)
        self.Date.place(relx=0.013, rely=0.06, height=27, width=109)
        self.Date.configure(activebackground="#f9f9f9")
        self.Date.configure(anchor='w')
        self.Date.configure(compound='left')
        self.Date.configure(text='''Date''')

        self.Location = tk.Label(self.top)
        self.Location.place(relx=0.375, rely=0.122, height=27, width=89)
        self.Location.configure(activebackground="#f9f9f9")
        self.Location.configure(anchor='w')
        self.Location.configure(compound='left')
        self.Location.configure(text='''Location''')

        self.Make = tk.Label(self.top)
        self.Make.place(relx=0.011, rely=0.224, height=27, width=109)
        self.Make.configure(activebackground="#f9f9f9")
        self.Make.configure(anchor='w')
        self.Make.configure(compound='left')
        self.Make.configure(text='''Make''')

        self.Model = tk.Label(self.top)
        self.Model.place(relx=0.299, rely=0.221, height=27, width=109)
        self.Model.configure(activebackground="#f9f9f9")
        self.Model.configure(anchor='w')
        self.Model.configure(compound='left')
        self.Model.configure(text='''Model''')

        self.Year = tk.Label(self.top)
        self.Year.place(relx=0.62, rely=0.218, height=27, width=109)
        self.Year.configure(activebackground="#f9f9f9")
        self.Year.configure(anchor='w')
        self.Year.configure(compound='left')
        self.Year.configure(text='''Year''')

        self.Miles = tk.Label(self.top)
        self.Miles.place(relx=0.299, rely=0.266, height=27, width=109)
        self.Miles.configure(activebackground="#f9f9f9")
        self.Miles.configure(anchor='w')
        self.Miles.configure(compound='left')
        self.Miles.configure(text='''Miles''')

        self.Condition = tk.Label(self.top)
        self.Condition.place(relx=0.619, rely=0.266, height=27, width=109)
        self.Condition.configure(activebackground="#f9f9f9")
        self.Condition.configure(anchor='w')
        self.Condition.configure(compound='left')
        self.Condition.configure(text='''Condition''')

        self.Model_1_1_1_1 = tk.Label(self.top)
        self.Model_1_1_1_1.place(relx=0.011, rely=0.504, height=27, width=109)
        self.Model_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Model_1_1_1_1.configure(anchor='w')
        self.Model_1_1_1_1.configure(compound='left')
        self.Model_1_1_1_1.configure(text='''List Price''')

        self.SalesPrice = tk.Label(self.top)
        self.SalesPrice.place(relx=0.011, rely=0.56, height=27, width=109)
        self.SalesPrice.configure(activebackground="#f9f9f9")
        self.SalesPrice.configure(anchor='w')
        self.SalesPrice.configure(compound='left')
        self.SalesPrice.configure(text='''Sales Price''')

        self.Style = tk.Label(self.top)
        self.Style.place(relx=0.011, rely=0.331, height=27, width=109)
        self.Style.configure(activebackground="#f9f9f9")
        self.Style.configure(anchor='w')
        self.Style.configure(compound='left')
        self.Style.configure(text='''Style''')

        self.InteriorColor = tk.Label(self.top)
        self.InteriorColor.place(relx=0.011, rely=0.448, height=27, width=109)
        self.InteriorColor.configure(activebackground="#f9f9f9")
        self.InteriorColor.configure(anchor='w')
        self.InteriorColor.configure(compound='left')
        self.InteriorColor.configure(text='''Interior Color''')

        self.Vehicle1 = tk.Label(self.top)
        self.Vehicle1.place(relx=0.011, rely=0.168, height=27, width=130)
        self.Vehicle1.configure(activebackground="#f9f9f9")
        self.Vehicle1.configure(anchor='w')
        self.Vehicle1.configure(compound='left')
        self.Vehicle1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Vehicle1.configure(highlightcolor="#ffffff")
        self.Vehicle1.configure(text='''Vehicle 1''')
        self.Vehicle1.configure(textvariable=self.vehicleTitleValue)
        self.vehicleTitleValue.set('''Vehicle 1''')

        self.SellerDealer = tk.Label(self.top)
        self.SellerDealer.place(relx=0.374, rely=0.07, height=27, width=109)
        self.SellerDealer.configure(activebackground="#f9f9f9")
        self.SellerDealer.configure(anchor='w')
        self.SellerDealer.configure(compound='left')
        self.SellerDealer.configure(text='''Seller/Dealer''')

        self.TaxId = tk.Label(self.top)
        self.TaxId.place(relx=0.672, rely=0.126, height=27, width=79)
        self.TaxId.configure(activebackground="#f9f9f9")
        self.TaxId.configure(anchor='w')
        self.TaxId.configure(compound='left')
        self.TaxId.configure(text='''Tax ID''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.768, rely=0.672, height=34, width=197)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=CarPurchaseForm_support.AddVehicle)
        self.Button1.configure(compound='left')
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Vehicle''')

        self.Submit = tk.Button(self.top)
        self.Submit.place(relx=0.8, rely=0.952, height=24, width=177)
        self.Submit.configure(activebackground="#f9f9f9")
        self.Submit.configure(command=CarPurchaseForm_support.Submit)
        self.Submit.configure(compound='left')
        self.Submit.configure(pady="0")
        self.Submit.configure(text='''Submit''')

        self.DateEntry = tk.Entry(self.top)
        self.DateEntry.place(relx=0.117, rely=0.069, height=20, relwidth=0.143)
        self.DateEntry.configure(background="white")
        self.DateEntry.configure(font="TkFixedFont")
        self.DateEntry.configure(selectbackground="blue")
        self.DateEntry.configure(selectforeground="white")
        self.DateEntry.configure(textvariable=self.dateValue)

        self.LocationEntry = tk.Entry(self.top)
        self.LocationEntry.place(relx=0.48, rely=0.126, height=20
                , relwidth=0.143)
        self.LocationEntry.configure(background="white")
        self.LocationEntry.configure(font="TkFixedFont")
        self.LocationEntry.configure(selectbackground="blue")
        self.LocationEntry.configure(selectforeground="white")
        self.LocationEntry.configure(textvariable=self.locationValue)

        self.MakeEntry = tk.Entry(self.top)
        self.MakeEntry.place(relx=0.128, rely=0.224, height=20, relwidth=0.143)
        self.MakeEntry.configure(background="white")
        self.MakeEntry.configure(font="TkFixedFont")
        self.MakeEntry.configure(selectbackground="blue")
        self.MakeEntry.configure(selectforeground="white")
        self.MakeEntry.configure(textvariable=self.makeValue)

        self.ModelEntry = tk.Entry(self.top)
        self.ModelEntry.place(relx=0.438, rely=0.224, height=20, relwidth=0.143)
        self.ModelEntry.configure(background="white")
        self.ModelEntry.configure(font="TkFixedFont")
        self.ModelEntry.configure(selectbackground="blue")
        self.ModelEntry.configure(selectforeground="white")
        self.ModelEntry.configure(textvariable=self.modleValue)

        self.YearEntry = tk.Entry(self.top)
        self.YearEntry.place(relx=0.747, rely=0.224, height=20, relwidth=0.143)
        self.YearEntry.configure(background="white")
        self.YearEntry.configure(font="TkFixedFont")
        self.YearEntry.configure(selectbackground="blue")
        self.YearEntry.configure(selectforeground="white")
        self.YearEntry.configure(textvariable=self.yearValue)

        self.MilesEntry = tk.Entry(self.top)
        self.MilesEntry.place(relx=0.438, rely=0.266, height=20, relwidth=0.143)
        self.MilesEntry.configure(background="white")
        self.MilesEntry.configure(font="TkFixedFont")
        self.MilesEntry.configure(selectbackground="blue")
        self.MilesEntry.configure(selectforeground="white")
        self.MilesEntry.configure(textvariable=self.milesValue)

        self.ConditionEntry = tk.Entry(self.top)
        self.ConditionEntry.place(relx=0.747, rely=0.266, height=20
                , relwidth=0.143)
        self.ConditionEntry.configure(background="white")
        self.ConditionEntry.configure(font="TkFixedFont")
        self.ConditionEntry.configure(selectbackground="blue")
        self.ConditionEntry.configure(selectforeground="white")
        self.ConditionEntry.configure(textvariable=self.conditionValue)

        self.ListEntry = tk.Entry(self.top)
        self.ListEntry.place(relx=0.128, rely=0.504, height=20, relwidth=0.143)
        self.ListEntry.configure(background="white")
        self.ListEntry.configure(font="TkFixedFont")
        self.ListEntry.configure(selectbackground="blue")
        self.ListEntry.configure(selectforeground="white")
        self.ListEntry.configure(textvariable=self.listPriceValue)

        self.SalesPriceEntry = tk.Entry(self.top)
        self.SalesPriceEntry.place(relx=0.128, rely=0.56, height=20
                , relwidth=0.143)
        self.SalesPriceEntry.configure(background="white")
        self.SalesPriceEntry.configure(font="TkFixedFont")
        self.SalesPriceEntry.configure(selectbackground="blue")
        self.SalesPriceEntry.configure(selectforeground="white")
        self.SalesPriceEntry.configure(textvariable=self.salePriceValue)

        self.StyleEntry = tk.Entry(self.top)
        self.StyleEntry.place(relx=0.128, rely=0.336, height=20, relwidth=0.143)
        self.StyleEntry.configure(background="white")
        self.StyleEntry.configure(font="TkFixedFont")
        self.StyleEntry.configure(selectbackground="blue")
        self.StyleEntry.configure(selectforeground="white")
        self.StyleEntry.configure(textvariable=self.styleValue)

        self.InteriorColorEntry = tk.Entry(self.top)
        self.InteriorColorEntry.place(relx=0.128, rely=0.448, height=20
                , relwidth=0.143)
        self.InteriorColorEntry.configure(background="white")
        self.InteriorColorEntry.configure(font="TkFixedFont")
        self.InteriorColorEntry.configure(selectbackground="blue")
        self.InteriorColorEntry.configure(selectforeground="white")
        self.InteriorColorEntry.configure(textvariable=self.interiorValue)

        self.TaxIDEntry = tk.Entry(self.top)
        self.TaxIDEntry.place(relx=0.758, rely=0.126, height=20, relwidth=0.143)
        self.TaxIDEntry.configure(background="white")
        self.TaxIDEntry.configure(font="TkFixedFont")
        self.TaxIDEntry.configure(selectbackground="blue")
        self.TaxIDEntry.configure(selectforeground="white")
        self.TaxIDEntry.configure(textvariable=self.taxIDValue)

        self.Custom2 = CarPurchaseForm_support.Custom(self.top)
        self.Custom2.place(relx=0.021, rely=0.784, relheight=0.161
                , relwidth=0.967)

        self.Custom3 = CarPurchaseForm_support.Custom(self.top)
        self.Custom3.place(relx=0.288, rely=0.364, relheight=0.217
                , relwidth=0.689)

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.288, rely=0.322, height=25, width=177)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Vehicle Problems''')
        self.TLabel1.configure(compound='left')

        self.TButton1 = ttk.Button(self.top)
        self.TButton1.place(relx=0.299, rely=0.672, height=28, width=83)
        self.TButton1.configure(command=CarPurchaseForm_support.randomData)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Demo''')
        self.TButton1.configure(compound='left')

        self.VIN = tk.Label(self.top)
        self.VIN.place(relx=0.011, rely=0.28, height=27, width=109)
        self.VIN.configure(activebackground="#f9f9f9")
        self.VIN.configure(anchor='w')
        self.VIN.configure(compound='left')
        self.VIN.configure(text='''VIN''')

        self.VINEntry = tk.Entry(self.top)
        self.VINEntry.place(relx=0.128, rely=0.28, height=20, relwidth=0.143)
        self.VINEntry.configure(background="white")
        self.VINEntry.configure(font="TkFixedFont")
        self.VINEntry.configure(selectbackground="blue")
        self.VINEntry.configure(selectforeground="white")
        self.VINEntry.configure(textvariable=self.vinValue)

        self.InteriorColor = tk.Label(self.top)
        self.InteriorColor.place(relx=0.011, rely=0.392, height=27, width=109)
        self.InteriorColor.configure(activebackground="#f9f9f9")
        self.InteriorColor.configure(anchor='w')
        self.InteriorColor.configure(compound='left')
        self.InteriorColor.configure(text='''Color''')

        self.ColorEntry = tk.Entry(self.top)
        self.ColorEntry.place(relx=0.129, rely=0.396, height=20, relwidth=0.143)
        self.ColorEntry.configure(background="white")
        self.ColorEntry.configure(font="TkFixedFont")
        self.ColorEntry.configure(selectbackground="blue")
        self.ColorEntry.configure(selectforeground="white")
        self.ColorEntry.configure(textvariable=self.colorValue)

        self.SalesPrice = tk.Label(self.top)
        self.SalesPrice.place(relx=0.011, rely=0.616, height=27, width=109)
        self.SalesPrice.configure(activebackground="#f9f9f9")
        self.SalesPrice.configure(anchor='w')
        self.SalesPrice.configure(compound='left')
        self.SalesPrice.configure(text='''Book Value''')

        self.BookEntry = tk.Entry(self.top)
        self.BookEntry.place(relx=0.128, rely=0.616, height=20, relwidth=0.143)
        self.BookEntry.configure(background="white")
        self.BookEntry.configure(font="TkFixedFont")
        self.BookEntry.configure(selectbackground="blue")
        self.BookEntry.configure(selectforeground="white")
        self.BookEntry.configure(textvariable=self.bookValue)

        self.PricePaid = tk.Label(self.top)
        self.PricePaid.place(relx=0.011, rely=0.681, height=27, width=109)
        self.PricePaid.configure(activebackground="#f9f9f9")
        self.PricePaid.configure(anchor='w')
        self.PricePaid.configure(compound='left')
        self.PricePaid.configure(text='''Price Paid''')

        self.BookEntry_1 = tk.Entry(self.top)
        self.BookEntry_1.place(relx=0.128, rely=0.686, height=20, relwidth=0.143)

        self.BookEntry_1.configure(background="white")
        self.BookEntry_1.configure(font="TkFixedFont")
        self.BookEntry_1.configure(selectbackground="blue")
        self.BookEntry_1.configure(selectforeground="white")
        self.BookEntry_1.configure(textvariable=self.bookValue)

        self.SellerComboBox = ttk.Combobox(self.top)
        self.SellerComboBox.place(relx=0.48, rely=0.07, relheight=0.029
                , relwidth=0.189)
        self.SellerComboBox.configure(textvariable=self.sellerValue)
        self.SellerComboBox.configure(takefocus="")

        self.TButton2 = ttk.Button(self.top)
        self.TButton2.place(relx=0.875, rely=0.588, height=28, width=94)
        self.TButton2.configure(command=CarPurchaseForm_support.addProblem)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Add Problem''')
        self.TButton2.configure(compound='left')

        self.TLabel1_1 = ttk.Label(self.top)
        self.TLabel1_1.place(relx=0.011, rely=0.742, height=25, width=177)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Vehicle Purchase List''')
        self.TLabel1_1.configure(compound='left')

def start_up():
    CarPurchaseForm_support.main()

if __name__ == '__main__':
    CarPurchaseForm_support.main()




