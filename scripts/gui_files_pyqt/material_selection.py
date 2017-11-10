# coding=utf-8

from PyQt5.QtWidgets import (QGroupBox, QGridLayout, QLineEdit, QLabel,
                             QHBoxLayout, QComboBox)


class MaterialFrame:

    def __init__(self, parent, x=100, y=100):
        super().__init__()
        self.parent = parent

        self.boxGroup = QGroupBox('Material Settings', self.parent)
        self.gridLayout = QGridLayout(self.boxGroup)

        self.materialboxGroup = QGroupBox('Material Selection', self.boxGroup)
        self.miniLayout = QHBoxLayout(self.materialboxGroup)
        self.label_mat_name = QLabel('Select Material', self.materialboxGroup)
        # self.

        self.label_Density = QLabel('Density (kg/m^3)', self.boxGroup)
        self.entry_Density = QLineEdit(self.boxGroup)

        self.label_spHeat = QLabel('Specific Heat (J/Kg.K)', self.boxGroup)
        self.entry_spHeat = QLineEdit(self.boxGroup)

        self.label_Conductivity = QLabel('Thermal Conductivity (W/m.K)',
                                         self.boxGroup)
        self.entry_Conductivity = QLineEdit(self.boxGroup)

        self.label_meltPt = QLabel('Melting Temperature (K)', self.boxGroup)
        self.entry_meltPt = QLineEdit(self.boxGroup)

        self.label_Emissivity = QLabel('Emissivity (0-1)', self.boxGroup)
        self.entry_Emissivity = QLineEdit(self.boxGroup)

        self.label_Reflect = QLabel('Reflectivity (0-1)', self.boxGroup)
        self.entry_Reflect = QLineEdit(self.boxGroup)

        self.label_blank = QLabel(' ', self.boxGroup)
        self.label_blank.setFixedWidth(20)

        self.gridLayout.addWidget(self.materialboxGroup, 0, 0)

        self.gridLayout.addWidget(self.label_Density, 1, 0)
        self.gridLayout.addWidget(self.entry_Density, 1, 1)
        self.gridLayout.addWidget(self.label_blank, 1, 2)
        self.gridLayout.addWidget(self.label_spHeat, 1, 3)
        self.gridLayout.addWidget(self.entry_spHeat, 1, 4)

        self.gridLayout.addWidget(self.label_Conductivity, 2, 0)
        self.gridLayout.addWidget(self.entry_Conductivity, 2, 1)

        self.gridLayout.addWidget(self.label_meltPt, 2, 3)
        self.gridLayout.addWidget(self.entry_meltPt, 2, 4)

        self.gridLayout.addWidget(self.label_Emissivity, 3, 0)
        self.gridLayout.addWidget(self.entry_Emissivity, 3, 1)

        self.gridLayout.addWidget(self.label_Reflect, 3, 3)
        self.gridLayout.addWidget(self.entry_Reflect, 3, 4)

        self.boxGroup.setLayout(self.gridLayout)

