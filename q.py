from Tkinter import *

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def getDate(event=None):
	text.insert(INSERT,E1.get()+'\n')
	text.grid(row=2,column=1,sticky=W)

top = Tk()
top.title("Centered!")

# top.wait_visibility(top)
E1 = Entry(top, bd =5)
text = Text(top,height=2,width=20,xscrollcommand=1)

E1.grid(row=1,column=1)

top.bind('<Return>', getDate)
top.wm_attributes('-alpha',0.8)
# center(top)

top.mainloop()