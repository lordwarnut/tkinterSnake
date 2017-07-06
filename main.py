import tkinter as tk
import time
import snake

root = tk.Tk()
state = 's'
oldState = 'r'

sCanv = snake.Snake(root)
sCanv.grid(column=0, row=0, columnspan=3)
speed = 1

def setSpeed():
    global speed
    speed = float(speedSelect.get())

def start(*args):
    global state
    sCanv.reset()
    state = 'r'
    print(state)

def punp(*args):
    global state, oldState
    if state == 'p':
        state = oldState
    else:
        oldState = state
        state = 'p'

resetButton = tk.Button(root, text = 'Reset', command = start)
resetButton.grid(column=0, row=1, sticky=tk.W + tk.E)

pauseButton = tk.Button(root, text = 'Pause', command = punp)
pauseButton.grid(column=1, row=1, sticky=tk.W + tk.E)

speedSelect = tk.Spinbox(root, from_=0.1, to=2, increment=0.1, command=setSpeed)
speedSelect.grid(column=2, row=1, sticky=tk.W + tk.E)
speedSelect.delete(0,"end")
speedSelect.insert(0, 0.5)
setSpeed()

def setDXDY(x, y):
    def setter(e):
        sCanv.dxdy = (x, y)
    return setter

root.bind('<Up>', setDXDY(0, -1))
root.bind('<Down>', setDXDY(0, 1))
root.bind('<Left>', setDXDY(-1, 0))
root.bind('<Right>', setDXDY(1, 0))
root.bind('<space>', punp)
root.bind('r', start)

t = time.time() - 100

while True:
    if state == 'r':
        if time.time() - t > speed:
            sCanv.step()
            if len(sCanv.snake) >= 20*25:
                state = 'w'
            t = time.time()
            if sCanv.isOver():
                state = 'o'
    if state == 'o':
        if time.time() - t > 0.5:
            sCanv.gameOver()
            t = time.time()
    if state == 'p':
        if time.time() - t > 0.5:
            sCanv.pause()
            t = time.time()
    if state == 'w':
        if time.time() - t > 0.5:
            sCanv.winning()
            t = time.time()

    root.update_idletasks()
    root.update()