# coding=utf-8

import sys
from PySide2.QtWidgets import QMainWindow, QPushButton, QWidget
from PySide2.QtGui import QIcon
from scripts.gui_files_qt import MainMenu
from scripts.gui_files_qt import MaterialFrame
from scripts.gui_files_qt import ProcessFrame
from scripts.gui_files_qt import SolverFrame


class MainAppQt(QMainWindow):

    def __init__(self, width=1280, height=720):
        super().__init__()
        self.setWindowTitle("2D Heat Transfer")
        self.logo = QIcon("./images/logo.png")
        self.setWindowIcon(self.logo)
        self.setGeometry(50, 50, width, height)
        self.statusBar().showMessage("Welcome")
        self.menu = MainMenu(self)

        start_x = 10
        start_y = 35
        self.materialWidget = QWidget(self)
        self.materialWidget.setGeometry(start_x, start_y, 650, 175)
        self.mater_frame = MaterialFrame(self.materialWidget)

        self.processWidget = QWidget(self)
        self.processWidget.setGeometry(start_x, start_y + 175, 350, 175)
        self.process_frame = ProcessFrame(self.processWidget)

        self.solverWidget = QWidget(self)
        self.solverWidget.setGeometry(start_x + 360, start_y + 175, 300, 175)
        self.solver_frame = SolverFrame(self.solverWidget)

        self.show()
