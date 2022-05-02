#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 02, 2022 06:44:17 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from ui.CustomerADDorSelectForm import CustomerADDorSelectForm_support


class SelectCustomerForm:
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

        top.geometry("600x450+935+563")
        top.minsize(120, 1)
        top.maxsize(1796, 1101)
        top.resizable(0,  0)
        top.title("Select or Add Customer")
        top.configure(highlightcolor="black")

        self.top = top

        self.FirstName = tk.Label(self.top)
        self.FirstName.place(x=0, y=60, height=21, width=84)
        self.FirstName.configure(activebackground="#f9f9f9")
        self.FirstName.configure(anchor='w')
        self.FirstName.configure(compound='left')
        self.FirstName.configure(text='''First Name:''')

        self.Address = tk.Label(self.top)
        self.Address.place(x=0, y=120, height=21, width=84)
        self.Address.configure(activebackground="#f9f9f9")
        self.Address.configure(anchor='w')
        self.Address.configure(compound='left')
        self.Address.configure(text='''Address:''')

        self.State = tk.Label(self.top)
        self.State.place(x=0, y=180, height=21, width=84)
        self.State.configure(activebackground="#f9f9f9")
        self.State.configure(anchor='w')
        self.State.configure(compound='left')
        self.State.configure(text='''State:''')

        self.DOB = tk.Label(self.top)
        self.DOB.place(x=0, y=250, height=21, width=84)
        self.DOB.configure(activebackground="#f9f9f9")
        self.DOB.configure(anchor='w')
        self.DOB.configure(compound='left')
        self.DOB.configure(text='''DOB:''')

        self.Gender = tk.Label(self.top)
        self.Gender.place(x=0, y=300, height=41, width=84)
        self.Gender.configure(activebackground="#f9f9f9")
        self.Gender.configure(anchor='w')
        self.Gender.configure(compound='left')
        self.Gender.configure(text='''Gender:''')

        self.FirstNameText = tk.Text(self.top)
        self.FirstNameText.place(x=90, y=60, height=24, width=164)
        self.FirstNameText.configure(background="white")
        self.FirstNameText.configure(font="TkTextFont")
        self.FirstNameText.configure(selectbackground="blue")
        self.FirstNameText.configure(selectforeground="white")
        self.FirstNameText.configure(wrap="none")

        self.AddressText = tk.Text(self.top)
        self.AddressText.place(x=90, y=120, height=24, width=164)
        self.AddressText.configure(background="white")
        self.AddressText.configure(font="TkTextFont")
        self.AddressText.configure(selectbackground="blue")
        self.AddressText.configure(selectforeground="white")
        self.AddressText.configure(wrap="none")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.StateText = tk.Text(self.top)
        self.StateText.place(x=90, y=180, height=24, width=164)
        self.StateText.configure(background="white")
        self.StateText.configure(font="TkTextFont")
        self.StateText.configure(selectbackground="blue")
        self.StateText.configure(selectforeground="white")
        self.StateText.configure(wrap="none")

        self.DOBText = tk.Text(self.top)
        self.DOBText.place(x=90, y=240, height=24, width=164)
        self.DOBText.configure(background="white")
        self.DOBText.configure(font="TkTextFont")
        self.DOBText.configure(selectbackground="blue")
        self.DOBText.configure(selectforeground="white")
        self.DOBText.configure(wrap="none")

        self.GenderText = tk.Text(self.top)
        self.GenderText.place(x=90, y=310, height=24, width=164)
        self.GenderText.configure(background="white")
        self.GenderText.configure(font="TkTextFont")
        self.GenderText.configure(selectbackground="blue")
        self.GenderText.configure(selectforeground="white")
        self.GenderText.configure(wrap="none")

        self.LastName = tk.Label(self.top)
        self.LastName.place(x=300, y=60, height=21, width=84)
        self.LastName.configure(activebackground="#f9f9f9")
        self.LastName.configure(anchor='w')
        self.LastName.configure(compound='left')
        self.LastName.configure(text='''Last Name:''')

        self.City = tk.Label(self.top)
        self.City.place(x=300, y=120, height=21, width=84)
        self.City.configure(activebackground="#f9f9f9")
        self.City.configure(anchor='w')
        self.City.configure(compound='left')
        self.City.configure(text='''City:''')

        self.Zip = tk.Label(self.top)
        self.Zip.place(x=300, y=180, height=21, width=84)
        self.Zip.configure(activebackground="#f9f9f9")
        self.Zip.configure(anchor='w')
        self.Zip.configure(compound='left')
        self.Zip.configure(text='''Zip:''')

        self.TaxID = tk.Label(self.top)
        self.TaxID.place(x=300, y=240, height=21, width=84)
        self.TaxID.configure(activebackground="#f9f9f9")
        self.TaxID.configure(anchor='w')
        self.TaxID.configure(compound='left')
        self.TaxID.configure(text='''Tax ID:''')

        self.Phone = tk.Label(self.top)
        self.Phone.place(x=300, y=310, height=21, width=84)
        self.Phone.configure(activebackground="#f9f9f9")
        self.Phone.configure(anchor='w')
        self.Phone.configure(compound='left')
        self.Phone.configure(text='''Phone:''')

        self.LastNameText = tk.Text(self.top)
        self.LastNameText.place(x=390, y=60, height=24, width=164)
        self.LastNameText.configure(background="white")
        self.LastNameText.configure(font="TkTextFont")
        self.LastNameText.configure(selectbackground="blue")
        self.LastNameText.configure(selectforeground="white")
        self.LastNameText.configure(wrap="none")

        self.CityText = tk.Text(self.top)
        self.CityText.place(x=390, y=120, height=24, width=164)
        self.CityText.configure(background="white")
        self.CityText.configure(font="TkTextFont")
        self.CityText.configure(selectbackground="blue")
        self.CityText.configure(selectforeground="white")
        self.CityText.configure(wrap="none")

        self.ZipText = tk.Text(self.top)
        self.ZipText.place(x=390, y=180, height=24, width=164)
        self.ZipText.configure(background="white")
        self.ZipText.configure(font="TkTextFont")
        self.ZipText.configure(selectbackground="blue")
        self.ZipText.configure(selectforeground="white")
        self.ZipText.configure(wrap="none")

        self.TaxIDText = tk.Text(self.top)
        self.TaxIDText.place(x=390, y=240, height=24, width=164)
        self.TaxIDText.configure(background="white")
        self.TaxIDText.configure(font="TkTextFont")
        self.TaxIDText.configure(selectbackground="blue")
        self.TaxIDText.configure(selectforeground="white")
        self.TaxIDText.configure(wrap="none")

        self.PhoneText = tk.Text(self.top)
        self.PhoneText.place(x=390, y=310, height=24, width=164)
        self.PhoneText.configure(background="white")
        self.PhoneText.configure(font="TkTextFont")
        self.PhoneText.configure(selectbackground="blue")
        self.PhoneText.configure(selectforeground="white")
        self.PhoneText.configure(wrap="none")

        self.SelectCustomer = tk.Label(self.top)
        self.SelectCustomer.place(x=10, y=10, height=21, width=194)
        self.SelectCustomer.configure(activebackground="#f9f9f9")
        self.SelectCustomer.configure(anchor='w')
        self.SelectCustomer.configure(compound='left')
        self.SelectCustomer.configure(text='''Select Customer:''')

        self.Search = tk.Button(self.top)
        self.Search.place(x=150, y=400, height=24, width=117)
        self.Search.configure(activebackground="#f9f9f9")
        self.Search.configure(command=CustomerADDorSelectForm_support.Search)
        self.Search.configure(compound='left')
        self.Search.configure(pady="0")
        self.Search.configure(text='''Search''')

        self.AddNewCustomer = tk.Button(self.top)
        self.AddNewCustomer.place(x=380, y=400, height=24, width=187)
        self.AddNewCustomer.configure(activebackground="#f9f9f9")
        self.AddNewCustomer.configure(command=CustomerADDorSelectForm_support.AddNewCustomer)
        self.AddNewCustomer.configure(compound='left')
        self.AddNewCustomer.configure(pady="0")
        self.AddNewCustomer.configure(text='''Select''')

        self.Demo = ttk.Button(self.top)
        self.Demo.place(x=10, y=400, height=34, width=119)
        self.Demo.configure(command=CustomerADDorSelectForm_support.randomButton)
        self.Demo.configure(takefocus="")
        self.Demo.configure(text='''Demo''')
        self.Demo.configure(compound='left')

def start_up():
    CustomerADDorSelectForm_support.main()

if __name__ == '__main__':
    CustomerADDorSelectForm_support.main()




