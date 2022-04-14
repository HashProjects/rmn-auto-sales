#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 13, 2022 12:49:44 PM PDT  platform: Linux
#    Apr 14, 2022 09:14:02 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import tksheet

import rmn_auto_sales

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

Custom = tksheet.Sheet  # To be updated by user with name of custom widget.

def button_vehicle_search(*args):
    print('rmn_auto_sales_support.button_vehicle_search')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    global _top2, _w2
    _top2 = tk.Toplevel(root)
    _w2 = rmn_auto_sales.vehicle_search(_top2)

if __name__ == '__main__':
    rmn_auto_sales.start_up()




