# coding=utf-8

from PyQt5.QtWidgets import QWidget, QGroupBox, QGridLayout, QLineEdit, QLabel


class MaterialFrame:

    def __init__(self, parent, x=100, y=100):
        super().__init__()
        self.parent = parent

        self.boxGroup = QGroupBox('Material Selection', self.parent)

        self.gridLayout = QGridLayout(self.boxGroup)

        self.label_Density = QLabel('Density (kg/m^3)', self.boxGroup)
        self.entry_Density = QLineEdit(self.boxGroup)

        self.label_spHeat = QLabel('Specific Heat (J/Kg.K)', self.boxGroup)
        self.entry_spHeat = QLineEdit(self.boxGroup)

        self.label_Conductivity = QLabel('Thermal Conductivity (W/m.K)', self.boxGroup)
        self.entry_Conductivity = QLineEdit(self.boxGroup)

        self.label_meltPt = QLabel('Melting Temperature (K)', self.boxGroup)
        self.entry_meltPt = QLineEdit(self.boxGroup)

        self.label_Emissivity = QLabel('Emissivity (0-1)', self.boxGroup)
        self.entry_Emissivity = QLineEdit(self.boxGroup)

        self.label_Reflect = QLabel('Reflectivity (0-1)', self.boxGroup)
        self.entry_Reflect = QLineEdit(self.boxGroup)

        self.label_blank = QLabel(' ', self.boxGroup)
        self.label_blank.setFixedWidth(20)

        self.gridLayout.addWidget(self.label_Density, 0, 0)
        self.gridLayout.addWidget(self.entry_Density, 0, 1)
        self.gridLayout.addWidget(self.label_blank, 0, 2)
        self.gridLayout.addWidget(self.label_spHeat, 0, 3)
        self.gridLayout.addWidget(self.entry_spHeat, 0, 4)

        self.gridLayout.addWidget(self.label_Conductivity, 1, 0)
        self.gridLayout.addWidget(self.entry_Conductivity, 1, 1)

        self.gridLayout.addWidget(self.label_meltPt, 1, 3)
        self.gridLayout.addWidget(self.entry_meltPt, 1, 4)

        self.gridLayout.addWidget(self.label_Emissivity, 2, 0)
        self.gridLayout.addWidget(self.entry_Emissivity, 2, 1)

        self.gridLayout.addWidget(self.label_Reflect, 2, 3)
        self.gridLayout.addWidget(self.entry_Reflect, 2, 4)

        self.boxGroup.setLayout(self.gridLayout)

