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
        self.material_menu = self.menu_top.addMenu('Materials')
        self.help_menu = self.menu_top.addMenu('Help')

        # %%%%%%% add/edit material button
        self.option_new_material = QAction('Add Material', self.parent)
        self.option_new_material.setStatusTip('Add new material to database')
        self.material_menu.addAction(self.option_new_material)

        self.option_edit_material = QAction('Edit Material', self.parent)
        self.option_edit_material.setStatusTip('Edit existing material '
                                               'in database')
        self.material_menu.addAction(self.option_edit_material)

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
