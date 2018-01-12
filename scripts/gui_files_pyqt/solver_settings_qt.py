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
        # self.solver_name = ''

        self.boxGroup = QGroupBox('Solver Settings', self.parent)
        self.gridLayout = QGridLayout(self.boxGroup)

        self.solverBoxGroup = QGroupBox('', self.boxGroup)
        self.miniLayout = QHBoxLayout(self.solverBoxGroup)
        self.label_solver_name = QLabel('Select Solver', self.solverBoxGroup)
        self.label_solver_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.combo_solver_name = QComboBox()
        self.miniLayout.addWidget(self.label_solver_name)
        self.miniLayout.addWidget(self.combo_solver_name)
        self.solverBoxGroup.setLayout(self.miniLayout)

        self.label_conv_crit = QLabel('Convergence Criterion', self.boxGroup)
        self.label_conv_crit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_conv_crit = QLineEdit(self.boxGroup)

        self.label_max_iter = QLabel('Max # of Iterations', self.boxGroup)
        self.label_max_iter.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_max_iter = QLineEdit(self.boxGroup)

        self.label_relaxation = QLabel('Relaxation Parameter', self.boxGroup)
        self.label_relaxation.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_relaxation = QLineEdit(self.boxGroup)

        self.gridLayout.addWidget(self.solverBoxGroup, 0, 0, 1, 3)

        self.gridLayout.addWidget(self.label_conv_crit, 1, 0)
        self.gridLayout.addWidget(self.entry_conv_crit, 1, 1)

        self.gridLayout.addWidget(self.label_max_iter, 2, 0)
        self.gridLayout.addWidget(self.entry_max_iter, 2, 1)

        self.gridLayout.addWidget(self.label_relaxation, 3, 0)
        self.gridLayout.addWidget(self.entry_relaxation, 3, 1)

        self.boxGroup.setLayout(self.gridLayout)
