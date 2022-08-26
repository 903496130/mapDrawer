import tkinter
import event.DrawCanvasEvent as drawCanvasEvent
import config.config as config
import util.commonUtil as commonUtil

canvas = ""


def addCanvasToWindow(window):
    global canvas
    # 创建一个canvas画布
    # 画布有黑色边框
    canvas = tkinter.Canvas(window, bg='black', height=window.winfo_height() * 0.9, width=window.winfo_height() * 0.9)
    canvas.pack(side='left')
    # canvas添加黑色边框
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), outline='black')
    # 创建点击事件
    canvas.bind('<Button-1>', lambda event: drawCanvasEvent.handleMouseMoveEvent(canvas, event))
    # 创建鼠标移动时间
    canvas.bind('<B1-Motion>', lambda event: drawCanvasEvent.handleMouseMoveEvent(canvas, event))

    # 注册左键放开事件
    canvas.bind('<ButtonRelease-1>', lambda event: drawCanvasEvent.handleMouseReleaseEvent(canvas, event))


def fullCanvasWithBlock(color):
    global canvas
    blockWidthAndHeight = commonUtil.getUnitLength(canvas)
    for i in range(config.mapSize):
        for j in range(config.mapSize):
            canvas.create_rectangle(i * blockWidthAndHeight, j * blockWidthAndHeight,
                                    (i + 1) * blockWidthAndHeight,
                                    (j + 1) * blockWidthAndHeight, fill=color, outline=color)
