from itertools import count
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer)
    label_1.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
    canva.itemconfig(timer_text, text = "00:00")
    label_2.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text = "Break", fg = RED, bg = YELLOW, font = (FONT_NAME, 40, "bold"))
    #:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_1.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))

    else:
        count_down(work_sec)
        label_1.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))

    # count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canva.itemconfig(timer_text, text = f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marker = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marker +="✔"

        label_2["text"] = marker
    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pamadora")
window.config(padx = 100, pady = 50, bg = YELLOW)


label_1 = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 40, "bold"))
label_1.grid(column = 1, row = 0)

canva = Canvas(width = 200, height=224, bg = YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file = "tomato.png")
canva.create_image(100, 113, image = tomato_img)
timer_text = canva.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME , 35, "bold"))
canva.grid(column = 1, row = 1)


button_start = Button(text = " Start", border=0.5, command = start_timer)
button_start.grid(column = 0, row = 2)

button_reset = Button(text = "Reset", border=0.5, command = reset_time)
button_reset.grid(column = 2, row = 2)
label_2 = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 15, "bold"))
label_2.grid(column = 1, row = 3)

window.mainloop()