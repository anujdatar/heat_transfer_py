# coding=utf-8

import json

filename = "test.json"

with open(filename, 'r') as json_file:
    data = json.load(json_file)

entry_list = []
for key in data:
    entry_list.append(key)
entry_list.sort()

print(entry_list)

# %%%%%%%%%%%% new data for addition
new_entry = {"test 3": {"one": 1.1,
                        "two": 2.2}}
print(new_entry)
print(new_entry["test 3"]['one'])

# %%%%%%%%% saving new data to file
with open(filename, 'r') as output_file:
    existing_data = json.load(output_file)
    existing_data.update(new_entry)
with open(filename, 'w') as output_file:
    json.dump(existing_data, output_file, indent=4)


# edit an existing entry in the JSON file
with open(filename, 'r') as output_file:
    existing_data = json.load(output_file)
existing_data["test 3"]["one"] = 1
with open(filename, 'w') as output_file:
    json.dump(existing_data, output_file, indent=4)


# delete an existing entry in the JSON file
with open(filename, 'r') as output_file:
    existing_data = json.load(output_file)
existing_data["test 3"].pop("one", None)
with open(filename, 'w') as output_file:
    json.dump(existing_data, output_file, indent=4)

# orig_dict = {
#     "test 1": {
#         "one": 1,
#         "two": 2
#     },
#     "test 2": {
#         "one": "a",
#         "two": "b"
#     },
#     "test 3": {
#         "one": 1.1,
#         "two": 2.0
#     }
# }

# ######################################################################

# coding=utf-8

""" Tkinter frame for material properties """

import tkinter as tk
from tkinter import ttk
from material_class_file import MaterialProperties


class GenerateMaterialFrame(object):
    def __init__(self, window_type, master=None):
        self.master = master
        self.window_type = window_type

        self.material = MaterialProperties()

        # %%%%%%%%%%%%% define material property variables
        self.material_name = tk.StringVar()
        self.material_density = tk.DoubleVar()
        self.material_sp_heat = tk.DoubleVar()
        self.material_conductivity = tk.DoubleVar()
        self.material_melt_point = tk.DoubleVar()
        self.material_emissivity = tk.DoubleVar()
        self.material_reflectivity = tk.DoubleVar()

        # %%%%%%%%%%%%% pre-define the structure of the entry fields
        self.frame_material_name = None
        self.label_material_name = None
        self.field_material_name = None

        self.label_density = None
        self.label_density_units = None
        self.entry_density = None
        self.label_sp_heat = None
        self.label_sp_heat_units = None
        self.entry_sp_heat = None
        self.label_conductivity = None
        self.label_conductivity_units = None
        self.entry_conductivity = None
        self.label_melt_point = None
        self.label_melt_point_units = None
        self.entry_melt_point = None
        self.label_emissivity = None
        self.label_emissivity_units = None
        self.entry_emissivity = None
        self.label_reflectivity = None
        self.label_reflectivity_units = None
        self.entry_reflectivity = None

        self.button_add_material = None
        self.button_close_window = None

        self.material_add_window_open = False

        self.material_property_frame()

    def material_property_frame(self):
        # material property widgets
        self.frame_material_name = ttk.LabelFrame(self.master)
        self.frame_material_name.grid(row=0, column=0, columnspan=3,
                                      padx=5, pady=5, ipadx=2, ipady=2, sticky='w')

        # ################ Density
        self.label_density = ttk.Label(self.master, text='Density')
        self.label_density.grid(row=1, column=0, padx=10, pady=2, sticky='e')
        self.entry_density = ttk.Entry(self.master,
                                       textvariable=self.material_density,
                                       justify='center')
        self.entry_density.grid(row=1, column=1, pady=2)
        self.label_density_units = ttk.Label(self.master, text="(kg/m^3)")
        self.label_density_units.grid(row=1, column=2, pady=2, sticky='w')

        # ################## Specific Heat
        self.label_sp_heat = ttk.Label(self.master, text='Specific Heat',
                                       width=20, anchor='e')
        self.label_sp_heat.grid(row=1, column=3, padx=15, pady=2, sticky='e')
        self.entry_sp_heat = ttk.Entry(self.master,
                                       textvariable=self.material_sp_heat,
                                       justify='center')
        self.entry_sp_heat.grid(row=1, column=4, pady=2)
        self.label_sp_heat_units = ttk.Label(self.master, text="(J/Kg.K)")
        self.label_sp_heat_units.grid(row=1, column=5, pady=2, sticky='w')

        # ################ Thermal Conductivity
        self.label_conductivity = ttk.Label(self.master, text='Thermal Conductivity')
        self.label_conductivity.grid(row=2, column=0, padx=10, pady=2, sticky='e')
        self.entry_conductivity = ttk.Entry(self.master,
                                            textvariable=self.material_conductivity,
                                            justify='center')
        self.entry_conductivity.grid(row=2, column=1, pady=2)
        self.label_conductivity_units = ttk.Label(self.master, text="(W/m.K)")
        self.label_conductivity_units.grid(row=2, column=2, pady=2, sticky='w')

        # ################## Melting Point
        self.label_melt_point = ttk.Label(self.master, text='Melting Point',
                                          width=20, anchor='e')
        self.label_melt_point.grid(row=2, column=3, padx=15, pady=2, sticky='e')
        self.entry_melt_point = ttk.Entry(self.master,
                                          textvariable=self.material_melt_point,
                                          justify='center')
        self.entry_melt_point.grid(row=2, column=4, pady=2)
        self.label_melt_point_units = ttk.Label(self.master, text="(K)")
        self.label_melt_point_units.grid(row=2, column=5, pady=2, sticky='w')

        # ################ Emissivity
        self.label_emissivity = ttk.Label(self.master, text='Emissivity')
        self.label_emissivity.grid(row=3, column=0, padx=10, pady=2, sticky='e')
        self.entry_emissivity = ttk.Entry(self.master,
                                          textvariable=self.material_emissivity,
                                          justify='center')
        self.entry_emissivity.grid(row=3, column=1, pady=2)
        self.label_emissivity_units = ttk.Label(self.master, text="(0-1)")
        self.label_emissivity_units.grid(row=3, column=2, pady=2, sticky='w')

        # ################## reflectivity
        self.label_reflectivity = ttk.Label(self.master, text='Reflectivity',
                                            width=20, anchor='e')
        self.label_reflectivity.grid(row=3, column=3, padx=15, pady=2, sticky='e')
        self.entry_reflectivity = ttk.Entry(self.master,
                                            textvariable=self.material_reflectivity,
                                            justify='center')
        self.entry_reflectivity.grid(row=3, column=4, pady=2)
        self.label_reflectivity_units = ttk.Label(self.master, text="(0-1)")
        self.label_reflectivity_units.grid(row=3, column=5, pady=2, sticky='w')

        # define type of material frame
        if self.window_type == 'select':
            self.select_material_frame()
        elif self.window_type == 'entry':
            self.master.minsize(width=400, height=225)
            self.master.resizable(False, False)
            self.master.title("Add New / Edit Material")
            self.enter_material_frame()

    def select_material_frame(self):
        self.label_material_name = ttk.Label(self.frame_material_name,
                                             text='Select Material')
        self.label_material_name.grid(row=0, column=0, padx=10, pady=5, sticky='e')

        self.field_material_name = ttk.Combobox(self.frame_material_name,
                                                postcommand=self.return_material_list,
                                                width=30)
        self.field_material_name.bind("<<ComboboxSelected>>",
                                      self.new_material_selected)
        self.field_material_name.grid(row=0, column=1, padx=5, pady=5)

    def enter_material_frame(self):
        self.material_add_window_open = True
        self.label_material_name = ttk.Label(self.frame_material_name,
                                             text='Enter/Select Material Name')
        self.label_material_name.grid(row=0, column=0, padx=10, pady=5, sticky='e')

        self.field_material_name = ttk.Entry(self.frame_material_name,
                                             textvariable=self.material_name,
                                             width=30)
        self.field_material_name.grid(row=0, column=1, padx=5, pady=5)

        self.button_add_material = ttk.Button(self.master,
                                              text='Add Material',
                                              command=self.add_material_function)
        self.button_add_material.grid(row=4, column=4, padx=5, pady=5)

        self.button_close_window = ttk.Button(self.master,
                                              text='Close',
                                              command=self.master.destroy)
        self.button_close_window.grid(row=4, column=5, padx=5, pady=5)

    def return_material_list(self):
        """ retrieve list of materials from json file for the combobox """
        self.material.get_material_list()
        self.field_material_name['values'] = self.material.material_list

    def new_material_selected(self, event=None):
        """ retrieve material properties from json file, when material
         is selected from the drop-down combobox menu and update the
         fields in the material properties frame """
        if event:
            self.material_name = self.field_material_name.get()
            self.material.read_from_json(self.material_name)
            self.material_density.set(self.material.density)
            self.material_sp_heat.set(self.material.specific_heat)
            self.material_conductivity.set(self.material.conductivity)
            self.material_melt_point.set(self.material.melting_point)
            self.material_emissivity.set(self.material.emissivity)
            self.material_reflectivity.set(self.material.reflectivity)

    def add_material_function(self):
        """ retrieve material properties from the new material addition
         frame to save to the json database """
        self.material.material_name = self.material_name.get()
        self.material.density = self.material_density.get()
        self.material.specific_heat = self.material_sp_heat.get()
        self.material.conductivity = self.material_conductivity.get()
        self.material.melting_point = self.material_melt_point.get()
        self.material.emissivity = self.material_emissivity.get()
        self.material.reflectivity = self.material_reflectivity.get()

        self.material.save_material()


