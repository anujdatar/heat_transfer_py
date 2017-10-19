# coding=utf-8

import sys
from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtGui as Qtg


class SampleMain(Qtw.QMainWindow):

    def __init__(self, width=640, height=480):
        super().__init__()

        self.setWindowTitle('Sample Window')
        self.setGeometry(50, 50, width, height)
        self.statusBar().showMessage('Welcome')

        GenerateMenu(self)

        self.show()


class SampleForm(Qtw.QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent


class GenerateMenu:
    def __init__(self, parent):
        self.parent = parent

        menu_top = self.parent.menuBar()
        file_menu = menu_top.addMenu('File')
        edit_menu = menu_top.addMenu('Edit')
        help_menu = menu_top.addMenu('Help')

        # %%%%%%% add/edit material button
        option_new_material = Qtw.QAction('Add/Edit Material', self.parent)
        option_new_material.setStatusTip('Add or edit a material in database')
        edit_menu.addAction(option_new_material)

        # %%%%%%%%%%%%%% exit button
        option_exit = Qtw.QAction('Exit', self.parent)
        option_exit.setShortcut('Ctrl+Q')
        option_exit.setStatusTip('Exit application')
        option_exit.triggered.connect(self.parent.close)
        file_menu.addAction(option_exit)

        # %%%%%%%%%%%% about button
        option_about = Qtw.QAction('About', self.parent)
        help_menu.addAction(option_about)


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    ex = SampleMain()
    sys.exit(app.exec_())
