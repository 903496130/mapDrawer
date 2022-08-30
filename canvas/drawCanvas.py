import tkinter
import event.DrawCanvasEvent as drawCanvasEvent
import config.config as config
import util.commonUtil as commonUtil

canvas = ""


def addCanvasToWindow(window):
    global canvas

    width = commonUtil.getHeight(window, "100%") - 70
    height = width

    group = tkinter.LabelFrame(window, text="绘制区域")
    group.place(x=7, y=60, width=width, height=height)

    canvas = tkinter.Canvas(group, bg='black', height=width - 10, width=height - 10)
    canvas.place(x=5, y=5)

    canvas.place(x=-2, y=0)
    canvas.bind('<Button-1>', lambda event: drawCanvasEvent.handleMouseMoveEvent(canvas, event))
    canvas.bind('<B1-Motion>', lambda event: drawCanvasEvent.handleMouseMoveEvent(canvas, event))
    canvas.bind('<ButtonRelease-1>', lambda event: drawCanvasEvent.handleMouseReleaseEvent(canvas, event))


def fullCanvasWithBlock(color):
    global canvas
    blockWidthAndHeight = commonUtil.getUnitLength(canvas)
    for i in range(config.mapSize):
        for j in range(config.mapSize):
            canvas.create_rectangle(i * blockWidthAndHeight, j * blockWidthAndHeight,
                                    (i + 1) * blockWidthAndHeight,
                                    (j + 1) * blockWidthAndHeight, fill=color, outline=color)





