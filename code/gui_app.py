from pylab import * 
from tkinter import * 
import matplotlib.pylab as pl
from numpy import * 
class Charge : 
    def __init__(self,x,y,mag):
        self.x = x
        self.y = y
        self.mag = mag

class charge: 
    def __init__(self,q,pos) : 
        self.q = q
        self.pos = pos

def E_point_charge(q,a,x,y):
    #formula to calculate electric field due to a single charge
    return q(x-a[0])/((x-a[0])**2+(y-a[1])**2)**(1.5),q*(y-a[1])/((x-a[0])**2+(y-a[1])**2)*(1.5)

def E_total(x,y,charges):
    Ex,Ey=0,0
    for C in charges:
        E = E_point_charge(C.q,C.pos,x,y)
        Ex=Ex+E[0]
        Ey = Ey+E[1]
    return [ Ex,Ey ]

w = Tk()

w.title('Field Lines')

mag = [];

plax = [];

play = []

charges = []

def Appender():

    x1 = (eval(xv.get()))
    x1 = float(x1)
    plax.append(float(x1))

    y1 = (eval(yv.get()))
    y1 = float(y1)
    play.append(float(y1))

    mag1 = (eval(magv.get()))
    mag1  = float(mag1)
    mag.append(float(mag1))
    c  = len(plax)
    pos = [];
    cx = float(plax[c-1]);
    pos.append(cx);
    cy = float(play[c-1])
    pos.append(cy);
    cm = float(mag[c-1]);
    charges.append(charge(cm,pos))


space = Label(w,text="Please enter the details of all the charges one by one and then press the Plot Button").pack()

Xentry = Label(w,text = 'X Co-ordinate = ').pack()
xv = StringVar()
xentry = Entry(w,textvariable = xv, font=("Sitka Text",10)).pack()
Yentry = Label(w,text="y Co-ordinate = ").pack()
yv = StringVar()
yentry = Entry(w,textvariable = yv, font=("Sitka Text",10)).pack()
MAGentry = Label(w,text="Magnitude of Charge = ").pack()
magv = StringVar()

magentry = Entry(w,textvariable=magv,font=("Sitka Text",10)).pack()

load = Button(w,text='Add Charge Details',command=Appender).pack(pady=10)

def Plotter():

    x0,x1 = -10,10
    y0,y1 = -10,10
    x = linspace(x0,x1,64)
    y = linspace(y0,y1,64)

    x,y = meshgrid(x,y)
    Ex,Ey=E_total(x,y,charges)
    streamplot(x,y,Ex,Ey,color='k')

    for C in charges : 
        if C.q > 0  : 
            plot(C.pos[0],C.pos[1],'bo',ms=8*sqrt(C.q))
        if C.q < 0 : 
            plot(C.pos[0],C.pos[1],'ro',ms=8*sqrt(-C.q))
        xlabel('$x$')
        ylabel('$y$')

        gca().set_xlim(x0,x1)
        gca().set_ylim(y0,y1)
        show()

ploted = Button(w,text='Plot The Field Lines',command=plotter).pack(pady=10)
w.mainloop()
