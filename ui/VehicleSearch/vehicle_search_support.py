#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 18, 2022 12:43:43 PM PDT  platform: Linux
#    Apr 18, 2022 12:47:19 PM PDT  platform: Linux
#    Apr 18, 2022 12:52:15 PM PDT  platform: Linux

import sys
import tkinter as tk

import tksheet

import ui
from database import database
from database.database import Database
from ui import VehicleSearch
from ui.VehicleSearch import vehicle_search
from ui.VehicleSearch.vehicle_search import VehicleSearchForm

DB = database.Database()
vehicle_sold = False
vehicle_repaired = True


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top2, _w2
    _top2 = root
    _w2 = VehicleSearchForm(_top2)
    init(_top2, _w2)
    root.mainloop()

topLevel = None
def start(*args):
    '''Main entry point for the application.'''
    global topLevel
    topLevel = tk.Toplevel()
    topLevel.protocol('WM_DELETE_WINDOW', topLevel.destroy)
    # Creates a toplevel widget.
    global _top2, _w2
    _top2 = topLevel
    _w2 = VehicleSearchForm(_top2)
    init(_top2, _w2)
    root.mainloop()

Custom = tksheet.Sheet  # To be updated by user with name of custom widget.


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

    # w.lblCellValue.config(text='')

    # Call a separate function to initialise the sheet (data grid) widget.
    initialise_custom_widget()
    do_vehicle_search()


def do_vehicle_search(*args):
    print('vehicle_search_support.do_vehicle_search')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()
    db = Database()
    results = db.searchVehicles(vehicle_year=_w2.yearValue.get(),
                                vehicle_make=_w2.makeValue.get(),
                                vehicle_color=_w2.colorValue.get(),
                                vehicle_sold=False,
                                vehicle_repaired=True)

    count = _w2.Custom1.get_total_rows()
    for i in range(count-1, -1, -1):
        _w2.Custom1.delete_row(i)

    for car in results:
        print(car)
        _w2.Custom1.insert_row([car.vehicle_id, car.vehicle_year, car.vehicle_make,
                                car.vehicle_model, car.vehicle_color, car.vehicle_condition],
                               redraw=True)
    _w2.Custom1.set_all_column_widths()

    _w2.Custom1.bind("<Double-Button-1>", doubleClick)
    db.close()

def doubleClick(event):
    print("double click:", event)
    row = _w2.Custom1.identify_row(event)
    print (row)
    rowData = _w2.Custom1.get_cell_data(row, 0)
    print(rowData)
    db = Database()
    vehicle = db.getVehicleById(rowData)
    if callback is not None:
        callback(vehicle)
    db.close()


def formatSheet(rows):
    """ Set up various formatting options for the data grid.  """

    # Change column width
    w.Custom1.column_width(1, 100)

    # Change column alignment
    w.Custom1.align_columns(2, 'center')
    w.Custom1.align_columns(3, 'center')
    w.Custom1.align_columns(4, 'center')
    w.Custom1.align_columns(5, 'e')

    # Highlight any cells that meet a condition - a Balance that is negative.
    for row in range(0, rows):
        value = w.Custom1.get_cell_data(row, 5)
        if value != ' ' and value != '':
            if float(value) < 0:
                w.Custom1.highlight_cells(row=row, column=5, fg='white', bg='red')


def initialise_custom_widget():
    """
    The tksheet.Sheet class has a lot of properties and event handlers, this
    initialisation function only uses a small subset of them to make a data
    grid with fairly basic functionality and formatting. There is minimal (or
    no) documentation with tksheet, so to extend the functionality illustrated
    here, look at the test_tksheet.py on GitHub for other options.
    """

    # global _w2
    head = ['id', 'Year', 'Make', 'Model', 'Color', 'Condition']
    # and apply them to the data grid.
    _w2.Custom1.headers(head, redraw=True)

    # Enable a subset of the built-in class event handlers. These don't need to
    # be defined here, they are included in the class.



    # This code has an error
    w.Custom1.enable_bindings(
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


callback = None

def selectVehicle(vehicleCallback, vehicleSold=False, vehicleRepaired=True):
    global callback
    global vehicle_repaired
    global vehicle_sold
    callback = vehicleCallback
    vehicle_repaired = vehicleRepaired
    vehicle_sold = vehicleSold
    start()


if __name__ == '__main__':
    vehicle_search.start_up()
