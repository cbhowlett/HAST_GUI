#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Oct 04, 2019 01:35:57 PM PDT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from PIL import Image, ImageTk

import HAST_PreProcess_GUI_support
import os.path

import HAST_Analysis_GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    ########################
    ######################
    HAST_Analysis_GUI_support.set_Tk_var()
    top = Toplevel1 (root)
    HAST_Analysis_GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    HAST_Analysis_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("607x487+546+167")
        
        # Gets the requested values of the height and widht.
        windowWidth = 607#top.winfo_reqwidth()
        windowHeight = 487#top.winfo_reqheight()
        print(windowWidth,windowHeight)
        # Gets both half the screen width/height and window width/height
        positionRight = int(top.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(top.winfo_screenheight()/2 - windowHeight/2)
         
        # Positions the window in the center of the page.
        top.geometry("+{}+{}".format(positionRight, positionDown))
        
        
        top.title("HAST - Analyze")
        top.configure(background="#87CEFA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.SelectInput = tk.Button(top)
        self.SelectInput.place(relx=0.906, rely=0.667, height=35, width=35)
        self.SelectInput.configure(activebackground="#ececec")
        self.SelectInput.configure(activeforeground="#000000")
        self.SelectInput.configure(background="#87CEFA")
        self.SelectInput.configure(command=lambda: HAST_Analysis_GUI_support.browse_button(self.Run,{'Longitude*':self.LongitudeEntry,
    'Latitude*':self.LatitudeEntry,
    'SOID*':self.SOIDEntry,
    'BuildingArea*':self.BuildingAreaEntry,
    'BuildingValue*':self.BuildingValueEntry,
    'HUSBT*':self.HUSBTEntry,
    'TerrainID*':self.TerrainIDEntry,
    'WBID*':self.WBIDEntry
    }))
        self.SelectInput.configure(disabledforeground="#a3a3a3")
        self.SelectInput.configure(foreground="#000000")
        self.SelectInput.configure(highlightbackground="#d9d9d9")
        self.SelectInput.configure(highlightcolor="black")
        photo_location = os.path.join(os.path.dirname(os.getcwd()),'images',"FileOpen_small.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.SelectInput.configure(image=_img0)
        self.SelectInput.configure(pady="0")

        self.RequiredFields = tk.LabelFrame(top)
        self.RequiredFields.place(relx=0.0, rely=0.021, relheight=0.626
                , relwidth=0.56)
        self.RequiredFields.configure(relief='groove')
        self.RequiredFields.configure(foreground="black")
        self.RequiredFields.configure(text='''Required Input Fields''')
        self.RequiredFields.configure(background="#87CEFA")
        self.RequiredFields.configure(highlightbackground="#d9d9d9")
        self.RequiredFields.configure(highlightcolor="black")

        self.Longitude = tk.Label(self.RequiredFields)
        self.Longitude.place(relx=0.029, rely=0.098, height=26, width=82
                , bordermode='ignore')
        self.Longitude.configure(activebackground="#f9f9f9")
        self.Longitude.configure(activeforeground="black")
        self.Longitude.configure(anchor='w')
        self.Longitude.configure(background="#87CEFA")
        self.Longitude.configure(disabledforeground="#a3a3a3")
        self.Longitude.configure(foreground="#000000")
        self.Longitude.configure(highlightbackground="#d9d9d9")
        self.Longitude.configure(highlightcolor="black")
        self.Longitude.configure(text='''Longitude*:''')

        self.LongitudeEntry = tk.Entry(self.RequiredFields)
        self.LongitudeEntry.place(relx=0.706, rely=0.098, height=24
                , relwidth=0.276, bordermode='ignore')
        self.LongitudeEntry.configure(background="white")
        self.LongitudeEntry.configure(disabledforeground="#a3a3a3")
        self.LongitudeEntry.configure(font="TkFixedFont")
        self.LongitudeEntry.configure(foreground="#000000")
        self.LongitudeEntry.configure(highlightbackground="#d9d9d9")
        self.LongitudeEntry.configure(highlightcolor="black")
        self.LongitudeEntry.configure(insertbackground="black")
        self.LongitudeEntry.configure(selectbackground="#c4c4c4")
        self.LongitudeEntry.configure(selectforeground="black")

        self.Latitude = tk.Label(self.RequiredFields)
        self.Latitude.place(relx=0.029, rely=0.197, height=26, width=66
                , bordermode='ignore')
        self.Latitude.configure(activebackground="#f9f9f9")
        self.Latitude.configure(activeforeground="black")
        self.Latitude.configure(anchor='w')
        self.Latitude.configure(background="#87CEFA")
        self.Latitude.configure(disabledforeground="#a3a3a3")
        self.Latitude.configure(foreground="#000000")
        self.Latitude.configure(highlightbackground="#d9d9d9")
        self.Latitude.configure(highlightcolor="black")
        self.Latitude.configure(text='''Latitude*:''')

        self.LatitudeEntry = tk.Entry(self.RequiredFields)
        self.LatitudeEntry.place(relx=0.706, rely=0.197, height=24
                , relwidth=0.276, bordermode='ignore')
        self.LatitudeEntry.configure(background="white")
        self.LatitudeEntry.configure(disabledforeground="#a3a3a3")
        self.LatitudeEntry.configure(font="TkFixedFont")
        self.LatitudeEntry.configure(foreground="#000000")
        self.LatitudeEntry.configure(highlightbackground="#d9d9d9")
        self.LatitudeEntry.configure(highlightcolor="black")
        self.LatitudeEntry.configure(insertbackground="black")
        self.LatitudeEntry.configure(selectbackground="#c4c4c4")
        self.LatitudeEntry.configure(selectforeground="black")

        self.SOID = tk.Label(self.RequiredFields)
        self.SOID.place(relx=0.029, rely=0.295, height=26, width=166
                , bordermode='ignore')
        self.SOID.configure(activebackground="#f9f9f9")
        self.SOID.configure(activeforeground="black")
        self.SOID.configure(anchor='w')
        self.SOID.configure(background="#87CEFA")
        self.SOID.configure(disabledforeground="#a3a3a3")
        self.SOID.configure(foreground="#000000")
        self.SOID.configure(highlightbackground="#d9d9d9")
        self.SOID.configure(highlightcolor="black")
        self.SOID.configure(text='''Specific Occupancy Id*:''')

        self.BuildingArea = tk.Label(self.RequiredFields)
        self.BuildingArea.place(relx=0.029, rely=0.393, height=26, width=106
                , bordermode='ignore')
        self.BuildingArea.configure(activebackground="#f9f9f9")
        self.BuildingArea.configure(activeforeground="black")
        self.BuildingArea.configure(anchor='w')
        self.BuildingArea.configure(background="#87CEFA")
        self.BuildingArea.configure(disabledforeground="#a3a3a3")
        self.BuildingArea.configure(foreground="#000000")
        self.BuildingArea.configure(highlightbackground="#d9d9d9")
        self.BuildingArea.configure(highlightcolor="black")
        self.BuildingArea.configure(text='''Building Area*:''')

        self.BuildingValue = tk.Label(self.RequiredFields)
        self.BuildingValue.place(relx=0.029, rely=0.492, height=26, width=116
                , bordermode='ignore')
        self.BuildingValue.configure(activebackground="#f9f9f9")
        self.BuildingValue.configure(activeforeground="black")
        self.BuildingValue.configure(anchor='w')
        self.BuildingValue.configure(background="#87CEFA")
        self.BuildingValue.configure(disabledforeground="#a3a3a3")
        self.BuildingValue.configure(foreground="#000000")
        self.BuildingValue.configure(highlightbackground="#d9d9d9")
        self.BuildingValue.configure(highlightcolor="black")
        self.BuildingValue.configure(text='''Building Value*:''')

        self.HUSBT = tk.Label(self.RequiredFields)
        self.HUSBT.place(relx=0.029, rely=0.59, height=26, width=226
                , bordermode='ignore')
        self.HUSBT.configure(activebackground="#f9f9f9")
        self.HUSBT.configure(activeforeground="black")
        self.HUSBT.configure(anchor='w')
        self.HUSBT.configure(background="#87CEFA")
        self.HUSBT.configure(disabledforeground="#a3a3a3")
        self.HUSBT.configure(foreground="#000000")
        self.HUSBT.configure(highlightbackground="#d9d9d9")
        self.HUSBT.configure(highlightcolor="black")
        self.HUSBT.configure(text='''Hurricane Specific Building Type*:''')

        self.BuildingAreaEntry = tk.Entry(self.RequiredFields)
        self.BuildingAreaEntry.place(relx=0.706, rely=0.393, height=24
                , relwidth=0.276, bordermode='ignore')
        self.BuildingAreaEntry.configure(background="white")
        self.BuildingAreaEntry.configure(disabledforeground="#a3a3a3")
        self.BuildingAreaEntry.configure(font="TkFixedFont")
        self.BuildingAreaEntry.configure(foreground="#000000")
        self.BuildingAreaEntry.configure(highlightbackground="#d9d9d9")
        self.BuildingAreaEntry.configure(highlightcolor="black")
        self.BuildingAreaEntry.configure(insertbackground="black")
        self.BuildingAreaEntry.configure(selectbackground="#c4c4c4")
        self.BuildingAreaEntry.configure(selectforeground="black")

        self.BuildingValueEntry = tk.Entry(self.RequiredFields)
        self.BuildingValueEntry.place(relx=0.706, rely=0.492, height=24
                , relwidth=0.276, bordermode='ignore')
        self.BuildingValueEntry.configure(background="white")
        self.BuildingValueEntry.configure(disabledforeground="#a3a3a3")
        self.BuildingValueEntry.configure(font="TkFixedFont")
        self.BuildingValueEntry.configure(foreground="#000000")
        self.BuildingValueEntry.configure(highlightbackground="#d9d9d9")
        self.BuildingValueEntry.configure(highlightcolor="black")
        self.BuildingValueEntry.configure(insertbackground="black")
        self.BuildingValueEntry.configure(selectbackground="#c4c4c4")
        self.BuildingValueEntry.configure(selectforeground="black")

        self.HUSBTEntry = tk.Entry(self.RequiredFields)
        self.HUSBTEntry.place(relx=0.706, rely=0.59, height=24, relwidth=0.276
                , bordermode='ignore')
        self.HUSBTEntry.configure(background="white")
        self.HUSBTEntry.configure(disabledforeground="#a3a3a3")
        self.HUSBTEntry.configure(font="TkFixedFont")
        self.HUSBTEntry.configure(foreground="#000000")
        self.HUSBTEntry.configure(highlightbackground="#d9d9d9")
        self.HUSBTEntry.configure(highlightcolor="black")
        self.HUSBTEntry.configure(insertbackground="black")
        self.HUSBTEntry.configure(selectbackground="#c4c4c4")
        self.HUSBTEntry.configure(selectforeground="black")

        self.SOIDEntry = tk.Entry(self.RequiredFields)
        self.SOIDEntry.place(relx=0.706, rely=0.295, height=24, relwidth=0.276
                , bordermode='ignore')
        self.SOIDEntry.configure(background="white")
        self.SOIDEntry.configure(disabledforeground="#a3a3a3")
        self.SOIDEntry.configure(font="TkFixedFont")
        self.SOIDEntry.configure(foreground="#000000")
        self.SOIDEntry.configure(highlightbackground="#d9d9d9")
        self.SOIDEntry.configure(highlightcolor="black")
        self.SOIDEntry.configure(insertbackground="black")
        self.SOIDEntry.configure(selectbackground="#c4c4c4")
        self.SOIDEntry.configure(selectforeground="black")

        self.TerrainID = tk.Label(self.RequiredFields)
        self.TerrainID.place(relx=0.029, rely=0.689, height=26, width=136
                , bordermode='ignore')
        self.TerrainID.configure(activebackground="#f9f9f9")
        self.TerrainID.configure(activeforeground="black")
        self.TerrainID.configure(anchor='w')
        self.TerrainID.configure(background="#87CEFA")
        self.TerrainID.configure(disabledforeground="#a3a3a3")
        self.TerrainID.configure(foreground="#000000")
        self.TerrainID.configure(highlightbackground="#d9d9d9")
        self.TerrainID.configure(highlightcolor="black")
        self.TerrainID.configure(text='''Terrain Id*:''')

        self.TerrainIDEntry = tk.Entry(self.RequiredFields)
        self.TerrainIDEntry.place(relx=0.706, rely=0.689, height=24
                , relwidth=0.276, bordermode='ignore')
        self.TerrainIDEntry.configure(background="white")
        self.TerrainIDEntry.configure(disabledforeground="#a3a3a3")
        self.TerrainIDEntry.configure(font="TkFixedFont")
        self.TerrainIDEntry.configure(foreground="#000000")
        self.TerrainIDEntry.configure(highlightbackground="#d9d9d9")
        self.TerrainIDEntry.configure(highlightcolor="black")
        self.TerrainIDEntry.configure(insertbackground="black")
        self.TerrainIDEntry.configure(selectbackground="#c4c4c4")
        self.TerrainIDEntry.configure(selectforeground="black")

        self.WBID = tk.Label(self.RequiredFields)
        self.WBID.place(relx=0.029, rely=0.787, height=26, width=136
                , bordermode='ignore')
        self.WBID.configure(activebackground="#f9f9f9")
        self.WBID.configure(activeforeground="black")
        self.WBID.configure(anchor='w')
        self.WBID.configure(background="#87CEFA")
        self.WBID.configure(disabledforeground="#a3a3a3")
        self.WBID.configure(foreground="#000000")
        self.WBID.configure(highlightbackground="#d9d9d9")
        self.WBID.configure(highlightcolor="black")
        self.WBID.configure(text='''Wb Id*:''')

        self.WBIDEntry = tk.Entry(self.RequiredFields)
        self.WBIDEntry.place(relx=0.706, rely=0.787, height=24, relwidth=0.276
                , bordermode='ignore')
        self.WBIDEntry.configure(background="white")
        self.WBIDEntry.configure(disabledforeground="#a3a3a3")
        self.WBIDEntry.configure(font="TkFixedFont")
        self.WBIDEntry.configure(foreground="#000000")
        self.WBIDEntry.configure(highlightbackground="#d9d9d9")
        self.WBIDEntry.configure(highlightcolor="black")
        self.WBIDEntry.configure(insertbackground="black")
        self.WBIDEntry.configure(selectbackground="#c4c4c4")
        self.WBIDEntry.configure(selectforeground="black")

        self.OptionalFields = tk.LabelFrame(top)
        self.OptionalFields.place(relx=0.56, rely=0.021, relheight=0.626
                , relwidth=0.438)
        self.OptionalFields.configure(relief='groove')
        self.OptionalFields.configure(foreground="black")
        self.OptionalFields.configure(text='''Optional Fields''')
        self.OptionalFields.configure(background="#87CEFA")
        self.OptionalFields.configure(highlightbackground="#d9d9d9")
        self.OptionalFields.configure(highlightcolor="black")

        self.Run = tk.Button(top)
        self.Run.place(relx=0.247, rely=0.924, height=33, width=90)
        self.Run.configure(activebackground="#ececec")
        self.Run.configure(activeforeground="#000000")
        self.Run.configure(background="#87CEFA")
        self.Run.configure(command=HAST_Analysis_GUI_support.analyze)
        self.Run.configure(disabledforeground="#a3a3a3")
        self.Run.configure(foreground="#000000")
        self.Run.configure(highlightbackground="#d9d9d9")
        self.Run.configure(highlightcolor="black")
        self.Run.configure(pady="0")
        self.Run.configure(text='''Run''')

        self.QuitButton = tk.Button(top)
        self.QuitButton.place(relx=0.577, rely=0.924, height=33, width=90)
        self.QuitButton.configure(activebackground="#ececec")
        self.QuitButton.configure(activeforeground="#000000")
        self.QuitButton.configure(background="#87CEFA")
        self.QuitButton.configure(command=HAST_Analysis_GUI_support.Exit)
        self.QuitButton.configure(disabledforeground="#a3a3a3")
        self.QuitButton.configure(foreground="#000000")
        self.QuitButton.configure(highlightbackground="#d9d9d9")
        self.QuitButton.configure(highlightcolor="black")
        self.QuitButton.configure(pady="0")
        self.QuitButton.configure(text='''Exit''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.016, rely=0.575, height=26, width=182)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#87CEFA")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''* Indicates a required field.''')

        self.MainScreenButton = tk.Button(top)
        self.MainScreenButton.place(relx=0.412, rely=0.924, height=33, width=90)
        self.MainScreenButton.configure(activebackground="#ececec")
        self.MainScreenButton.configure(activeforeground="#000000")
        self.MainScreenButton.configure(background="#87CEFA")
        self.MainScreenButton.configure(command=HAST_Analysis_GUI_support.MainScreen)
        self.MainScreenButton.configure(disabledforeground="#a3a3a3")
        self.MainScreenButton.configure(foreground="#000000")
        self.MainScreenButton.configure(highlightbackground="#d9d9d9")
        self.MainScreenButton.configure(highlightcolor="black")
        self.MainScreenButton.configure(pady="0")
        self.MainScreenButton.configure(text='''Main Menu''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.016, rely=0.801, height=26, width=152)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#87CEFA")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Select Windfield data:''')

        self.SelectWinfieldButton = tk.Button(top)
        self.SelectWinfieldButton.place(relx=0.906, rely=0.791, height=35
                , width=35)
        self.SelectWinfieldButton.configure(activebackground="#ececec")
        self.SelectWinfieldButton.configure(activeforeground="#000000")
        self.SelectWinfieldButton.configure(background="#87CEFA")
        self.SelectWinfieldButton.configure(command=HAST_Analysis_GUI_support.SelectWindfield)
        self.SelectWinfieldButton.configure(disabledforeground="#a3a3a3")
        self.SelectWinfieldButton.configure(foreground="#000000")
        self.SelectWinfieldButton.configure(highlightbackground="#d9d9d9")
        self.SelectWinfieldButton.configure(highlightcolor="black")
        photo_location = os.path.join(os.path.dirname(os.getcwd()),'images',"FileOpen_small.jpg")
        global _img1
        _img1 = ImageTk.PhotoImage(file=photo_location)
        self.SelectWinfieldButton.configure(image=_img1)
        self.SelectWinfieldButton.configure(pady="0")
        self.SelectWinfieldButton.configure(text='''...''')

        self.WindfieldEntry = tk.Entry(top)
        self.WindfieldEntry.place(relx=0.28, rely=0.801, height=24, relwidth=0.6)

        self.WindfieldEntry.configure(background="white")
        self.WindfieldEntry.configure(disabledforeground="#a3a3a3")
        self.WindfieldEntry.configure(font="TkFixedFont")
        self.WindfieldEntry.configure(foreground="#000000")
        self.WindfieldEntry.configure(insertbackground="black")
        self.WindfieldEntry.configure(textvariable=HAST_Analysis_GUI_support.WindVar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.016, rely=0.678, height=26, width=87)
        self.Label3.configure(anchor='nw')
        self.Label3.configure(background="#87CEFA")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Select Input:''')

        self.SelectFile = tk.Entry(top)
        self.SelectFile.place(relx=0.28, rely=0.678,height=24, relwidth=0.6)
        self.SelectFile.configure(background="white")
        self.SelectFile.configure(disabledforeground="#a3a3a3")
        self.SelectFile.configure(font="TkFixedFont")
        self.SelectFile.configure(foreground="#000000")
        self.SelectFile.configure(highlightbackground="#d9d9d9")
        self.SelectFile.configure(highlightcolor="black")
        self.SelectFile.configure(insertbackground="black")
        self.SelectFile.configure(selectbackground="#c4c4c4")
        self.SelectFile.configure(selectforeground="black")
        self.SelectFile.configure(textvariable=HAST_Analysis_GUI_support.SelectVar)

if __name__ == '__main__':
    vp_start_gui()





