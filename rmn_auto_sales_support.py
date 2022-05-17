#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 13, 2022 12:49:44 PM PDT  platform: Linux
#    Apr 14, 2022 09:14:02 AM PDT  platform: Linux
#    Apr 29, 2022 03:14:55 PM PDT  platform: Linux
#    Apr 29, 2022 03:22:55 PM PDT  platform: Linux
#    May 17, 2022 09:36:36 AM PDT  platform: Linux
import subprocess
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import tksheet

import rmn_auto_sales
from database.database import Database
from ui import generic_report
from ui.generic_report import generic_report_support


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = rmn_auto_sales.HomePage(_top1)
    root.mainloop()

def button_click_purchase_car(*args):
    print('rmn_auto_sales_support.button_click_purchase_car')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    print("do something cool here")
    subprocess.call(["python3", "./ui/CarPurchaseForm/CarPurchaseForm.py"])

Custom = tksheet.Sheet  # To be updated by user with name of custom widget.

def button_vehicle_search(*args):
    print('rmn_auto_sales_support.button_vehicle_search')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    subprocess.call(["python3", "./ui/VehicleSearch/vehicle_search.py"])

def make_payment(*args):
    print('rmn_auto_sales_support.make_payment')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    subprocess.call(["python3", "./ui/AddCustomerPaymentForm/AddCustomerPaymentForm.py"])

def repair_vehicle(*args):
    print('rmn_auto_sales_support.repair_vehicle')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    subprocess.call(["python3", "./ui/VehicleRepair/vehicle_repair.py"])

def sell_vehicle(*args):
    print('rmn_auto_sales_support.sell_vehicle')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    subprocess.call(["python3", "./ui/CarSaleForm/CarSaleForm.py"])

def sell_warranty(*args):
    print('rmn_auto_sales_support.sell_warranty')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    subprocess.call(["python3", "./ui/WarrantySaleForm/WarrantySaleForm.py"])

def annual_report(*args):
    print('rmn_auto_sales_support.annual_report')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    db = Database()
    html = db.getAnnualReport()

    generic_report_support.displayReport(html, "Annual Report")
    db.close()

if __name__ == '__main__':
    rmn_auto_sales.start_up()





