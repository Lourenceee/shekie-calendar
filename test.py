# from tqdm.auto import tqdm
# for i in tqdm(range(100001)):
#     print(" ", end = '\r')

# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks()

# window = Tk()

# percent = StringVar()
# text = StringVar()

# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()

# start()

# window.mainloop()

from tkinter import *

def showCanvas(): 
    window = Tk()
    canvas = Canvas(window,height=500,width=500)
    #canvas.create_line(0,0,500,500,fill="blue",width=5)
    #canvas.create_line(0,500,500,0,fill="red",width=5)
    #canvas.create_rectangle(50,50,250,250,fill="purple")
    #points = [250,0,500,500,0,500]
    #canvas.create_polygon(points,fill="yellow",outline="black",width=5)
    #canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
    canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
    canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
    canvas.create_oval(190,190,310,310,fill="white",width=10)
    canvas.pack()

    window.mainloop()

showCanvas()