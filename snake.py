import tkinter as tk
import random

class Snake(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='black', width=500, height=400)
        self.canvas = tk.Canvas(self, bg='black', width=500, height=400)
        self.canvas.grid(row = 0, column = 0)
        self.parent = parent

        self.reset()

    def reset(self):
        self.snake = [[1, 0]]
        self.apple = [1, 4]
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
            self.apple = [random.randint(0,24), random.randint(0,19)]
            while self.apple in self.snake + [self.nextStep()]:
                self.apple = [random.randint(0, 24), random.randint(0, 19)]
        else:
            self.updateSnake()
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.snake[0][0] * 20, self.snake[0][1] * 20, self.snake[0][0] * 20 + 20, self.snake[0][1] * 20 + 20, fill='orange')
        for i in range(1, len(self.snake)):
            link = self.snake[i]
            self.canvas.create_rectangle(link[0] * 20, link[1] * 20, link[0] * 20 + 20, link[1] * 20 + 20, fill='green')
            self.canvas.create_oval(link[0] * 20 + 5, link[1] * 20 + 5, link[0] * 20 + 15, link[1] * 20 + 15, fill='blue')
        self.canvas.create_rectangle(self.apple[0] * 20 , self.apple[1] * 20, self.apple[0] * 20 + 20, self.apple[1] * 20 + 20, fill='red')

    def updateSnake(self):
        _snake = [list(self.snake[0])]
        for i in range(len(self.snake) - 1):
            _snake.append(list(self.snake[i]))

        _snake[0][0] += self.dxdy[0]
        _snake[0][1] += self.dxdy[1]

        self.snake = _snake

    def isOver(self):
        if self.snake[0] in self.snake[1:]:
            return True

        cell = self.snake[0]

        if cell[0] < 0 or cell[0] > 24 or cell[1] < 0 or cell[1] > 19:
            return True

        return False

    def gameOver(self):
        self.textOcc = not self.textOcc
        self.canvas.delete("all")
        if self.textOcc:
            self.canvas.create_text(500 // 2, 400 // 2, text='Game Over', fill='red', font=("Purisa", 70))

    def pause(self):
        self.textOcc = not self.textOcc
        self.canvas.delete("all")
        self.draw()
        if self.textOcc:
            self.canvas.create_text(500 // 2, 400 // 2, text='Pause', fill='yellow', font=("Purisa", 70))

    def winning(self):
        self.textOcc = not self.textOcc
        self.canvas.delete("all")
        self.draw()
        if self.textOcc:
            self.canvas.create_text(500 // 2, 400 // 2, text='You Win !!!', fill='yellow', font=("Purisa", 70))