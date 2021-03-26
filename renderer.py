from graphics import *

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
                for j in range(self.scale):
                    for k in range(self.scale):
                        pt = Point(x+j,x+k)
                        pt.setOutline(color_rgb(255,255,255))
                
    def testRender(self):
        self.setPixel(0, 0)
        self.setPixel(5, 2)


     