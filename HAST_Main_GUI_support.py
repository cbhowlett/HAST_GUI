#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 30, 2019 05:38:55 PM PDT  platform: Windows NT

import sys, webbrowser, os

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

def set_Tk_var():
    global selectedButton
    selectedButton = tk.StringVar()

def destroy_window():
    print('HAST_Main_GUI_support.destroy_window')
    sys.stdout.flush()

def run():
    try: import HAST_PreProcess_GUI_support
    except: pass
    try: import HAST_Analysis_GUI_support
    except: pass
    if selectedButton.get() != '':
        destroy_window()
        if selectedButton.get() == '2': HAST_PreProcess_GUI_support.start_program()
        elif selectedButton.get() == '1': HAST_Analysis_GUI_support.start_program()
        sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    root.iconbitmap('../Images/Hu_Symbol.ico')
    def callback(url):
        webbrowser.open_new(url)
    w.Message1.bind("<Button-1>", lambda e: callback(os.path.join(os.path.dirname(os.getcwd()),'help','readme.txt')))
    
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print(windowWidth,windowHeight)
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight)
     
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    
def start_program():
    import HAST_Main_GUI
    HAST_Main_GUI.vp_start_gui()
    
if __name__ == '__main__':
    import HAST_Main_GUI
    HAST_Main_GUI.vp_start_gui()




