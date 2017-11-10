# coding=utf-8

import json


class SolverSettings:

    def __init__(self):
        self.solver_settings_file = "./data/settings_files/solver_settings.json"
        self.convergence_criterion = 0.
        self.maximum_iterations = 0.
        self.relaxation_parameter = 0.
        self.solver_list = []
        self.solver_json = {}

        self.get_solver_list()

    def get_solver_list(self):
        with open(self.solver_settings_file, 'r') as _jsfile:
            _data = json.load(_jsfile)
        self.solver_list = []
        for _key in _data:
            self.solver_list.append(_key)
            self.solver_list.sort()

    def get_solver_settings(self, solver_name):
        with open(self.solver_settings_file, 'r') as _jsfile:
            _data = json.load(_jsfile)
        self.convergence_criterion = _data[solver_name]['convergence_criterion']
        self.maximum_iterations = _data[solver_name]['maximum_iterations']
        self.relaxation_parameter = _data[solver_name]['relaxation_param']
