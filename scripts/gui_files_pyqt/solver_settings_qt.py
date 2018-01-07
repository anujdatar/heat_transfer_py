# coding=utf-8

from PyQt5.QtWidgets import (QGroupBox, QGridLayout, QLineEdit, QLabel,
                             QHBoxLayout, QComboBox)
from PyQt5.QtCore import Qt
from scripts.import_settings import SolverSettings


class SolverFrame:

    def __init(self, parent):
        super().__init__()
        self.parent = parent
        self.solver = SolverSettings()
        self.solver_name = ''

        self.boxGroup = QGroupBox('Solver Settings', self.parent)
        self.gridLayout = QGridLayout(self.boxGroup)

        self.solverBoxGroup = QGroupBox('', self.boxGroup)

