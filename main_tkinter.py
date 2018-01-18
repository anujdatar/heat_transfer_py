# coding=utf-8

""" Main App """

import tkinter as tk
from sys import platform

from scripts import MainAppTk


if __name__ == '__main__':
    root = tk.Tk()

    if platform == 'win32':
        root.iconbitmap('./images/logo.ico')
    elif platform == 'linux' or platform == 'linux2':
        icon = tk.Image("photo", file=r'./images/logo.png')
        # root.wm_iconphoto(icon)
        # root.call('wm', 'iconphoto', root.w, icon)

    MainAppTk(root)
    root.mainloop()
