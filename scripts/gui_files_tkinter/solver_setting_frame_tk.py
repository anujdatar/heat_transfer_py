# coding=utf-8

import tkinter as tk
from tkinter import ttk
from scripts.import_settings import SolverSettings


class GenerateSolverFrame(object):

    def __init__(self, master=None):
        self.master = master

        self.solver = SolverSettings()

        # define variables
        self.convergence_criterion = tk.DoubleVar()
        self.maximum_iterations = tk.DoubleVar()
        self.relaxation_parameter = tk.DoubleVar()

        self.solver_name = tk.StringVar()

        # define solver frame objects
        self.frame_solver_select = None
        self.label_solver_select = None
        self.combo_solver_select = None
        self.label_conv_crit = None
        self.entry_conv_crit = None
        self.label_max_iterations = None
        self.entry_max_iterations = None
        self.label_relax_param = None
        self.entry_relax_param = None

        self.generate_settings_frame()

    def generate_settings_frame(self):
        # solver selection frame
        self.frame_solver_select = ttk.LabelFrame(self.master)
        self.frame_solver_select.grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, ipadx=2, ipady=2,
            sticky='w')
        self.label_solver_select = ttk.Label(
            self.frame_solver_select, text='Select Solver')
        self.label_solver_select.grid(
            row=0, column=0, padx=10, pady=5, sticky='e')
        self.combo_solver_select = ttk.Combobox(
            self.frame_solver_select, postcommand=self.return_solver_list)
        self.combo_solver_select.bind(
            "<<ComboboxSelected>>", self.new_solver_selected)
        self.combo_solver_select.grid(row=0, column=1, padx=5, pady=5)

        # convergence criterion
        self.label_conv_crit = ttk.Label(
            self.master, text='Convergence Criterion')
        self.label_conv_crit.grid(row=1, column=0, padx=10, pady=2, sticky='e')
        self.entry_conv_crit = ttk.Entry(
            self.master, textvariable=self.convergence_criterion,
            justify='center')
        self.entry_conv_crit.grid(row=1, column=1, pady=2)

        # maximum iterations
        self.label_max_iterations = ttk.Label(
            self.master, text='Max # of Iterations')
        self.label_max_iterations.grid(
            row=2, column=0, padx=10, pady=2, sticky='e')
        self.entry_max_iterations = ttk.Entry(
            self.master, textvariable=self.maximum_iterations, justify='center')
        self.entry_max_iterations.grid(row=2, column=1, pady=2)

        # relaxation parameter
        self.label_relax_param = ttk.Label(
            self.master, text='Relaxation Parameter')
        self.label_relax_param.grid(
            row=3, column=0, padx=10, pady=2, sticky='e')
        self.entry_relax_param = ttk.Entry(
            self.master, textvariable=self.relaxation_parameter,
            justify='center')
        self.entry_relax_param.grid(row=3, column=1, pady=2)

    def return_solver_list(self):
        self.solver.get_solver_list()
        self.combo_solver_select['values'] = self.solver.solver_list

    def new_solver_selected(self, event=None):
        if event:
            self.solver_name = self.combo_solver_select.get()
            self.solver.get_solver_settings(self.solver_name)
            self.convergence_criterion.set(self.solver.convergence_criterion)
            self.maximum_iterations.set(self.solver.maximum_iterations)
            self.relaxation_parameter.set(self.solver.relaxation_parameter)
