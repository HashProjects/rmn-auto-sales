#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 29, 2022 09:17:03 PM PDT  platform: Windows NT
import datetime
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import tksheet

import WarrantySaleForm
from database.database import Database
from database.warranty import Warranty
from database.warrantyitem import WarrantyItem
from database.warrantysale import WarrantySale
from ui.generic_report import generic_report_support

warranties = []
salesPeople = []
customers = []
vehicles = []
currentSalesPerson = None
currentCustomer = None
currentVehicle = None
currentWarranty = Warranty(0, 0, "", "", "", "")
warrantyItemList = []
warrantyitemlist = {
    "Tire": 100,
    "Drivetrain": 100,
    "Windows": 100,
    "Battery": 100,
    "Paint": 1000,
    "Headlights": 100,
    "Entire Vehicle": 2000
}

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = WarrantySaleForm.WarrantySaleForm(_top1)
    init(_w1)
    root.mainloop()


def init(window):
    db = Database()
    global salesPeople
    salesPeople = db.searchSalesPeople()

    salesNames = []
    for name in salesPeople:
        salesNames.append(name.salesperson_name)

    global customers
    customers = db.searchCustomersWithVehicles()
    customerNames = []
    for customer in customers:
        customerNames.append(customer.customer_last_name + ", " + customer.customer_first_name)

    window.SalesPersonTCombobox["values"] = salesNames
    window.CustomerTCombobox["values"] = customerNames
    window.VehicleTCombobox["values"] = ["Select Customer"]

    global warrantyItemList
    warrantyItemList = db.searchWarrantyItems()

    itemNameList = []
    for key in warrantyitemlist.keys():
        itemNameList.append(key)

    window.Items1TCombobox["values"] = itemNameList

    window.SalesPersonTCombobox.bind('<<ComboboxSelected>>', selectSalesPerson)
    window.CustomerTCombobox.bind('<<ComboboxSelected>>', selectCustomer)
    window.VehicleTCombobox.bind('<<ComboboxSelected>>', selectVehicle)
    window.Items1TCombobox.bind('<<ComboboxSelected>>', selectItem)

    #default value
    window.startDateValue.set(datetime.date.today().strftime("%m/%d/%y"))
    window.lengthValue.set("2")
    window.costValue.set("1000")
    window.deductableValue.set("500")
    window.monthlyCostValue.set("0")
    window.totalCostValue.set("0")
    window.dateValue.set(datetime.date.today().strftime("%m/%d/%y"))
    initialise_custom_widget()

    db.close()
    updateView()

def updateView():
    if len(_w1.salesPersonValue.get()) and len(_w1.customerValue.get()) and len(_w1.vehicleValue.get()) and len(warranties):
        _w1.SubmitBottom["state"] = "active"
    else:
        _w1.SubmitBottom["state"] = "disabled"

    if len(_w1.itemValue.get()):
        _w1.AddItem["state"] = "active"
    else:
        _w1.AddItem["state"] = "disabled"

    end_index = _w1.AddItemScrolledlistbox.index("end")
    if end_index != 0:
        _w1.AddWarranty["state"] = "active"
    else:
        _w1.AddWarranty["state"] = "disabled"

    if len(_w1.customerValue.get()):
        _w1.VehicleTCombobox["state"] = "active"
    else:
        _w1.VehicleTCombobox["state"] = "disabled"

def initialise_custom_widget():
    """
    The tksheet.Sheet class has a lot of properties and event handlers, this
    initialisation function only uses a small subset of them to make a data
    grid with fairly basic functionality and formatting. There is minimal (or
    no) documentation with tksheet, so to extend the functionality illustrated
    here, look at the test_tksheet.py on GitHub for other options.
    """

    # global _w2
    head = ['Start Date', 'Length', 'Cost', 'Deductable', 'Items Covered']
    # and apply them to the data grid.
    _w1.AddWarrantyCustom.headers(head, redraw=True)


    # Enable a subset of the built-in class event handlers. These don't need to
    # be defined here, they are included in the class.

    # This code has an error
    _w1.AddWarrantyCustom.enable_bindings(
        "single_select",
        #"drag_select",
        "column_select",
        "row_select",
        "column_width_resize",
        "row_height_resize",
        "copy",
        "cut",
        #"paste",
        #"delete",
        #"undo",
        #"edit_cell"
        )

    # Additional event handlers that require a local definition.
    # w.Custom1.extra_bindings([('cell_select', cell_select)])

