from cgitb import reset
from tkinter import *
from tkinter.tix import COLUMN
from turtle import color
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="TIMER",fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.config(bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start")
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

checkmark_button = Button(text= "✔", fg=GREEN)
checkmark_button.grid(column=1, row=3)
window.mainloop()