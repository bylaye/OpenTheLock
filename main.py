import tkinter as tk
import time
from open_lock import OpenLock # type: ignore

TITLE = "Open THe Lock"
COLOR_BACKGROUND = 'white'
COLOR_ENTRY_OK = 'green'
COLOR_ENTRY_WARNING = 'red'
COLOR_WHEEL_CELL = 'yellow'
MAX_WIDTH = 600
MAX_HEIGHT = 600
PAD_X = 10
PAD_Y = 10

FONT_LABEL = ("Arial", 16)
DEFAULT_ANCHOR = 'nw'

TARGET_X = 50
DEADENDS_X = 300

LEN_MAX_LOCK = 4
FIRST = '0'*LEN_MAX_LOCK
DEFAULT_BAD_LOCK_VALUE = None

WHEEL_MIN_X = 50
WHEEL_MAX_X = MAX_WIDTH - 50
WHEEL_MIN_Y = int(MAX_HEIGHT / 3) 
WHEEL_MAX_Y = int(MAX_HEIGHT / 3) + 150
WHEEL_SIZE_X = int(WHEEL_MAX_X / LEN_MAX_LOCK)
WHEEL_SIZE = int((WHEEL_MAX_X - WHEEL_MIN_X) / LEN_MAX_LOCK)
WHEEL_SIZE_Y = int(WHEEL_MAX_Y / LEN_MAX_LOCK)


deadends = set()
list_wheels_label = []

def control_lock_value(val):
    if len(val) == LEN_MAX_LOCK:
        try:
            for char in val:
                c = int(char)
            return val
        except:
            pass
    return DEFAULT_BAD_LOCK_VALUE


def get_entry_target():
    result = control_lock_value(target_var_entry.get())
    color = COLOR_ENTRY_WARNING
    if result != DEFAULT_BAD_LOCK_VALUE:
        text_warning = 'target OK'
        color = COLOR_ENTRY_OK
    else:
        text_warning = f'Only {LEN_MAX_LOCK} digits'
    canvas.itemconfig(target_warning, text=text_warning, fill=color,  font=FONT_LABEL)


def add_deadends():
    global deadends
    result = control_lock_value(deadend_var_entry.get())
    color = COLOR_ENTRY_WARNING
    if result != DEFAULT_BAD_LOCK_VALUE:
        text_warning = 'deadend added'
        color = COLOR_ENTRY_OK
        deadends.add(result)
        print(deadends)
    else:
        text_warning = f'Only {LEN_MAX_LOCK} digits'
    canvas.itemconfig(deadend_warning, text=text_warning, fill=color,  font=FONT_LABEL)


def reset_deadends():
    global deadends
    text_warning = 'Reset deadends'
    print(f'deadend reset {deadends}')
    deadends = set()
    color = 'blue'
    canvas.itemconfig(deadend_warning, text=text_warning, fill=color,  font=FONT_LABEL)


def initialise_wheels(first=FIRST):
    for i in range(LEN_MAX_LOCK):
        x = box_wheels[i][0]
        y = box_wheels[i][1]
        w = FIRST[i]
        v = canvas.create_text(x+10, y-int(WHEEL_SIZE*0.1), text=w, anchor=DEFAULT_ANCHOR, font=('Arial', WHEEL_SIZE-10))
        list_wheels_label.append(v)


def run_simulation():
    op_lock = OpenLock(target=target_var_entry.get(), deadends=deadends, first=FIRST)
    paths = op_lock.get_paths()
    print(op_lock.get_paths())

    for u in paths:
        print(u)
        for i in range(LEN_MAX_LOCK):
            x = box_wheels[i][0]
            y = box_wheels[i][1]
            w = u[i]
            time.sleep(0.2)
            canvas.itemconfig(list_wheels_label[i], text=w, font=('Arial', WHEEL_SIZE-10))
            root.update()
        time.sleep(1)
    print(f'End Run simulation')


root = tk.Tk()
root.geometry(f"{MAX_WIDTH}x{MAX_HEIGHT}")
root.resizable(False, False)
root.title('Open THe Lock')
canvas = tk.Canvas(root, width=MAX_WIDTH, height=MAX_HEIGHT, background=COLOR_BACKGROUND)

# Target Lock
target_label = canvas.create_text(TARGET_X, 10, text='Target', anchor=DEFAULT_ANCHOR, font=FONT_LABEL)

target_var_entry = tk.StringVar()
target_entry = tk.Entry(root, textvariable=target_var_entry, width=10,  font=FONT_LABEL)
entry = canvas.create_window(TARGET_X, 40, window=target_entry, anchor=DEFAULT_ANCHOR)

target_warning = canvas.create_text(TARGET_X, 70, text=f'(*){LEN_MAX_LOCK} chiffres', anchor=DEFAULT_ANCHOR, font=FONT_LABEL)  

button1 = tk.Button(root, text='Add Target', font=FONT_LABEL, command=get_entry_target )
button_target = canvas.create_window(50, 100, window=button1, anchor=DEFAULT_ANCHOR)


# Deadends
deadends_label = canvas.create_text(DEADENDS_X, 10, text='Deadends', anchor=DEFAULT_ANCHOR, font=FONT_LABEL)

deadend_var_entry = tk.StringVar()
entry2 = tk.Entry(root, textvariable=deadend_var_entry, width=10,  font=FONT_LABEL)
deadends_entry = canvas.create_window(DEADENDS_X, 40, window=entry2, anchor=DEFAULT_ANCHOR)

deadend_warning = canvas.create_text(DEADENDS_X, 70, text=f'Deadends only {LEN_MAX_LOCK} digits', anchor=DEFAULT_ANCHOR, font=FONT_LABEL)

button2 = tk.Button(root, text='Add', font=FONT_LABEL, command=add_deadends)
button3 = tk.Button(root, text='Reset', font=FONT_LABEL, command=reset_deadends)
button_add_deadend = canvas.create_window(DEADENDS_X, 100, window=button2, anchor=DEFAULT_ANCHOR)
button_delete_deadend = canvas.create_window(DEADENDS_X+70, 100, window=button3, anchor=DEFAULT_ANCHOR)

# Cellule Lock
#canvas.create_rectangle(WHEEL_MIN_X, WHEEL_MIN_Y, WHEEL_MAX_X, WHEEL_MAX_Y, width=1, fill='blue')
box_wheels = []
for i in range(WHEEL_MIN_X, WHEEL_MAX_X, WHEEL_SIZE):
    dim = (i, WHEEL_MIN_Y, i+WHEEL_SIZE, WHEEL_MAX_Y)
    box_wheels.append(dim)
    x1 = dim[0]
    y1 = dim[1]
    x2 = dim[2]-10
    y2 = dim[3]
    canvas.create_rectangle(x1, y1, x2, y2, width=5, fill=COLOR_WHEEL_CELL)

initialise_wheels()

button4 = tk.Button(root, text='OPEN LOCK', font=FONT_LABEL, command=run_simulation)
button_run = canvas.create_window(200, 400, window=button4, anchor=DEFAULT_ANCHOR)

canvas.pack(expand=False)
root.mainloop()