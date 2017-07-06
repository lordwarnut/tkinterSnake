import tkinter as tk
import time

root = tk.Tk()

chain = [[10,10], [9,10], [8, 10], [7, 10], [6, 10]]
dxdy = (1, 0)

state = 'Running'

resetButton = tk.Button(root, text = 'Reset', command = lambda:print('Reset'))
resetButton.grid(column=0, row=1, sticky=tk.W + tk.E)

canv = tk.Canvas(root, bg='black', width=500, height=400)
canv.grid(column = 0, row = 0)

def move():
    global chain
    newChain = [list(chain[0])]
    for i in range(len(chain) - 1):
        newChain.append(list(chain[i]))

    newChain[0][0] += dxdy[0]
    newChain[0][1] += dxdy[1]

    chain = newChain

def isOver():
    if chain[0] in chain[1:]:
        return True

    return False

def update():
    global state
    canv.delete("all")
    if isOver():
        state = 'GameOver'
    for link in chain:
        canv.create_rectangle(link[0] * 20, link[1] * 20, link[0] * 20 + 20, link[1] * 20 + 20, fill='green')
    move()

gameOverDraw = False
def gameOver():
    global gameOverDraw
    gameOverDraw = not gameOverDraw
    canv.delete("all")
    if gameOverDraw:
        canv.create_text(500//2, 400//2, text='Game Over', fill='red')

def setDXDY(x):
    def setter(e):
        global dxdy
        print(x)
        dxdy = x
    return setter

root.bind('<Up>', setDXDY((0, -1)))
root.bind('<Down>', setDXDY((0, 1)))
root.bind('<Left>', setDXDY((-1, 0)))
root.bind('<Right>', setDXDY((1, 0)))

t = time.time()
while True:
    if time.time() - t > 0.4 and state == 'Running':
        update()
        t = time.time()
    elif time.time() - t > 0.5 and state == 'GameOver':
        gameOver()
        t = time.time()

    root.update_idletasks()
    root.update()