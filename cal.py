from tkinter import *
from math import *
import statistics
import random
import datetime
from tkinter import  messagebox


W = Tk()
W.title('Phy-Cal version 1.0')
W.iconbitmap('c:/PP/b.ico')
W.geometry("1250x700")
W.resizable(0, 0)

menu = Menu(W)
W.config(menu=menu)

File = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=File)
File.add_command(label="New")
File.add_command(label="Open")
File.add_command(label="Save")
File.add_command(label="Save as...")
File.add_separator()
File.add_command(label="print  Ctrl+P")
File.add_separator()
File.add_command(label="Close", command=W.quit)


Edit = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=Edit)

Tool = Menu(menu, tearoff=0)
menu.add_cascade(label="Tool", menu=Tool)

Help = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=Help)
Help.add_command(label="View Help")
Help.add_separator()
Help.add_command(label="About Phy-Cal")
Help.add_command(label="SB")



lf = Frame(W, width=400 , height=900 , bg="WHITE" ).place(x=2 , y=1)

L1 = Label(lf, text="Select Form the following", font="Times 20 bold" , bg="WHITE", fg="Black")
L1.place(x=30 , y=10)

# v = Scrollbar(lf)
# tf = Frame(lf, width = 15, height = 15, wrap = NONE, yscrollcommand = v.set)


# v.pack(side = RIGHT, fill = Y) 
# v.config(command=lf.yview) 
# # Scrollbar
# scrol = Scrollbar(lf, orient=VERTICAL)




# Function to calculate the speed=distance/time 
lspeed = Label(lf,text="Calculate Speed", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=80 , y=47)

# del keywords
 

l = IntVar()
t = IntVar()
# a = StringVar()

def sd(): 
	global a
	length= l.get()
	time = t.get()
	answer = length/time
	a = Label(lf, text=answer, font="Times 13 bold", bg="Black", fg="WHITE" )
	a.place(x = 100 , y = 160)
    
def clear():
	l.set('')
	t.set('')
	a.configure(text="")
	# a.delete(0,'END')
	# a.destroy()
	# a.set('')



    
