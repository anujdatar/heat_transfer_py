# coding=utf-8

import json


class ProcessSettings:
    """ define and retrieve process settings """

    def __init__(self):
        self.settings_file = "./data/settings_files/process_settings.json"
        self.laser_power = 0.
        self.laser_spot_size = 0.
        self.laser_velocity = 0.
        self.temperature_inf = 0.
        self.convection_coeff = 0.

        self.process_json = {}

        self.get_process_settings()

        self.box_title = []
        self.box_message = []

    def get_process_settings(self):
        with open(self.settings_file, 'r') as _jsfile:
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
        with open(self.settings_file, 'r') as _output_file:
            _existing_data = json.load(_output_file)
        _existing_data.update(self.process_json)
        with open(self.settings_file, 'w') as _output_file:
            json.dump(_existing_data, _output_file, indent=4)
