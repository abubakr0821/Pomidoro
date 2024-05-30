import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
reps = 0
timer = None


# ---------------------------- Functions -------------------------------
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps, timer = 0, None
    canvas.itemconfig(tagOrId=timer_text, text='00:00')
    timer_label.config(text='Timer')
    checkmark_label.config(text='')



def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60



    if reps % 2 > 0:
        count_down(work_sec)
        timer_label['text'] = 'Work'
        timer_label.config(fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label['text'] = 'Short Break'
        timer_label.config(fg=PINK)
    else:
        return


window = tkinter.Tk()
window.title(string='Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text='Timer', font=(FONT_NAME, 36, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmark_label = tkinter.Label(font=(FONT_NAME, 8, 'bold'), bg=YELLOW, fg=GREEN)

checkmark_label.grid(column=1, row=3)


start_button = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = '0{}'.format(count_min)
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(tagOrId=timer_text, text='{minutes}:{seconds}'.format(minutes=count_min, seconds=count_sec))
    if count == 0:
        if reps % 2 > 0:
            checkmark_label['text'] += '✔'
        start_timer()
        return

    global timer
    timer = window.after(1000, count_down, count - 1)




window.mainloop()