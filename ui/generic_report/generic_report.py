#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Apr 23, 2022 10:28:54 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from ui.generic_report import generic_report_support


class HtmlWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1236x806+840+280")
        top.minsize(1, 1)
        top.maxsize(7665, 2130)
        top.resizable(1,  1)
        top.title("HtmlWindow")

        self.top = top

        self.Custom1 = generic_report_support.Custom(self.top)
        self.Custom1.place(relx=0.008, rely=0.062, relheight=0.919
                , relwidth=0.984)

def start_up():
    generic_report_support.main()

if __name__ == '__main__':
    generic_report_support.main()




