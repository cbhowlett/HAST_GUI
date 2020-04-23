#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 30, 2019 06:35:29 PM PDT  platform: Windows NT

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

import HAST_Main_GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    HAST_Main_GUI_support.set_Tk_var()
    top = Toplevel1 (root)
    HAST_Main_GUI_support.init(root, top)
    HAST_Main_GUI_support.selectedButton.set('2')###########################
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    HAST_Main_GUI_support.set_Tk_var()
    top = Toplevel1 (w)
    HAST_Main_GUI_support.init(w, top, *args, **kwargs)
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

        top.geometry("383x232+972+259")
        top.title("HAST")
        top.configure(background="#97CFFC")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.026, rely=0.043, relheight=0.474
                , relwidth=0.956)
        self.Message1.configure(anchor='nw')
        self.Message1.configure(background="#97CFFC")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Welcome to HAST - Hurricane Analysis Structure Tool 
This wizard will help you pre-process the data required for the analyses. If you have a dataset ready with HU attributes (see ReadMe), please select the Analysis option.''')
        self.Message1.configure(width=366)
        

        self.AnalysisButton = tk.Radiobutton(top)
        self.AnalysisButton.place(relx=0.052, rely=0.647, relheight=0.134
                , relwidth=0.418)
        self.AnalysisButton.configure(activebackground="#ececec")
        self.AnalysisButton.configure(activeforeground="#000000")
        self.AnalysisButton.configure(anchor='nw')
        self.AnalysisButton.configure(background="#97CFFC")
        self.AnalysisButton.configure(disabledforeground="#a3a3a3")
        self.AnalysisButton.configure(foreground="#000000")
        self.AnalysisButton.configure(highlightbackground="#d9d9d9")
        self.AnalysisButton.configure(highlightcolor="black")
        self.AnalysisButton.configure(justify='left')
        self.AnalysisButton.configure(text='''Analyze HU Losses''')
        self.AnalysisButton.configure(value="1")
        self.AnalysisButton.configure(variable=HAST_Main_GUI_support.selectedButton)

        self.PreProcessingButton = tk.Radiobutton(top)
        self.PreProcessingButton.place(relx=0.052, rely=0.517, relheight=0.134
                , relwidth=0.418)
        self.PreProcessingButton.configure(activebackground="#ececec")
        self.PreProcessingButton.configure(activeforeground="#000000")
        self.PreProcessingButton.configure(anchor='nw')
        self.PreProcessingButton.configure(background="#97CFFC")
        self.PreProcessingButton.configure(disabledforeground="#a3a3a3")
        self.PreProcessingButton.configure(foreground="#000000")
        self.PreProcessingButton.configure(highlightbackground="#d9d9d9")
        self.PreProcessingButton.configure(highlightcolor="black")
        self.PreProcessingButton.configure(justify='left')
        self.PreProcessingButton.configure(text='''Pre-Process Input''')
        self.PreProcessingButton.configure(value="2")
        self.PreProcessingButton.configure(variable=HAST_Main_GUI_support.selectedButton)

        self.ExitButton = tk.Button(top)
        self.ExitButton.place(relx=0.339, rely=0.819, height=33, width=90)
        self.ExitButton.configure(activebackground="#ececec")
        self.ExitButton.configure(activeforeground="#000000")
        self.ExitButton.configure(background="#97CFFC")
        self.ExitButton.configure(command=HAST_Main_GUI_support.destroy_window)
        self.ExitButton.configure(disabledforeground="#a3a3a3")
        self.ExitButton.configure(foreground="#000000")
        self.ExitButton.configure(highlightbackground="#d9d9d9")
        self.ExitButton.configure(highlightcolor="black")
        self.ExitButton.configure(pady="0")
        self.ExitButton.configure(text='''Exit''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.065, rely=0.819, height=33, width=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#97CFFC")
        self.Button2.configure(command=HAST_Main_GUI_support.run)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Next''')

if __name__ == '__main__':
    vp_start_gui()




