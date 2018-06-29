# coding=utf-8

import json
import re


class MaterialProperties:
    """ define and retrieve material properties """

    def __init__(self, name=None):
        self.material_name = name
        self.material_file = "./data/materials.json"
        self.material_list = []
        self.material_json = {}
        self.density = 0.
        self.specific_heat = 0.
        self.conductivity = 0.
        self.melting_point = 0.
        self.emissivity = 0.
        self.reflectivity = 0.

        self.get_material_list()

    def get_material_list(self):
        with open(self.material_file, 'r') as _jsfile:
            _data = json.load(_jsfile)
        self.material_list = []
        for _key in _data:
            self.material_list.append(_key)
        self.material_list.sort()

    def read_from_json(self, material_name):
        with open(self.material_file, 'r') as _jsfile:
            _data = json.load(_jsfile)
        self.material_name = material_name
        self.density = _data[material_name]["Density"]
        self.specific_heat = _data[material_name]["SpecificHeat"]
        self.conductivity = _data[material_name]["Conductivity"]
        self.melting_point = _data[material_name]["MeltingTemperature"]
        self.emissivity = _data[material_name]["Emissivity"]
        self.reflectivity = _data[material_name]["Reflectivity"]

    def write_to_json(self):
        with open(self.material_file, 'r') as _output_file:
            _existing_data = json.load(_output_file)
        _existing_data.update(self.material_json)
        with open(self.material_file, 'w') as _output_file1:
            json.dump(_existing_data, _output_file1, indent=4)

    def format_material_as_json(self):
        # format properties for JSON dump
        self.material_json = {self.material_name: {
            "Density": self.density,
            "SpecificHeat": self.specific_heat,
            "Conductivity": self.conductivity,
            "MeltingTemperature": self.melting_point,
            "Emissivity": self.emissivity,
            "Reflectivity": self.reflectivity}}

    def material_name_test(self):
        _new_name = self.material_name
        while _new_name in self.material_list:
            _bracketed_words = (re.findall("\((.*?)\)", _new_name))
            _material_version = 0
            if len(_bracketed_words) > 0:
                _last_entry = _bracketed_words[-1]
                if _last_entry.isdigit():
                    _material_version = int(_last_entry)
                if _material_version > 0:
                    _new_name = _new_name[:-len(_last_entry)-3]
            _new_name = "%s (%s)" % (_new_name, _material_version+1)
        return _new_name


def material_db_reader():
    header = ["Material", "Density", "Specific Heat", "Conductivity",
              "Melting Point", "Emissivity", "Reflectivity"]

    data = []
    material_file = "./data/materials.json"
    with open(material_file, 'r') as _jsfile:
        _database = json.load(_jsfile)

    for _name_key, _value in _database:
        material_name = _name_key
        for _value_key in _value:

