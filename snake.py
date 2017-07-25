import tkinter as tk
import random

class Snake(tk.Frame):
    def __init__(self, parent):

        self.width = 4
        self.height = 4
        self.linkHW = 150

        self.screenWidth = self.width * self.linkHW
        self.screenHeight = self.height * self.linkHW

        tk.Frame.__init__(self, parent, bg='black', width=self.screenWidth, height=self.screenHeight)
        self.canvas = tk.Canvas(self, bg='black', width=self.screenWidth, height=self.screenHeight)
        self.canvas.grid(row = 0, column = 0)
        self.parent = parent

        self.reset()

    def reset(self):
        self.snake = [[1, 0]]
        self.apple = [1, 2]
        self.dxdy = [0, 1]
        self.textOcc = False

    def isApple(self):
        if self.nextStep() == self.apple:
            return True
        return False

    def nextStep(self):
        return [self.snake[0][0] + self.dxdy[0], self.snake[0][1] + self.dxdy[1]]

    def step(self):
        if self.isApple():
            self.snake.insert(0, self.nextStep())
            if len(self.snake) < self.width * self.height:
                self.apple = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
                while self.apple in self.snake + [self.nextStep()]:
                    self.apple = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
        else:
            self.updateSnake()
        self.draw()

    def getCellCoords(self, x, y):
        return (x * self.linkHW,
                y * self.linkHW,
                x * self.linkHW + self.linkHW,
                y * self.linkHW + self.linkHW)

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(*self.getCellCoords(self.snake[0][0], self.snake[0][1]), fill='orange')
        for i in range(1, len(self.snake)):
            link = self.snake[i]
            self.canvas.create_rectangle(*self.getCellCoords(link[0], link[1]), fill='green')
            self.canvas.create_oval(link[0] * self.linkHW + self.linkHW * 0.25,
                                    link[1] * self.linkHW + self.linkHW * 0.25,
                                    link[0] * self.linkHW + self.linkHW * 0.75,
                                    link[1] * self.linkHW + self.linkHW * 0.75, fill='blue')
        self.canvas.create_rectangle(*self.getCellCoords(self.apple[0], self.apple[1]), fill='red')
        self.canvas.create_text(0, 0, anchor=tk.NW, text=f'Score : {len(self.snake)}', fill='pink', font=("Purisa", 10))

    def updateSnake(self):
        snakeBuffer = [list(self.snake[0])]
        for i in range(len(self.snake) - 1):
            snakeBuffer.append(list(self.snake[i]))

        snakeBuffer[0][0] += self.dxdy[0]
        snakeBuffer[0][1] += self.dxdy[1]

        self.snake = snakeBuffer

    def isOver(self):
        if self.snake[0] in self.snake[1:]:
            return True

        cell = self.snake[0]

        if cell[0] < 0 or cell[0] >= self.width or cell[1] < 0 or cell[1] >= self.height:
            return True

        return False

    def gameOver(self):
        self.textOcc = not self.textOcc
        self.canvas.delete("all")
        if self.textOcc:
            self.canvas.create_text(self.screenWidth // 2, self.screenHeight // 2, text='Game Over', fill='red', font=("Purisa", 70))

    def pause(self):
        self.textOcc = not self.textOcc
        self.canvas.delete("all")
        #self.draw()
        if self.textOcc:
            self.canvas.create_text(self.screenWidth // 2, self.screenHeight // 2, text='Pause', fill='yellow', font=("Purisa", 70))

    def winning(self):
        self.textOcc = not self.textOcc
        self.canvas.delete("all")
        self.draw()
        if self.textOcc:
            self.canvas.create_text(self.screenWidth // 2, self.screenHeight // 2, text='You Win !!!', fill='yellow', font=("Purisa", 70))