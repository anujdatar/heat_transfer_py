# coding=utf-8

""" Main App """

import tkinter as tk
from tkinter import ttk

from gui_files import GenerateMaterialFrame
from gui_files import GenerateProcessFrame
from gui_files import GenerateSolverFrame

# from material_class_file import MaterialProperties


class MainApp(object):
    def __init__(self, master=None):
        self.master = master

        master.minsize(width=680, height=480)
        master.resizable(True, True)
        master.title("Heat Transfer Simulation")

        self.new_material_window_open = False

        # define variables, and objects
        self.topbox_new_material = None
        self.new_material_window = None

        # frame definition
        self.frame_main = tk.Frame(self.master)
        self.frame_main.pack(fill='both', expand=True)

        # %%%%%%%%%%%%%%%%%%% material frame
        self.frame_material = ttk.LabelFrame(self.frame_main,
                                             text='Material Properties')
        self.frame_material.grid(row=0, column=0, columnspan=3,
                                 padx=5, pady=5, ipadx=2, ipady=2, sticky='w')
        self.material_frame = GenerateMaterialFrame('select', self.frame_material)

        # %%%%%%%%%%%%%%%%% process settings frame
        self.frame_process = ttk.LabelFrame(self.frame_main,
                                            text='Process Settings')
        self.frame_process.grid(row=1, column=0, columnspan=2,
                                padx=5, pady=5, ipadx=2, ipady=2, sticky='w')
        self.process_frame = GenerateProcessFrame(self.frame_process)

        # %%%%%%%%%%%%%% solver settings frame
        self.frame_solver = ttk.LabelFrame(self.frame_main,
                                           text='Solver Setting')
        self.frame_solver.grid(row=1, column=2,
                               padx=5, pady=5, ipadx=2, ipady=2, sticky='e')
        self.solver_frame = GenerateSolverFrame(self.frame_solver)

        # extra test buttons
        self.button_print_test = ttk.Button(self.frame_main,
                                            text='Test Print',
                                            command=self.test_print)
        self.button_print_test.grid(row=5, column=2, padx=5, pady=5, sticky='w')

        self.button_add_new_material = ttk.Button(self.frame_main,
                                                  text='Add/Edit Materials',
                                                  command=self.launch_new_material_window)
        self.button_add_new_material.grid(row=5, column=2, padx=5, pady=5)

        self.button_close_all = ttk.Button(self.frame_main,
                                           text='Quit',
                                           command=self.close_all)
        self.button_close_all.grid(row=5, column=2, padx=5, pady=5, sticky='e')

    def generate_menu(self):
        self.menubar = tk.Menu(self.master)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.close_all)

        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.edit_menu.add_command(label='Add/Edit Material', command=self.launch_new_material_window)

    def test_print(self):
        print(self.material_frame.material_name)

    def close_all(self):
        self.master.destroy()

    def launch_new_material_window(self):
        if self.new_material_window_open is True:
            self.topbox_new_material.destroy()
            self.new_material_window_open = False
        self.new_material_window_open = True

        self.topbox_new_material = tk.Toplevel(self.master)
        self.topbox_new_material.transient(self.master)
        self.new_material_window = GenerateMaterialFrame('entry', self.topbox_new_material)

        self.topbox_new_material.focus()
        self.new_material_window.combo_material_name.focus()


root = tk.Tk()
MainApp(root)
root.mainloop()
