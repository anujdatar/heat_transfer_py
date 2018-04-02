# coding=utf-8

""" Main App """

import sys
from scripts import MainAppQt
from scripts import MainAppTk


current_gui = "PySide"

try:
    from PySide2 import QtWidgets
except ImportError:
    import tkinter as tk
    current_gui = 'Tkinter'
    print("pyside unavailable, fallback to Tkinter")


if __name__ == '__main__':

    if current_gui == 'PySide':
        app = QtWidgets.QApplication(sys.argv)
        ex = MainAppQt()
        sys.exit(app.exec_())

    elif current_gui == 'Tkinter':
        root = tk.Tk()
        MainAppTk(root)
        root.mainloop()
