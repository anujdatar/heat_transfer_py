# coding=utf-8

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QAction,
                             QFormLayout, QLabel, QLineEdit, QGroupBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 sample')
        self.setGeometry(50, 50, 1280, 720)
        self.statusBar().showMessage('Welcome')

        # %%%%%%%%%% menu
        generateMenu(self)

        # a = GenerateMaterialBox(self)


        # %%%%%%%%%% quit button
        button_quit = QPushButton('Quit', self)
        button_quit.setToolTip('Close Program')
        button_quit.move(500, 500)
        # button_quit.resize(100, 100)
        button_quit.clicked.connect(self.close)


        # #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
        self.materialGroupBox = QGroupBox('Material Selection')

        self.densityEntry = QLineEdit()
        self.spHeatEntry = QLineEdit()
        self.conductivityEntry = QLineEdit()

        layout = QFormLayout()
        layout.addRow(QLabel('Density (kg/m^3)'), self.densityEntry)
        layout.addRow(QLabel('Specific Heat (J/kg.K)'), self.spHeatEntry)
        layout.addRow(QLabel('Thermal Conductivity (W/m.k)'), self.conductivityEntry)

        self.materialGroupBox.setLayout(layout)



        self.show()

    @pyqtSlot(bool)
    def close_all(self):
        print('yay something worked')
        sys.exit()


class generateMenu:
    def __init__(self, parent):
        self.parent = parent

        menu_top = self.parent.menuBar()
        fileMenu = menu_top.addMenu('File')
        editMenu = menu_top.addMenu('Edit')
        helpMenu = menu_top.addMenu('Help')



        # %%%%%%% add/edit material button
        newMaterialButton = QAction('Add/Edit Material', self.parent)
        newMaterialButton.setStatusTip('Add or edit a material in database')
        editMenu.addAction(newMaterialButton)

        # %%%%%%%%%%%%%% exit button
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self.parent)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.parent.close)
        fileMenu.addAction(exitButton)

        # %%%%%%%%%%%% about button
        aboutButton = QAction('About', self.parent)
        helpMenu.addAction(aboutButton)


class GenerateMaterialBox:

    def __init__(self, parent):
        self.parent = parent

        self.materialGroupBox = QGroupBox('Material Selection')

        self.densityEntry = QLineEdit()
        self.spHeatEntry = QLineEdit()
        self.conductivityEntry = QLineEdit()

        layout = QFormLayout()
        layout.addRow(QLabel('Density (kg/m^3)'), self.densityEntry)
        layout.addRow(QLabel('Specific Heat (J/kg.K)'), self.spHeatEntry)
        layout.addRow(QLabel('Thermal Conductivity (W/m.k)'), self.conductivityEntry)

        self.materialGroupBox.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