ll = Entry(lf, width=30, textvariable=l , border=5).place(x=150 , y=90)
le = Label(lf, text="Enter Length :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=10 , y = 88 )

tt = Entry(lf, width=30, textvariable=t , border=5).place(x=150 , y=130)
ti = Label(lf, text="Enter Time :" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=10 , y = 128 )

ans = Label(lf, text="Speed = " , font="Times 16 bold", bg="WHITE", fg="Black" ).place(x = 10 , y = 160)

spd = Button(lf,text="Calculate Speed",width=20, command=sd , bg="Black", fg="WHITE" , border = 4 ).place(x=30 , y = 190 )
cl = Button(lf,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=200 , y = 190 )



# Function to calculate the Velocity= displacement/timetaken using string variable and EXCEPTION

velocity = Label(lf,text="Calculate Velocity ", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=80 , y=230)

ve = IntVar()
dis = IntVar()
vel = IntVar()

def velocity():
	global vel
	velo = ve.get()/dis.get()
	vel = Label(lf, text=velo, font="Times 13 bold", bg="Black", fg="WHITE" )
	vel.place(x = 110 , y = 345)

    
def clear():
	dis.set('')
	ve.set('')
	vel.destroy()



ll = Entry(lf, width=30, textvariable=ve, border=5).place(x=150 , y=270)
le = Label(lf, text="Displacement :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=10 , y = 270 )

tt = Entry(lf, width=30, textvariable=dis , border=5).place(x=150 , y=310)
ti = Label(lf, text="Time Taken :" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=10 , y = 310 )

vel = Label(lf, text="Velocity = " , font="Times 16 bold", bg="WHITE", fg="Black" ).place(x = 10 , y = 345)

calvel = Button(lf,text="Calculate Velocity",width=20, command=velocity , bg="Black", fg="WHITE" , border = 4 ).place(x=30 , y = 380 )
clear = Button(lf,text="Clear Text",width=20, command= clear, bg="Black", fg="WHITE" , border = 4 ).place(x=200 , y = 380 )


# Calculating Averaage 

averagevelocity = Label(lf,text="Average Velocity ", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=80 , y=415)

td = IntVar()
tt = IntVar()

def averagevelocity():
	global av
	avg = td.get()/tt.get()
	av = Label(lf, text=avg, font="Times 13 bold", bg="Black", fg="WHITE" )
	av.place(x = 185 , y = 523)

def clear():
	td.set('')
	tt.set('')
	av.destroy()
    


ll = Entry(lf, width=30, textvariable= td, border=5).place(x=150 , y=450)
le = Label(lf, text="Total Displace:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=10 , y = 450 )

ll = Entry(lf, width=30, textvariable= tt, border=5).place(x=150 , y=490)
le = Label(lf, text="Total Time :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=10 , y = 490)

av = Label(lf, text="Average Velocity= " , font="Times 16 bold", bg="WHITE", fg="Black" ).place(x = 10 , y = 520)

avgvel = Button(lf,text="Calculate Velocity",width=20, command=averagevelocity, bg="Black", fg="WHITE" , border = 4 ).place(x=30 , y = 560)
clear = Button(lf,text="Clear Text",width=20, command= clear, bg="Black", fg="WHITE" , border = 4 ).place(x=200 , y = 560)

#  Middle Frame 

md = Frame(W, width=400 , height=900 , bg="WHITE" ).place(x=410 , y=1)

# Calculating force 

at = IntVar()
mm = IntVar()



def force():
	global aa
	forc = mm.get()*at.get()
	aa = Label(md, text=forc, font="Times 13 bold", bg="Black", fg="WHITE" )
	aa.place(x = 490 , y = 80)
    # except Exception: messagebox.showinfo("Phy-Cal","Enter number")

def clear():
	at.set('')
	mm.set('')
	aa.destroy()
	     

calculateforce = Label(md,text="Calculate Force", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=500 , y=10)
    
mee = Entry(md, width=15, textvariable= at , border=5).place(x=470 , y=50)
mass = Label(md, text="Mass:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=415 , y = 50 )

ac = Entry(md, width=15, textvariable= mm , border=5).place(x=700, y=50)
acc = Label(md, text="Acceleration:" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=580 , y = 50 )

foorce = Label(md, text="Force = " , font="Times 16 bold", bg="WHITE", fg="Black" ).place(x =415 , y = 80)

btn = Button(md,text="Calculate force",width=20, command=force, bg="Black", fg="WHITE" , border = 4 ).place(x=435 , y = 115 )
clean = Button(md,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=600 , y = 115 )


# Calculate Pressure

pressure = Label(md,text="Calculate Pressure", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=500 , y=155)



ar = IntVar()
fy = IntVar()
 
def pressure():
	global ans
	pr = fy.get()/ar.get()
	ans = Label(md, text=pr, font="Times 13 bold", bg="Black", fg="WHITE" )
	ans.place(x = 515 , y = 220)  


def clear():
    ar.set('') 
    fy.set('')
    ans.destroy()


fd = Entry(md, width=15, textvariable= fy , border=5).place(x=485, y=190)
frc = Label(md, text="Force :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=415 , y = 190 )

aaaa = Entry(md, width=15, textvariable= ar , border=5).place(x=680, y=190)
area = Label(md, text="Area :" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=610 , y = 190 )

aea = Label(md, text="Pressure = " ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=415 , y = 220 )


btn_pressure = Button(md,text="Calculate Pressure",width=20, command=pressure, bg="Black", fg="WHITE" , border = 4 ).place(x=435 , y = 255 )
clean = Button(md,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=600 , y = 255 )


# Moment of a Force
l2 = Label(md,text="Calculate Moment of a Force", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=470 , y=295)


# pd = IntVar()
# fo = IntVar()

pd = DoubleVar()
fo = DoubleVar()

def momentforce():
    try:
	    global att 
	    mf = pd.get()*fo.get()
	    att = Label(md, text=mf, font="Times 13 bold", bg="Black", fg="WHITE" )
	    att.place(x = 645 , y = 362)
    except Exception: messagebox.showinfo("Phy-Cal","Enter number")

def clear():
	pd.set('')
	fo.set('')
	att.destroy()

perdis = Entry(md, width=15, textvariable= pd, border=5).place(x=650, y=330)
per = Label(md,text="Perpendicular Distance :", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=420 , y=330)
 
f = Entry(md, width=15, textvariable= fo , border=5).place(x=485, y=363)
lf = Label(md, text="Force :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=415 , y = 360 )

btn = Button(md,text="Calculate force",width=20, command=momentforce, bg="Black", fg="WHITE" , border = 4 ).place(x=435 , y = 400 )
clean = Button(md,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=600 , y = 400 )

mmm = Label(md, text="MoF =", font="Times 13 bold", bg="WHITE", fg="Black" ).place(x = 590 , y = 365)


# Recoil velocity v2= -(m1/m2)v1.
R = Label(md,text="Recoil Velocity", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=550 , y=435)

mb = DoubleVar()
mr = DoubleVar()
vb = DoubleVar()
vr = DoubleVar()
ecoil = StringVar()

def rv():
    try:
    	vr = (mb.get()/mr.get())*vb.get()
    	eciol = Label(md, text=vr, font="Times 13 bold", bg="Black", fg="WHITE" )
    	ecoil.place(x=690,y=510)
    except Exception: messagebox.showinfo("Phy-Cal","Enter number")

def clear():
	mb.set('')
	mr.set('')
	vb.set('') 
	ecoil.set("")
  

v1 = Entry(md, width=15, textvariable= mb, border=5).place(x=510, y=470)
L1 = Label(md, text="MoBullet:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=415 , y = 470 )

v1 = Entry(md, width=15, textvariable= mr, border=5).place(x=697, y=470)
L2 = Label(md, text="MoRifle:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=613 , y = 470 )

v1 = Entry(md, width=15, textvariable= vb, border=5).place(x=509, y=510)
L3 = Label(md, text="VoBullet:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=415 , y = 510)

L4= Label(md, text="Recoil :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=610 , y = 510)



btn = Button(md,text="Calculate force",width=20, command=rv, bg="Black", fg="WHITE" , border = 4 ).place(x=435 , y = 550 )
clean = Button(md,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=600 , y = 550 )




# Right Frame

rf = Frame(W, width=400 , height=900 , bg="WHITE" ).place(x=819 , y=1)

#muzzle vlocity v.exp()=2ad    ::(a= acceleration , d= distance)

Muz = Label(rf,text="Muzzle Velocity", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=950 , y=10)


acl = DoubleVar()
dis = DoubleVar()

def mv():
    try:
    	global mz
    	mvel = 2*acl.get()*dis.get()
    	mz = Label(rf,text=mvel, font="Times 16 bold" , bg="Black", fg="WHITE" )
    	mz.place(x=1010 , y=80)
    except Exception: messagebox.showinfo("Phy-Cal","Enter number") 

def clear():
	acl.set('')
	dis.set('')
	# mz.configure(text="")
	mz.destroy()



mee = Entry(rf, width=15, textvariable= acl , border=5).place(x=895 , y=50)
mass = Label(rf, text="Acc:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y = 50 )

ac = Entry(rf, width=15, textvariable= dis , border=5).place(x=1100, y=50)
acc = Label(rf, text="Distacne:" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=1010 , y = 50 )

mass = Label(rf, text="Muzzule velocity:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y = 80 )


btn = Button(rf,text="Calculate force",width=20, command=mv, bg="Black", fg="WHITE" , border = 4 ).place(x=850 , y = 112 )
clean = Button(rf,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=1020 , y = 112 )




#kinetics energy of bullets  same fromulat as kinetic energy.
keob = Label(rf,text="Kinetic energy of a bullet", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=900 , y=150)

ma = DoubleVar()
vol = DoubleVar()

def ke():
	try:
		global gy
		eng = 1/2*ma.get()*vol.get()**2
		gy = Label(rf,text=eng, font="Times 16 bold" , bg="Black", fg="WHITE" )
		gy.place(x=980 , y=210)
	except Exception: messagebox.showinfo("Phy-Cal","Enter number") 

def clear():
	ma.set('')
	vol.set('')
	gy.destroy()


mee = Entry(rf, width=15, textvariable= ma , border=5).place(x=905 , y=180)
mass = Label(rf, text="Mass :" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y = 180 )

ac = Entry(rf, width=15, textvariable= vol , border=5).place(x=1100, y=180)
acc = Label(rf, text="Velocity:" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=1005 , y = 180 )

mass = Label(rf, text="Energy =" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y = 210 )


btn = Button(rf,text="Calculate force",width=20, command=ke, bg="Black", fg="WHITE" , border = 4 ).place(x=850 , y = 252 )
clean = Button(rf,text="Clear Text",width=20, command=clear , bg="Black", fg="WHITE" , border = 4 ).place(x=1020 , y = 252 )



#presure inside the barrel

keob = Label(rf,text="Pressure in A barrel", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=900 , y=295)

pm = DoubleVar()
pv = DoubleVar()
ba = DoubleVar()
lb = DoubleVar()

def pb():
	try:
		global psi
		prs = pm.get()*pv.get()**2/8*ba.get()*lb.get()
		psi = Label(rf, text= prs, font= "Times 16 bold", bg="WHITE", fg="Black")
		psi.place(x=1050 , y =465)
	except Exception: messagebox.showinfo("Phy-Cal","Enter Number")

def cln():
	pm.set('')
	pv.set('')
	ba.set('')
	lb.set('')
	psi.destroy()




prjtmas = Entry(rf, width=15, textvariable= pm , border=5).place(x=1020 , y=325)
mas = Label(rf, text="Projectile Mass:" , font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y=325 )

prhtveloc = Entry(rf, width=15, textvariable= pv , border=5).place(x=1020, y=360)
pvv = Label(rf, text="Projectile Velocity:" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y=360 )


borear = Entry(rf, width=15, textvariable= ba , border=5).place(x=1020, y=395)
brr = Label(rf, text="Bore Area:" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y=395 )

lenbrl = Entry(rf, width=15, textvariable= lb , border=5).place(x=1020, y=430)
lbbb = Label(rf, text="Lenght of Barrel:" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y=430 )

lbbb = Label(rf, text="Pressure in Barrel =" ,font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=840 , y=465 )


btn = Button(rf,text="Calculate force",width=20, command=pb, bg="Black", fg="WHITE" , border = 4 ).place(x=850 , y = 500 ) 
clean = Button(rf,text="Clear Text",width=20, command=cln , bg="Black", fg="WHITE" , border = 4 ).place(x=1020 , y = 500 )

#projectile friction

#compresson of the spring

# keob = Label(rf,text="Compression of a Spring", font="Times 16 bold" , bg="WHITE", fg="Black" ).place(x=900 , y=540)

W.mainloop()

