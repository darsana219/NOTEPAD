# how to create the notepad in python

import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from  tkinter import *
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("MS NOTEPAD")

main_menu = tk.Menu()

#importing icons
# file icon
new_icon = tk.PhotoImage(file ="icons/nnew.png")
open_icon = tk.PhotoImage(file ="icons/oopen.png")
save_icon = tk.PhotoImage(file ="icons/ssave.png")
save_as_icon = tk.PhotoImage(file ="icons/ssaveas.png")
exit_icon = tk.PhotoImage(file ="icons/eexit.png")

# adding file option
file = tk.Menu(main_menu,tearoff = False)

# edit icon
copy_icon = tk.PhotoImage(file ="icons/ccopy.png")
paste_icon = tk.PhotoImage(file = "icons/ppaste.png")
cut_item_icon = tk.PhotoImage(file ="icons/ccut.png")
clear_icon = tk.PhotoImage(file ="icons/cclear.png")
find_icon = tk.PhotoImage(file ="icons/ffind.png")

# adding edit option
edit = tk.Menu(main_menu,tearoff = False)

# adding viwe option
tool_bar_icon = tk.PhotoImage(file ="icons/ttool.png")
status_bar_icon = tk.PhotoImage(file ="icons/sstatus.png")

view = tk.Menu(main_menu,tearoff = False)

# adding colour theme options
blue_theme = tk.PhotoImage(file ="icons/bblue.png")
red_theme = tk.PhotoImage(file ="icons/rred.png")
green_theme = tk.PhotoImage(file ="icons/ggreen.png")
yellow_theme = tk.PhotoImage(file ="icons/yyellow.png")
dark_theme = tk.PhotoImage(file ="icons/ddark.png")

color_theme = tk.Menu(main_menu,tearoff = False)

main_menu.add_cascade(label = "FILE",menu = file)
main_menu.add_cascade(label = "EDIT",menu = edit)
main_menu.add_cascade(label = "VIEW",menu = view)
main_menu.add_cascade(label ="COLOR THEME",menu = color_theme)

# Additonal features set in tool bar
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP,fill = tk.X)

#font family
font_tuple = tk.font.families()
font_family =tk.StringVar # change text according to font families
font_box = ttk.Combobox(tool_bar_label,width = 30,textvariable = font_family,state = "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row = 0,column = 0,padx = 5,pady = 5)

# size of text
size_variable = tk.IntVar # change the size of string accordingly
font_size = ttk.Combobox(tool_bar_label,width = 20,textvariable = size_variable,state = "readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row =0,column =1,padx = 5,pady = 5)

# buttons
# bold button


color_icons =(blue_theme,red_theme,green_theme,yellow_theme,dark_theme)

# color added to each theme icon with foreground and background color
color_dict = {
    'Blue Theme' : ('#000000',"#54E3D6"),
    'Red Theme' : ('#000000',"#cc0000"),
    'Green Theme' : ('#000000',"#66ff00"),
    'Yellow Theme' : ('#000000',"#ffe135"),
    'Dark Theme' : ('#ffffff',"#000000")
}

# addding every sub option of color_theme
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i,image = color_icons[count],compound = tk.LEFT)
    count +=1

# adding every sub option of view
view.add_checkbutton(label = "Tool Bar",onvalue = True,offvalue = False,image = tool_bar_icon,compound = tk.LEFT)
view.add_checkbutton(label = "Status Bar",onvalue = True,offvalue = False,image = status_bar_icon ,compound = tk.LEFT)

# adding every sub option of edit
edit.add_command(label = "Copy",image = copy_icon,compound = tk.LEFT,accelerator = "Ctrl+C")
edit.add_command(label = "Paste",image =paste_icon,compound = tk.LEFT,accelerator = "Ctrl+o")
edit.add_command(label = "Cut",image = cut_item_icon,compound = tk.LEFT,accelerator = "Ctrl+x")
edit.add_command(label = "Clear",image = clear_icon,compound = tk.LEFT,accelerator = "Ctrl+Alt+x")
edit.add_command(label ="Find",image =find_icon,compound =tk.LEFT,accelerator = "Ctrl+")

#adding every sub option of file
file.add_command(label = "New",image = new_icon,compound = tk.LEFT,accelerator = "Ctrl+N")
file.add_command(label = "Open",image = open_icon,compound = tk.LEFT,accelerator = "Ctrl+O")
file.add_command(label = "Save",image = save_icon,compound = tk.LEFT,accelerator = "Ctrl+s")
file.add_command(label = "Save as",image = save_as_icon,compound = tk.LEFT,accelerator = "Ctrl+Alt+s")
file.add_command(label = "Exit",image = exit_icon,compound = tk.LEFT,accelerator = "Ctrl+")

# display all options including sub
main_application.config(menu = main_menu)

# loop to hold the page
main_application.mainloop()

