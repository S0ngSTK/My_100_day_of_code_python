from tkinter import *

def button_on_click():
    User = input.get()
    my_label.config(text=User)
    
window = Tk()

window.title('My GUI Program')
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
my_label = Label(text='I am a Label',font=('Arial',24,'bold'))
# my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")



button = Button(text='click me',command=button_on_click)
button.grid(column=1,row=1)
# button.pack()

button2 = Button(text='Text')
button2.grid(column=2,row=0)

input = Entry(width=30)
input.insert(END,string="Text??")
print(input.get())
# input.pack()
input.grid(column=4,row=4)


window.mainloop()