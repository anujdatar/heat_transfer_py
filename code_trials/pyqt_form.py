# coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QAction,
                             QLabel)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication


class SampleMain(QMainWindow):

    def __init__(self, width=640, height=480):
        super().__init__()

        self.setGeometry(50, 50, width, height)
        self.setWindowTitle('Sample Window')
        self.setWindowIcon(QIcon('web.png'))
        self.statusBar().showMessage('Welcome')

        GenerateMenu(self)
        SampleForm(self)

        self.show()


class SampleForm(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent

        self.label_density = QLabel('Density', self.parent)
        # self.label_density.move(100, 100)


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
        __ico_file = '/opt/google/chrome/product_logo_64.png'
        self.option_exit = QAction(QIcon('exit.png'), 'Exit', self.parent)
        self.option_exit.setShortcut('Ctrl+Q')
        self.option_exit.setStatusTip('Exit application')
        self.option_exit.triggered.connect(QCoreApplication.instance().quit)
        self.file_menu.addAction(self.option_exit)

        # %%%%%%%%%%%% about button
        self.option_about = QAction('About', self.parent)
        self.help_menu.addAction(self.option_about)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SampleMain()
    sys.exit(app.exec_())
