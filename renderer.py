from graphics import *
import math

class Renderer:
    def __init__(self, scale):
        self.cols = 64
        self.rows = 32
        self.scale = scale
        self.winWidth = self.cols * self.scale
        self.winHeight = self.rows * scale
        self.canvas = GraphWin("chip7emu",self.winWidth,self.winHeight)
        self.canvas.setBackground(color_rgb(0,0,0))
        self.display = [0] * self.cols * self.rows
    def setPixel(self, x, y):
        if x > self.cols:
            x -= self.cols
        elif x < 0:
            x += self.cols
        if y > self.rows:
            y -= self.rows
        elif y < 0:
            y += self.rows
        pixelLoc = x + (y * self.cols)
        self.display[pixelLoc] ^= 1
        return not self.display[pixelLoc] 

    def clear(self):
        self.display = [0] * self.cols * self.rows

    def render(self):
        self.canvas.setBackground(color_rgb(0,0,0))

        for i in range(self.cols * self.rows):
            x = (i % self.cols) * self.scale
            y = (i // self.cols) * self.scale

            if self.display[i]:
                self.canvas    
                pt = Point(250, 250)
                pt.setOutline(color_rgb(255,255,255))
                pt.draw(win)


     