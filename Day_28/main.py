from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    Time.config(text='Time')
    check.config(text='')
    

 
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    SHORT_BREAK_sec = SHORT_BREAK_MIN*60
    LONG_BREAK_sec = LONG_BREAK_MIN*60

    if reps == 8:
        Time.config(text='Break',fg=RED)
        count_down(LONG_BREAK_sec)
    elif reps % 2 == 1:
        Time.config(text='Work',fg=PINK)
        count_down(work_sec)
    else:
        Time.config(text='SBreak',fg=GREEN)
        count_down(SHORT_BREAK_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    

    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min <10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count>0:
        global timer 
        timer = window.after(1000,count_down,count-1)
        
    else:
        start_timer()
        mark=''
        for _ in range(math.floor(reps/2)):
            print(_)
            mark += '✔'
        print(mark)
        check.config(text=mark)
    
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)


Time = Label(text="Time",font=(FONT_NAME,35,'bold'),fg=GREEN,bg=YELLOW)
Time.grid(column=1,row=0)

Start = Button(text='Start',font=(FONT_NAME,10,'bold'),command=start_timer)
Start.grid(column=0,row=2)

reset = Button(text='reset',font=(FONT_NAME,10,'bold'),command=reset_time)
reset.grid(column=2,row=2)

check = Label(fg=GREEN,bg=YELLOW)
check.grid(column=1,row=3)

canvas = Canvas(width=200,height=224 ,bg=YELLOW,highlightthickness=0)
tomoto_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomoto_img)
timer_text = canvas.create_text(100,130,text="00:00",fill ="white",font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

window.mainloop()