def selectItem(event):
    updateView()

def selectSalesPerson(event):
    print("selected")
    global currentSalesPerson
    currentSalesPerson = salesPeople[_w1.SalesPersonTCombobox.current()]
    _w1.Phone.delete("1.0", END)
    _w1.Phone.insert("1.0", currentSalesPerson.salesperson_phone)
    updateView()

def selectCustomer(event):
    print("selected")
    global currentCustomer
    currentCustomer = customers[_w1.CustomerTCombobox.current()]
    db = Database()
    global vehicles
    vehicles = db.getVehicleByCustomerId(currentCustomer.customer_id)

    cars = []
    for car in vehicles:
        cars.append(car.vehicle_year + " " + car.vehicle_make + " " + car.vehicle_model)
    _w1.VehicleTCombobox["values"] = cars
    db.close()
    updateView()

def selectVehicle(event):
    print("selected")
    global currentVehicle
    currentVehicle = vehicles[_w1.VehicleTCombobox.current()]

    _w1.VIN.delete("1.0", END)
    _w1.VIN.insert("1.0", currentVehicle.vehicle_vin)
    updateView()

def AddItem(*args):
    print('WarrantySaleForm_support.AddItem')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    #_w1.AddItemScrolledlistbox.insert(0, [_w1.Items1TCombobox.get()])
    #currentWarranty.addWarrantyItem(WarrantyItem(len(warranties)+1, _w1.Items1TCombobox.get()))

    selectedItem = warrantyItemList[_w1.Items1TCombobox.current()]
    _w1.AddItemScrolledlistbox.insert(0, [selectedItem.item_description])
    currentWarranty.addWarrantyItem(selectedItem)
    updateView()


def AddWarranty(*args):
    global currentWarranty
    print('WarrantySaleForm_support.AddWarranty')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    currentWarranty.warranty_deductable = _w1.deductableValue.get()
    currentWarranty.warranty_cost = _w1.costValue.get()
    currentWarranty.warranty_length = _w1.lengthValue.get()
    currentWarranty.warranty_start_date = datetime.datetime.strptime(_w1.startDateValue.get(), "%m/%d/%y")

    warranties.append(currentWarranty)
    # update the grid

    #delete existing data
    count = _w1.AddWarrantyCustom.get_total_rows()
    for i in range(count-1, -1, -1):
        _w1.AddWarrantyCustom.delete_row(i)

    for problem in warranties:
        print(problem)

        itemsCovered = ""

        for item in problem.warranty_item_list:
            itemsCovered += item.item_description + ", "

        _w1.AddWarrantyCustom.insert_row([problem.warranty_start_date,
                                          problem.warranty_length,
                                          problem.warranty_cost,
                                          problem.warranty_deductable,
                                          itemsCovered],
                               redraw=True)

    _w1.AddWarrantyCustom.set_all_column_widths()

    # clear out current warranty
    currentWarranty = Warranty(0, 0, datetime.date.today(), 2, 1000, 500)
    _w1.AddItemScrolledlistbox.delete(0, END)


    totalCost = 0
    averageLength = 0
    for warranty in warranties:
        totalCost += int(warranty.warranty_cost)
        averageLength += int(warranty.warranty_length)

    averageLength = averageLength / len(warranties)
    _w1.totalCostValue.set(totalCost)
    _w1.monthlyCostValue.set(totalCost / averageLength / 12)
    updateView()


def Submit(*args):
    print('WarrantySaleForm_support.Submit')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()




def SubmitBottom(*args):
    print('WarrantySaleForm_support.SubmitBottom')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()

    warrantySale = WarrantySale(0, currentVehicle.vehicle_id, currentCustomer.customer_id, "None",
                                datetime.datetime.strptime(_w1.dateValue.get(), "%m/%d/%y"),
                                _w1.totalCostValue.get(),
                                _w1.monthlyCostValue.get(),
                                currentSalesPerson.salesperson_id)
    warrantySale.setItems(currentVehicle, currentCustomer, currentSalesPerson)
    for warranty in warranties:
        warrantySale.addWarranty(warranty)

    db = Database()

    warranty_sale_id = db.purchaseWarranty(warrantySale)

    warrantySale = db.getWarrantyReport(warranty_sale_id)

    generic_report_support.displayReport(warrantySale.getHtml(), "Warranty Sale")

    db.close()


Custom = tksheet.Sheet  # To be updated by user with name of custom widget.

if __name__ == '__main__':
    WarrantySaleForm.start_up()
