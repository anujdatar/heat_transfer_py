# coding=utf-8

import tkinter as tk

def option_select(event=None):
    if event:
        print(menu_var.get())

def do_one():
    print("one")

def do_two():
    print('two')

a = tk.Tk()

frame_main = tk.LabelFrame(a, text='Menu Trial')
frame_main.pack(padx=20, pady=20)
# a.minsize(width=640, height=480)

canvas = tk.Canvas(frame_main, width=400, height=288)
canvas.pack()

option_list = ['one', 'two', 'three']
menu_var = tk.StringVar()
menu_var.set(option_list[0])
option_menu = tk.OptionMenu(frame_main, menu_var, *option_list, command=option_select)
option_menu.pack()

menubar = tk.Menu(a)

menubar.add_command(label='one', command=do_one)
menubar.add_command(label='two', command=do_two)

drop_one = tk.Menu(menubar, tearoff=0)
drop_one.add_command(label='one', command=do_one)
drop_one.add_separator()
drop_one.add_command(label='two', command=do_two)
drop_one.add_command(label='Exit', command=a.destroy)
menubar.add_cascade(label='three', menu=drop_one)

mb1 = tk.Menubutton(frame_main, text='trial1', relief='raised')
mb1.pack()
mb1.menu = tk.Menu(mb1, tearoff=0)
mb1['menu'] = mb1.menu

mb1.menu.add_command(label='one', command=do_one)
mb1.menu.add_command(label='two', command=do_two)

a.config(menu=menubar)

a.mainloop()
