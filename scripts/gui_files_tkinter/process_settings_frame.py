# coding=utf-8

import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ProcessSettings:
    """ define and retrieve process settings """

    def __init__(self):
        self.process_settings_file = "./data/json_files/process_settings.json"
        self.laser_power = 0.
        self.laser_spot_size = 0.
        self.laser_velocity = 0.
        self.temperature_inf = 0.
        self.convection_coeff = 0.

        self.process_json = {}

        self.get_process_settings()

    def get_process_settings(self):
        with open(self.process_settings_file, 'r') as _jsfile:
            _data = json.load(_jsfile)
        self.laser_power = _data["LaserPower"]
        self.laser_spot_size = _data["LaserSpotSize"]
        self.laser_velocity = _data["LaserScanningVelocity"]
        self.temperature_inf = _data["AmbientTemperature"]
        self.convection_coeff = _data["ConvectiveCoefficient"]

    def format_settings_as_json(self):
        self.process_json = {
            "LaserPower": self.laser_power,
            "LaserSpotSize": self.laser_spot_size,
            "LaserScanningVelocity": self.laser_velocity,
            "AmbientTemperature": self.temperature_inf,
            "ConvectiveCoefficient": self.convection_coeff}

    def write_to_json(self):
        with open(self.process_settings_file, 'r') as _output_file:
            _existing_data = json.load(_output_file)
        _existing_data.update(self.process_json)
        with open(self.process_settings_file, 'w') as _output_file:
            json.dump(_existing_data, _output_file, indent=4)

    def edit_settings_db(self):
        _box_title = 'Edit Process Settings?'
        _box_message = 'Do you want to permanently change process settings in database?'
        if messagebox.askyesno(_box_title, _box_message, icon='warning'):
            self.format_settings_as_json()
            self.write_to_json()


class GenerateProcessFrame(object):
    def __init__(self, master=None):
        self.master = master

        self.process = ProcessSettings()

        # ##### define variables for use in entry fields
        self.laser_power = tk.DoubleVar()
        self.laser_spot_size = tk.DoubleVar()
        self.laser_velocity = tk.DoubleVar()
        self.temperature_inf = tk.DoubleVar()
        self.convection_coeff = tk.DoubleVar()

        # ######### define fields for tkinter structure
        self.label_laser_power = None
        self.entry_laser_power = None
        self.label_power_units = None
        self.label_spot_size = None
        self.entry_spot_size = None
        self.label_spot_units = None
        self.label_laser_vel = None
        self.entry_laser_vel = None
        self.label_velocity_units = None
        self.label_ambient_temp = None
        self.entry_ambient_temp = None
        self.label_temperature_units = None
        self.label_convect_coeff = None
        self.entry_convect_coeff = None
        self.label_convect_units = None

        self.generate_process_frame()
        self.set_process_setting_entries()

    def generate_process_frame(self):
        # ############# Laser Power
        self.label_laser_power = ttk.Label(self.master, text='Laser Power')
        self.label_laser_power.grid(row=0, column=0, padx=10, pady=2, sticky='e')
        self.entry_laser_power = ttk.Entry(self.master,
                                           textvariable=self.laser_power,
                                           justify='center')
        self.entry_laser_power.grid(row=0, column=1, pady=2)
        self.label_power_units = ttk.Label(self.master, text='Watts')
        self.label_power_units.grid(row=0, column=2, pady=2, sticky='w')

        # ############### Laser Spot Size
        self.label_spot_size = ttk.Label(self.master, text='Laser Spot Size')
        self.label_spot_size.grid(row=1, column=0, padx=10, pady=2, sticky='e')
        self.entry_spot_size = ttk.Entry(self.master,
                                         textvariable=self.laser_spot_size,
                                         justify='center')
        self.entry_spot_size.grid(row=1, column=1, pady=2)
        self.label_spot_units = ttk.Label(self.master, text='m^2')
        self.label_spot_units.grid(row=1, column=2, pady=2, sticky='w')

        # ############## Laser Scanning Velocity
        self.label_laser_vel = ttk.Label(self.master, text='Laser Scanning Velocity')
        self.label_laser_vel.grid(row=2, column=0, padx=10, pady=2, sticky='e')
        self.entry_laser_vel = ttk.Entry(self.master,
                                         textvariable=self.laser_velocity,
                                         justify='center')
        self.entry_laser_vel.grid(row=2, column=1, pady=2)
        self.label_velocity_units = ttk.Label(self.master, text='m/s')
        self.label_velocity_units.grid(row=2, column=2, pady=2, sticky='w')

        # ############## Ambient Temperature
        self.label_ambient_temp = ttk.Label(self.master, text='Ambient Temperature')
        self.label_ambient_temp.grid(row=3, column=0, padx=10, pady=2, sticky='e')
        self.entry_ambient_temp = ttk.Entry(self.master,
                                            textvariable=self.temperature_inf,
                                            justify='center')
        self.entry_ambient_temp.grid(row=3, column=1, pady=2)
        self.label_temperature_units = ttk.Label(self.master, text='K')
        self.label_temperature_units.grid(row=3, column=2, pady=2, sticky='w')

        # ########### Convective Heat Transfer Coefficient
        self.label_convect_coeff = ttk.Label(self.master, text='Convective HT Coeff')
        self.label_convect_coeff.grid(row=4, column=0, padx=10, pady=2, sticky='e')
        self.entry_convect_coeff = ttk.Entry(self.master,
                                             textvariable=self.convection_coeff,
                                             justify='center')
        self.entry_convect_coeff.grid(row=4, column=1, pady=2)
        self.label_convect_units = ttk.Label(self.master, text='W/(m^2.K)')
        self.label_convect_units.grid(row=4, column=2, pady=2, sticky='w')

    def set_process_setting_entries(self):
        self.laser_power.set(self.process.laser_power)
        self.laser_spot_size.set(self.process.laser_spot_size)
        self.laser_velocity.set(self.process.laser_velocity)
        self.temperature_inf.set(self.process.temperature_inf)
        self.convection_coeff.set(self.process.convection_coeff)