# coding=utf-8

from PySide2.QtWidgets import (QGroupBox, QGridLayout, QLineEdit, QLabel)
from PySide2.QtCore import Qt
from scripts.import_settings import ProcessSettings


class ProcessFrame:

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.process = ProcessSettings()

        self.boxGroup = QGroupBox("Process Settings", self.parent)
        self.gridLayout = QGridLayout(self.boxGroup)

        self.label_laser_power = QLabel("Laser Power", self.boxGroup)
        self.label_laser_power.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_laser_power_units = QLabel("W", self.boxGroup)
        self.label_laser_power_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_laser_power = QLineEdit(self.boxGroup)
        self.entry_laser_power.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_laser_spot = QLabel("Laser Spot Size", self.boxGroup)
        self.label_laser_spot.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_laser_spot_units = QLabel("m^2", self.boxGroup)
        self.label_laser_spot_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_laser_spot = QLineEdit(self.boxGroup)
        self.entry_laser_spot.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_scan_vel = QLabel("Laser Scanning Velocity", self.boxGroup)
        self.label_scan_vel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_scan_vel_units = QLabel("m/s", self.boxGroup)
        self.label_scan_vel_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_scan_vel = QLineEdit(self.boxGroup)
        self.entry_scan_vel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_ambient = QLabel("Ambient Temperature", self.boxGroup)
        self.label_ambient.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_ambient_units = QLabel("K", self.boxGroup)
        self.label_ambient_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_ambient = QLineEdit(self.boxGroup)
        self.entry_ambient.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.label_HT_coeff = QLabel("Convective HT Coefficient", self.boxGroup)
        self.label_HT_coeff.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_HT_coeff_units = QLabel("W/m^2.K", self.boxGroup)
        self.label_HT_coeff_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_HT_coeff = QLineEdit(self.boxGroup)
        self.entry_HT_coeff.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_laser_power, 0, 0)
        self.gridLayout.addWidget(self.entry_laser_power, 0, 1)
        self.gridLayout.addWidget(self.label_laser_power_units, 0, 2)

        self.gridLayout.addWidget(self.label_laser_spot, 1, 0)
        self.gridLayout.addWidget(self.entry_laser_spot, 1, 1)
        self.gridLayout.addWidget(self.label_laser_spot_units, 1, 2)

        self.gridLayout.addWidget(self.label_scan_vel, 2, 0)
        self.gridLayout.addWidget(self.entry_scan_vel, 2, 1)
        self.gridLayout.addWidget(self.label_scan_vel_units, 2, 2)

        self.gridLayout.addWidget(self.label_ambient, 3, 0)
        self.gridLayout.addWidget(self.entry_ambient, 3, 1)
        self.gridLayout.addWidget(self.label_ambient_units, 3, 2)

        self.gridLayout.addWidget(self.label_HT_coeff, 4, 0)
        self.gridLayout.addWidget(self.entry_HT_coeff, 4, 1)
        self.gridLayout.addWidget(self.label_HT_coeff_units, 4, 2)

        self.boxGroup.setLayout(self.gridLayout)
        self.update_process_settings()

    def update_process_settings(self):
        self.entry_laser_power.setText(str(self.process.laser_power))
        self.entry_laser_spot.setText(str(self.process.laser_spot_size))
        self.entry_scan_vel.setText(str(self.process.laser_velocity))
        self.entry_ambient.setText(str(self.process.temperature_inf))
        self.entry_HT_coeff.setText(str(self.process.convection_coeff))
