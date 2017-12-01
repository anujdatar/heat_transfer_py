# coding=utf-8

from PyQt5.QtWidgets import (QGroupBox, QGridLayout, QLineEdit, QLabel,
                             QHBoxLayout, QComboBox)
from PyQt5.QtCore import Qt
from scripts.import_settings import MaterialProperties


class MaterialFrame:

    def __init__(self, parent, box_type='select'):
        super().__init__()
        self.parent = parent
        self.box_type = box_type
        self.material = MaterialProperties()
        self.material_name = ''

        self.boxGroup = QGroupBox('Material Settings', self.parent)
        self.gridLayout = QGridLayout(self.boxGroup)

        self.materialBoxGroup = QGroupBox('', self.boxGroup)
        self.miniLayout = QHBoxLayout(self.materialBoxGroup)
        self.label_mat_name = QLabel(self.materialBoxGroup)
        self.label_mat_name.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.material_name_wid = QComboBox()

        self.miniLayout.addWidget(self.label_mat_name)
        # self.miniLayout.addWidget(self.material_name_wid)
        self.materialBoxGroup.setLayout(self.miniLayout)

        self.label_Density = QLabel('Density (kg/m^3)', self.boxGroup)
        self.label_Density.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_Density = QLineEdit(self.boxGroup)

        self.label_spHeat = QLabel('Specific Heat (J/Kg.K)', self.boxGroup)
        self.label_spHeat.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_spHeat = QLineEdit(self.boxGroup)

        self.label_Conductivity = QLabel('Thermal Conductivity (W/m.K)',
                                         self.boxGroup)
        self.label_Conductivity.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_Conductivity = QLineEdit(self.boxGroup)

        self.label_meltPt = QLabel('Melting Temperature (K)', self.boxGroup)
        self.label_meltPt.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_meltPt = QLineEdit(self.boxGroup)

        self.label_Emissivity = QLabel('Emissivity (0-1)', self.boxGroup)
        self.label_Emissivity.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_Emissivity = QLineEdit(self.boxGroup)

        self.label_Reflect = QLabel('Reflectivity (0-1)', self.boxGroup)
        self.label_Reflect.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.entry_Reflect = QLineEdit(self.boxGroup)

        self.label_blank = QLabel(' ', self.boxGroup)
        self.label_blank.setFixedWidth(40)

        self.gridLayout.addWidget(self.materialBoxGroup, 0, 0, 1, 3)

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
        if self.box_type == 'entry':
            self.new_material_entry()
        else:
            self.material_select_box()
            self.material_name_wid.activated[str].connect(self.on_material_select)

    def material_select_box(self):
        self.label_mat_name.setText('Select Material')
        self.material_name_wid = QComboBox(self.materialBoxGroup)
        self.miniLayout.addWidget(self.material_name_wid)
        self.update_material_combobox()

    def new_material_entry(self):
        self.label_mat_name.setText('Enter Material Name')
        self.material_name_wid = QLineEdit(self.materialBoxGroup)
        self.miniLayout.addWidget(self.material_name_wid)

    def update_material_combobox(self):
        self.material_name_wid.clear()
        self.material.get_material_list()
        self.material_name_wid.addItems(self.material.material_list)

    def on_material_select(self, text):
        self.material_name = text
        self.material.read_from_json(self.material_name)
        self.entry_Density.setText(str(self.material.density))
        self.entry_spHeat.setText(str(self.material.specific_heat))
        self.entry_Conductivity.setText(str(self.material.conductivity))
        self.entry_meltPt.setText(str(self.material.melting_point))
        self.entry_Emissivity.setText(str(self.material.emissivity))
        self.entry_Reflect.setText(str(self.material.reflectivity))

        print(self.material_name, self.entry_Density.text())