# #####################################################
# coding=utf-8

import re
import json


name_1 = 'Titanium'
name_2 = 'Titanium (1)'
name_3 = 'Aluminum Alloy (Al6061)'
name_4 = 'Aluminum Alloy (Al6061) (1)'
name_5 = 'Titanium (2)'

name_list = [name_1, name_2, name_3, name_4, name_5]


def name_test(name):
    bracket_words = (re.findall("\((.*?)\)", name))
    print(bracket_words)
    last_entry = []
    material_version = 0

    if len(bracket_words) > 0:
        last_entry = bracket_words[-1]
        print(last_entry)
        if last_entry.isdigit():
            material_version = int(last_entry)

    if not last_entry:
        print('new material')

    print(material_version)

    if material_version > 0:
        name = name[:-len(last_entry)-3]
    new_material_name = "%s (%s)" % (name, material_version+1)

    print(new_material_name)

    return new_material_name


new_name = 'Titanium'  # name_test(name_1)

while new_name in name_list:
    new_name = name_test(new_name)


new_data = {'Stainless Steel': {'Density': 500,
                                'Conductivity': 5}}

with open('test.json', 'r') as op_file:
    existing = json.load(op_file)
existing['Titanium']['Conductivity'] = 19
existing['Titanium'].pop('Density', None)
existing['Titanium']['sp ht'] = 500
# existing['Stainless Steel']['Density'] = 7500
existing.update(new_data)
existing['Stainless Steel']['sp heat'] = 7500
existing['copper'] = {}
existing['copper']['Density'] = 3000
existing['copper']['melt pt']= 800
with open('test.json', 'w') as op_file:
    json.dump(existing, op_file, indent=4)
