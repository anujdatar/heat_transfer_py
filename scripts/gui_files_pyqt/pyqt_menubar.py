# coding=utf-8

import sys
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class GenerateMenu:
    def __init__(self, parent):
        self.parent = parent

        self.menu_top = self.parent.menuBar()
        self.file_menu = self.menu_top.addMenu('File')
        self.edit_menu = self.menu_top.addMenu('Edit')
        self.help_menu = self.menu_top.addMenu('Help')

        # %%%%%%% add/edit material button
        self.option_new_material = QAction('Add/Edit Material', self.parent)
        self.option_new_material.setStatusTip('Add or edit a material in database')
        self.edit_menu.addAction(self.option_new_material)

        # %%%%%%%%%%%%%% exit button
        # __ico_file = '/opt/google/chrome/product_logo_64.png'
        option_exit = QAction(QIcon('exit.png'), 'Exit', self.parent)
        option_exit.setShortcut('Ctrl+Q')
        option_exit.setStatusTip('Exit application')
        option_exit.triggered.connect(QCoreApplication.instance().quit)
        self.file_menu.addAction(option_exit)

        # %%%%%%%%%%%% about button
        option_about = QAction('About', self.parent)
        self.help_menu.addAction(option_about)
