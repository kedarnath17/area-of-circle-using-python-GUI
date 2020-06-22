from tkinter import *

def ar():
  txt1 = txt.get()
  b = 3.14*float(txt1)*float(txt1)
  c = 'cm²'
  g = 'For'+' '+txt1+'cm Area is '+str(b)+' '+c
  Label(text=g,fg='#1afe14',bg='#000000').pack()

root = Tk()
root.title = 'Area'

Label(text='Input the radius of the circle(in cm)').pack()

txt = StringVar()
mydata = Entry(textvariable = txt).pack()

btn = Button(text='Calculate',fg='#ff0000',command=ar).pack()

btn2 = Label(text='Programmed by KEDARNATH',fg='#000000').pack()

root.mainloop()