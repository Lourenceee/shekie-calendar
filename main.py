from tkinter import *
from menus.menu import *
from menus.popupmenu import *
from functions.buttons import *
from functions.keybind import *
from widgets.canvas import *
from functions.mousebind import *

mainWindow = Tk()
mainWindow.geometry("400x500")
mainWindow.title("Shekiee")
icon = PhotoImage(file = 'images\logo.png')
openImg = PhotoImage(file = 'images\menu-img\openfile.png')
saveImg = PhotoImage(file = 'images\menu-img\savefile.png')
exitImg = PhotoImage(file = 'images\menu-img\exit.png')
mainWindow.iconphoto(True, icon)
mainWindow.config(background = "#C6A4A2")
header = PhotoImage(file = 'images\header.png')
mainWindow.bind("<Motion>", mouseCor)

menu = Menu(mainWindow)
mainWindow.config(menu = menu)

# mainWindow.bind('<Button - 3>', menuPop)

fileMenu = Menu(menu, tearoff = False, font = ('Racing Sans One', 10))
menu.add_cascade(label = 'File', menu = fileMenu, font = ('Racing Sans One', 10))
widgetsMenu = Menu(menu, tearoff = False, font = ('Racing Sans One', 10))
menu.add_cascade(label = 'Widgets', menu = widgetsMenu, font = ('Racing Sans One', 10))

fileMenu.add_cascade(label = 'Open', command = openFile, image = openImg, font = ('Racing Sans One', 10), compound = 'left')
fileMenu.add_cascade(label = 'Save', command = saveFile, image = saveImg, font = ('Racing Sans One', 10), compound = 'left')
fileMenu.add_separator()
fileMenu.add_cascade(label = 'Exit', command = exitFile, image = exitImg, font = ('Racing Sans One', 10), compound = 'left')

widgetsMenu.add_cascade(label = 'Canvas', command = showCanvas, image = exitImg, font = ('Racing Sans One', 10), compound = 'left')

headerlabel = Label(mainWindow, image = header).pack()

date2019 = PhotoImage(file = 'images//buttons-img//date2019.png')
date2020 = PhotoImage(file = 'images//buttons-img//date2020.png')
date2021 = PhotoImage(file = 'images//buttons-img//date2021.png')

showCalbutton2019 = Button(mainWindow, text = 'Show 2019 Calendar',background = '#DB4838', image = date2019, command = showCal2019).place(x=40, y=65)
headerlabel = Label(mainWindow, text = 'left ctrl + 9', font = ('Racing Sans One', 8,'italic'), background = '#C6A4A2').place(x=53, y=103)
mainWindow.bind('<Control_L><9>', kshowCal2019)
showCalbutton2020 = Button(mainWindow, text = 'Show 2020 Calendar',background = '#DB4838', image = date2020, command = showCal2020).place(x=158, y=65)
headerlabel = Label(mainWindow, text = 'left ctrl + 0', font = ('Racing Sans One', 8,'italic'), background = '#C6A4A2').place(x=171, y=103)
mainWindow.bind('<Control_L><0>', kshowCal2020)
showCalbutton2021 = Button(mainWindow, text = 'Show 2021 Calendar',background = '#DB4838', image = date2021, command = showCal2021).place(x=276, y=65)
headerlabel = Label(mainWindow, text = 'left ctrl + 1', font = ('Racing Sans One', 8,'italic'), background = '#C6A4A2').place(x=289, y=103)
mainWindow.bind('<Control_L><1>', kshowCal2021)

mainWindow.mainloop()