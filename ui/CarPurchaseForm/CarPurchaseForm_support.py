#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 23, 2022 03:37:45 PM PDT  platform: Windows NT
#    Apr 28, 2022 04:37:59 PM PDT  platform: Linux
#    Apr 28, 2022 04:47:32 PM PDT  platform: Linux
import datetime
import random
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import tksheet

import CarPurchaseForm
from database import vehicle, vehicleproblems, vehicleproblem
from database.database import Database
from database.purchase import Purchase
from database.vehicle import Vehicle
from database.vehiclepurchase import VehiclePurchase
from ui.generic_report import generic_report_support


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    # _w1 = CarPurchaseForm.ListPrice(_top1)
    _w1 = CarPurchaseForm.CarPurchaseForm(_top1)
    init(_top1, _w1)

    root.mainloop()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

    # w.lblCellValue.config(text='')
    gui.dateValue.set(datetime.date.today().strftime("%m/%d/%y"))

    # Call a separate function to initialise the sheet (data grid) widget.
    initialise_custom_widget()


def initialise_custom_widget():
    """
    The tksheet.Sheet class has a lot of properties and event handlers, this
    initialisation function only uses a small subset of them to make a data
    grid with fairly basic functionality and formatting. There is minimal (or
    no) documentation with tksheet, so to extend the functionality illustrated
    here, look at the test_tksheet.py on GitHub for other options.
    """

    # global _w1
    head = ['Year', 'Make', 'Model', 'VIN', 'Color', 'Style', 'Condition', 'List', 'Sale']
    # and apply them to the data grid.
    _w1.Custom2.headers(head, redraw=True)

    head2 = ['#', 'Problem', 'Estimated Cost']
    # and apply them to the data grid.
    _w1.Custom3.headers(head2, redraw=True)

    # Enable a subset of the built-in class event handlers. These don't need to
    # be defined here, they are included in the class.

    # This code has an error
    w.Custom2.enable_bindings(
        "single_select",
        # "drag_select",
        "column_select",
        "row_select",
        "column_width_resize",
        # "row_height_resize",
        "copy",
        "cut",
        # "paste",
        # "delete",
        # "undo",
        # "edit_cell"
    )

    # This code has an error
    w.Custom3.enable_bindings(
        "single_select",
        # "drag_select",
        "column_select",
        "row_select",
        "column_width_resize",
        # "row_height_resize",
        "copy",
        "cut",
        # "paste",
        # "delete",
        # "undo",
        "edit_cell"
    )

    # Additional event handlers that require a local definition.
    # w.Custom1.extra_bindings([('cell_select', cell_select)])


def AddVehicle(*args):
    print('CarPurchaseForm_support.AddVehicle')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()

    # get all data
    newVehicle = Vehicle(0,
                         vehicle_make=_w1.makeValue.get(),
                         vehicle_sold=False,
                         vehicle_repaired=False,
                         vehicle_color=_w1.colorValue.get(),
                         vehicle_year=_w1.yearValue.get(),
                         vehicle_model=_w1.modleValue.get(),
                         vehicle_vin=_w1.vinValue.get(),
                         vehicle_style=_w1.styleValue.get(),
                         vehicle_miles=_w1.milesValue.get(),
                         vehicle_condition=_w1.conditionValue.get(),
                         vehicle_interior_color=_w1.interiorValue.get(),
                         vehicle_list_price=_w1.listPriceValue.get(),
                         vehicle_sale_price=_w1.salePriceValue.get())

    newVehiclePurchase = VehiclePurchase(0, 0, _w1.bookValue.get(), _w1.pricePaidValue.get())
    newVehiclePurchase.setVehicle(newVehicle)
    newVehiclePurchase.setVehicleProblems(currentProblems)

    allVehiclePurchases.append(newVehiclePurchase)

    updateVehicleList(allVehiclePurchases)



def updateVehicleList(vehiclesPurchased):
    count = _w1.Custom2.get_total_rows()
    for i in range(count - 1, -1, -1):
        _w1.Custom2.delete_row(i)

    for vp in vehiclesPurchased:
        car = vp.vehicle
        print(car)

        _w1.Custom2.insert_row([car.vehicle_year, car.vehicle_make,
                                car.vehicle_model, car.vehicle_vin,
                                car.vehicle_color, car.vehicle_style, car.vehicle_condition,
                                car.vehicle_list_price, car.vehicle_sale_price
                                ],
                               redraw=True)
    _w1.Custom2.set_all_column_widths()


def Submit(*args):
    print('CarPurchaseForm_support.Submit')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()

    db = Database()
    seller = db.getSellerByTaxId('11-19139391')
    purchase = Purchase(0, datetime.datetime.strptime(_w1.dateValue.get(), "%m/%d/%y"), seller.seller_id, False)

    purchase_id = db.purchase(purchase, allVehiclePurchases)

    result = db.getPurchaseReport(purchase_id)

    generic_report_support.displayReport(result.getHtml(), "Car Purchase Report")


Custom = tksheet.Sheet

currentProblems = []
currentVehicle = None
allVehiclePurchases = []


def randomData(*args):
    print('CarPurchaseForm_support.randomData')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()

    newVehicle = vehicle.generateRandomVehicle()
    vehicleProblems = []
    for i in range(random.randint(1, 10)):
        newProblem = vehicleproblem.generateRandomProblem()
        newProblem.problem_id = i + 1
        shouldAdd = True
        for problem in vehicleProblems:
            if problem.problem_description == newProblem.problem_description:
                shouldAdd = False
        if shouldAdd:
            vehicleProblems.append(newProblem)

    displayVehicleProblems(vehicleProblems)
    displayVehicle(newVehicle)
    global currentProblems
    currentProblems = vehicleProblems
    global currentVehicle
    currentVehicle = newVehicle


def displayVehicleProblems(vehicleProblems):
    count = _w1.Custom3.get_total_rows()
    for i in range(count - 1, -1, -1):
        _w1.Custom3.delete_row(i)

    for problem in vehicleProblems:
        print(problem)
        _w1.Custom3.insert_row([problem.problem_id, problem.problem_description, problem.estimated_repair_cost],
                               redraw=True)
    _w1.Custom3.set_all_column_widths()


def displayVehicle(newVehicle):
    _w1.makeValue.set(newVehicle.vehicle_make)
    _w1.modleValue.set(newVehicle.vehicle_model)
    _w1.yearValue.set(newVehicle.vehicle_year)
    _w1.conditionValue.set(newVehicle.vehicle_condition)
    _w1.colorValue.set(newVehicle.vehicle_color)
    _w1.vinValue.set(newVehicle.vehicle_vin)
    _w1.milesValue.set(newVehicle.vehicle_miles)
    _w1.listPriceValue.set(newVehicle.vehicle_list_price)
    _w1.salePriceValue.set(newVehicle.vehicle_sale_price)
    _w1.styleValue.set(newVehicle.vehicle_style)
    _w1.interiorValue.set(newVehicle.vehicle_interior_color)
    _w1.bookValue.set(newVehicle.vehicle_sale_price)
    _w1.pricePaidValue.set(newVehicle.vehicle_sale_price)


if __name__ == '__main__':
    CarPurchaseForm.start_up()
