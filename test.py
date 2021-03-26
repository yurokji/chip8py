from graphics import *


def main():
    win = GraphWin("sdf",500,500)
    win.setBackground(color_rgb(0,0,0))
    pt = Point(250, 250)
    pt.setOutline(color_rgb(255,255,0))
    pt.draw(win)
    win.getMouse()
    win.close()

main()