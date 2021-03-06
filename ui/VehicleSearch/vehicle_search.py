#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    May 02, 2022 10:51:06 AM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from ui.VehicleSearch import vehicle_search_support

class VehicleSearchForm:
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

        top.geometry("943x450+424+329")
        top.minsize(1, 1)
        top.maxsize(3825, 2130)
        top.resizable(1,  1)
        top.title("Vehicle Search")
        top.configure(highlightcolor="black")

        self.top = top
        self.yearValue = tk.StringVar()
        self.makeValue = tk.StringVar()
        self.colorValue = tk.StringVar()
        self.modelValue = tk.StringVar()
        self.milesValue = tk.StringVar()

        self.Custom1 = vehicle_search_support.Custom(self.top)
        self.Custom1.place(relx=0.011, rely=0.4, relheight=0.573, relwidth=0.971)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TLabelframe1 = ttk.Labelframe(self.top)
        self.TLabelframe1.place(relx=0.011, rely=0.022, relheight=0.367
                , relwidth=0.976)
        self.TLabelframe1.configure(relief='solid')
        self.TLabelframe1.configure(text='''Enter Vehicle Search Criteria''')
        self.TLabelframe1.configure(relief="solid")

        self.TButton1 = ttk.Button(self.TLabelframe1)
        self.TButton1.place(relx=0.902, rely=0.788, height=28, width=83
                , bordermode='ignore')
        self.TButton1.configure(command=vehicle_search_support.do_vehicle_search)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Search''')
        self.TButton1.configure(compound='left')

        self.Year = ttk.Entry(self.TLabelframe1)
        self.Year.place(relx=0.163, rely=0.182, relheight=0.127, relwidth=0.178
                , bordermode='ignore')
        self.Year.configure(textvariable=self.yearValue)
        self.Year.configure(takefocus="")
        self.Year.configure(cursor="xterm")

        self.Make = ttk.Entry(self.TLabelframe1)
        self.Make.place(relx=0.163, rely=0.364, relheight=0.127, relwidth=0.178
                , bordermode='ignore')
        self.Make.configure(textvariable=self.makeValue)
        self.Make.configure(takefocus="")
        self.Make.configure(cursor="xterm")

        self.Color = ttk.Entry(self.TLabelframe1)
        self.Color.place(relx=0.457, rely=0.182, relheight=0.127, relwidth=0.178
                , bordermode='ignore')
        self.Color.configure(textvariable=self.colorValue)
        self.Color.configure(takefocus="")
        self.Color.configure(cursor="xterm")

        self.TLabel1 = ttk.Label(self.TLabelframe1)
        self.TLabel1.place(relx=0.022, rely=0.182, height=19, width=31
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Year''')
        self.TLabel1.configure(compound='left')

        self.TLabel1_1 = ttk.Label(self.TLabelframe1)
        self.TLabel1_1.place(relx=0.022, rely=0.364, height=26, width=46
                , bordermode='ignore')
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="TkDefaultFont")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Make''')
        self.TLabel1_1.configure(compound='left')

        self.TLabel1_1_1 = ttk.Label(self.TLabelframe1)
        self.TLabel1_1_1.place(relx=0.402, rely=0.182, height=26, width=46
                , bordermode='ignore')
        self.TLabel1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1.configure(foreground="#000000")
        self.TLabel1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1.configure(relief="flat")
        self.TLabel1_1_1.configure(anchor='w')
        self.TLabel1_1_1.configure(justify='left')
        self.TLabel1_1_1.configure(text='''Color''')
        self.TLabel1_1_1.configure(compound='left')
        self.TLabel1_1_1.configure(cursor="fleur")

        self.ModelEntry = ttk.Entry(self.TLabelframe1)
        self.ModelEntry.place(relx=0.163, rely=0.545, relheight=0.127
                , relwidth=0.178, bordermode='ignore')
        self.ModelEntry.configure(textvariable=self.modelValue)
        self.ModelEntry.configure(takefocus="")
        self.ModelEntry.configure(cursor="xterm")

        self.TLabel4 = ttk.Label(self.TLabelframe1)
        self.TLabel4.place(relx=0.022, rely=0.545, height=19, width=42
                , bordermode='ignore')
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Model''')
        self.TLabel4.configure(compound='left')

        self.MilesEnty = ttk.Entry(self.TLabelframe1)
        self.MilesEnty.place(relx=0.163, rely=0.727, relheight=0.127
                , relwidth=0.178, bordermode='ignore')
        self.MilesEnty.configure(textvariable=self.milesValue)
        self.MilesEnty.configure(takefocus="")
        self.MilesEnty.configure(cursor="xterm")

        self.TLabel4 = ttk.Label(self.TLabelframe1)
        self.TLabel4.place(relx=0.022, rely=0.727, height=19, width=37
                , bordermode='ignore')
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Miles''')
        self.TLabel4.configure(compound='left')

        self.TButton2 = ttk.Button(self.TLabelframe1)
        self.TButton2.place(relx=0.804, rely=0.788, height=28, width=83
                , bordermode='ignore')
        self.TButton2.configure(command=vehicle_search_support.clearButtonClick)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Clear''')
        self.TButton2.configure(compound='left')

def start_up():
    vehicle_search_support.main()

if __name__ == '__main__':
    vehicle_search_support.main()




