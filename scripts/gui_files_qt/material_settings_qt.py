# coding=utf-8

from PySide2.QtWidgets import (QGroupBox, QGridLayout, QLineEdit, QLabel,
                               QHBoxLayout, QComboBox)
from PySide2.QtCore import Qt
from scripts.import_settings import MaterialProperties


class MaterialFrame:

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.material = MaterialProperties()
        self.material_name = ""

        self.boxGroup = QGroupBox("Material Settings", self.parent)
        self.gridLayout = QGridLayout(self.boxGroup)

        # %%%%%% material name selection
        self.materialNameGroup = QGroupBox("", self.boxGroup)
        self.miniLlayout = QHBoxLayout(self.materialNameGroup)
        self.label_materialName = QLabel("Select Material",
                                         self.materialNameGroup)
        self.label_materialName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.combo_materialName = QComboBox(self.materialNameGroup)
        self.combo_materialName.setFixedWidth(250)
        self.miniLlayout.addWidget(self.label_materialName)
        self.miniLlayout.addWidget(self.combo_materialName)
        self.materialNameGroup.setLayout(self.miniLlayout)

        # %%%%%% material settings fields
        # material density
        self.label_density = QLabel("Density", self.boxGroup)
        self.label_density.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_density_units = QLabel("kg/m^3", self.boxGroup)
        self.label_density_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_density = QLineEdit(self.boxGroup)

        # specific heat or heat capacity
        self.label_spHeat = QLabel("Specific Heat", self.boxGroup)
        self.label_spHeat.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_spHeat_units = QLabel("J/kg.K", self.boxGroup)
        self.label_spHeat_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_spHeat = QLineEdit(self.boxGroup)

        # thermal conductivity
        self.label_thermalC = QLabel("Thermal Conductivity", self.boxGroup)
        self.label_thermalC.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_thermalC_units = QLabel("W/m.K", self.boxGroup)
        self.label_thermalC_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_thermalC = QLineEdit(self.boxGroup)

        # melting point
        self.label_meltPoint = QLabel("Melting Point", self.boxGroup)
        self.label_meltPoint.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_meltPoint_units = QLabel("K", self.boxGroup)
        self.label_meltPoint_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_meltPoint = QLineEdit(self.boxGroup)

        # emissivity
        self.label_emissivity = QLabel("Emissivity", self.boxGroup)
        self.label_emissivity.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_emissivity_units = QLabel("(0-1)", self.boxGroup)
        self.label_emissivity_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_emissivity = QLineEdit(self.boxGroup)

        # reflectivity
        self.label_reflect = QLabel("Reflectivity", self.boxGroup)
        self.label_reflect.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_reflect_units = QLabel("(0-1)", self.boxGroup)
        self.label_reflect_units.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entry_reflect = QLineEdit(self.boxGroup)

        # blank label for spacing
        self.label_blank = QLabel("", self.boxGroup)
        self.label_blank.setFixedWidth(60)

        # pack all label and entry widgets into the layout
        self.gridLayout.addWidget(self.materialNameGroup, 0, 0, 1, 5)
        self.update_material_combobox()

        self.gridLayout.addWidget(self.label_density, 1, 0)
        self.gridLayout.addWidget(self.entry_density, 1, 1)
        self.gridLayout.addWidget(self.label_density_units, 1, 2)
        self.gridLayout.addWidget(self.label_blank, 1, 3)
        self.gridLayout.addWidget(self.label_spHeat, 1, 4)
        self.gridLayout.addWidget(self.entry_spHeat, 1, 5)
        self.gridLayout.addWidget(self.label_spHeat_units, 1, 6)

        self.gridLayout.addWidget(self.label_thermalC, 2, 0)
        self.gridLayout.addWidget(self.entry_thermalC, 2, 1)
        self.gridLayout.addWidget(self.label_thermalC_units, 2, 2)
        self.gridLayout.addWidget(self.label_meltPoint, 2, 4)
        self.gridLayout.addWidget(self.entry_meltPoint, 2, 5)
        self.gridLayout.addWidget(self.label_meltPoint_units, 2, 6)

        self.gridLayout.addWidget(self.label_emissivity, 3, 0)
        self.gridLayout.addWidget(self.entry_emissivity, 3, 1)
        self.gridLayout.addWidget(self.label_emissivity_units, 3, 2)
        self.gridLayout.addWidget(self.label_reflect, 3, 4)
        self.gridLayout.addWidget(self.entry_reflect, 3, 5)
        self.gridLayout.addWidget(self.label_reflect_units, 3, 6)

        self.boxGroup.setLayout(self.gridLayout)
        self.combo_materialName.activated[str].connect(self.on_material_select)
        print(str(self.combo_materialName))

    def update_material_combobox(self):
        self.combo_materialName.clear()
        self.material.get_material_list()
        self.combo_materialName.addItems(self.material.material_list)

    def on_material_select(self, text):
        self.material_name = text
        self.material.read_from_json(self.material_name)
        self.entry_density.setText(str(self.material.density))
        self.entry_spHeat.setText(str(self.material.specific_heat))
        self.entry_thermalC.setText(str(self.material.conductivity))
        self.entry_meltPoint.setText(str(self.material.melting_point))
        self.entry_emissivity.setText(str(self.material.emissivity))
        self.entry_reflect.setText(str(self.material.reflectivity))
