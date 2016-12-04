from Tkinter import *
import urllib2
import threading

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def search(q):
	full_url = "https://suggestqueries.google.com/complete/search?client=firefox&q=";
	data = urllib2.urlopen(full_url+q)
	return eval(data.read())[1]

def getDate(a=1,s=1,d=1):
	def url():
		if(E1.get() != ''):
			s = search(E1.get())
			text = Text(top,height=len(s),width=20)
			for x in s :
				text.insert(INSERT,x+'\n')
			text.grid(row=2,column=1,sticky=W)
			return
		else:
			text = Text(top,height=1,width=20)
			text.insert(INSERT,"")

			return
	t = threading.Thread(target=url)
	t.start()

top = Tk()
top.title("GoogleAtHelp!")
# center(top)

top.wait_visibility(top)
top.wm_attributes('-alpha',0.8)

E1 = Entry(top,bd =5)
text = Text(top,height=0,width=20)

E1.grid(row=1,column=1)

# ee.trace('w',getDate)
# top.bind('<Return>', getDate)
E1.bind('<Key>', getDate)
# E1.after(300,getDate);

top.mainloop()