import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Title")
    reps=0
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    work_sec = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN*60
    if reps %8==0:
        reps=0
        title.config(text="Long Break", fg=RED)
        count_down(long_break)
    elif reps%2==0 :
        title.config(text="Short Break", fg=PINK)
        count_down(short_break)
    else:
        title.config(text="Work",fg=GREEN)
        count_down(work_sec)
    if(reps%2==0):
        checkmark = "✓" * (reps// 2)
        check.config(text=checkmark, fg=GREEN)
    print(reps)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count % 60
    canvas.itemconfig(timer_text,text=f"{count_min :02d}:{count_sec :02d}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_count()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# Title Label
title = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
title.grid(row=1,column=2)

# Totmato Timer
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.grid(row=2,column=2)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))


# Start button
start = Button(text="start",highlightthickness=0,command=start_count)
start.grid(row=3,column=1)

#Checkmark
check = Label(text="",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
check.grid(row=3,column=2)

#Reset button
reset = Button(text="reset",highlightthickness=0,command=reset)
reset.grid(row=3,column=3)

window.mainloop()