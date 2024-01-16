from tkinter import *

def entry_usd():
    mlie = int(entry.get())
    km = round(mlie*1.609)
    calculator_mile.config(text=km)
    


window = Tk()
window.minsize(width=250,height=200)
window.title('Calculator Mile to Km')
window.config(padx=20,pady=20)

entry = Entry(width=10)
entry.grid(column=1,row=0)

label_mlie = Label(text='Mlies')
label_mlie.grid(column=2,row=0)
label_mlie.config(padx=10)

label_equal = Label(text='is equal to')
label_equal.grid(column=0,row=1)

button = Button(text="calculator",command=entry_usd)
button.grid(column=1,row=2)

calculator_mile = Label(text='0')
calculator_mile.grid(column=1,row=1)

km_l = Label(text='km')
km_l.grid(column=2,row=1)



window.mainloop()