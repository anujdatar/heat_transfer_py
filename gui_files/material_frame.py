# coding=utf-8

""" Tkinter frame for material properties """

import tkinter as tk
from tkinter import ttk
from .material_class_file import MaterialProperties


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
        self.combo_material_name = None

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
        self.button_edit_material = None
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

        # ######### material selection / entry fields
        self.label_material_name = ttk.Label(self.frame_material_name,
                                             text='Select Material')
        self.label_material_name.grid(row=0, column=0, padx=10, pady=5, sticky='e')

        self.combo_material_name = ttk.Combobox(self.frame_material_name,
                                                postcommand=self.return_material_list,
                                                width=30)
        self.combo_material_name.bind("<<ComboboxSelected>>",
                                      self.new_material_selected)
        self.combo_material_name.grid(row=0, column=1, padx=5, pady=5)

        # define type of material frame
        if self.window_type == 'entry':
            # self.master.minsize(width=400, height=180)
            self.master.resizable(False, False)
            self.master.title("Add New / Edit Material")
            self.enter_material_frame()

    def enter_material_frame(self):
        self.button_add_material = ttk.Button(self.master,
                                              text='Add Material',
                                              command=self.add_material_to_db)
        self.button_add_material.grid(row=4, column=3, padx=5, pady=25, sticky='s')

        self.button_edit_material = ttk.Button(self.master,
                                               text='Edit Material',
                                               command=self.edit_material_in_db)
        self.button_edit_material.grid(row=4, column=4, padx=5, pady=25, sticky='s')

        self.button_close_window = ttk.Button(self.master,
                                              text='Close',
                                              command=self.master.destroy)
        self.button_close_window.grid(row=4, column=5, padx=5, pady=25, sticky='s')

    def return_material_list(self):
        """ retrieve list of materials from json file for the combobox """
        self.material.get_material_list()
        self.combo_material_name['values'] = self.material.material_list

    def new_material_selected(self, event=None):
        """ retrieve material properties from json file, when material
         is selected from the drop-down combobox menu and update the
         fields in the material properties frame """
        if event:
            self.material_name = self.combo_material_name.get()
            self.material.read_from_json(self.material_name)
            self.material_density.set(self.material.density)
            self.material_sp_heat.set(self.material.specific_heat)
            self.material_conductivity.set(self.material.conductivity)
            self.material_melt_point.set(self.material.melting_point)
            self.material_emissivity.set(self.material.emissivity)
            self.material_reflectivity.set(self.material.reflectivity)

    def add_material_to_db(self):
        """ retrieve material properties from the new material addition
         frame to save to the json database """
        self.get_mat_property_from_form()
        self.material.save_material()
        # self.field_material_name.set(self.material.material_name)
        self.master.destroy()

    def edit_material_in_db(self):
        """ edit existing material property values """
        self.get_mat_property_from_form()
        self.material.edit_existing_in_json()
        self.master.destroy()

    def get_mat_property_from_form(self):
        self.material.material_name = self.combo_material_name.get()
        self.material.density = self.material_density.get()
        self.material.specific_heat = self.material_sp_heat.get()
        self.material.conductivity = self.material_conductivity.get()
        self.material.melting_point = self.material_melt_point.get()
        self.material.emissivity = self.material_emissivity.get()
        self.material.reflectivity = self.material_reflectivity.get()
