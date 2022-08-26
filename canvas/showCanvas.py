import tkinter
import config.config as config
import util.commonUtil as commonUtil


def addCanvasToWindow(window):
    canvas = tkinter.Canvas(window, bg='#FFFFFF', height=commonUtil.getHeight(window, "80%"),
                            width=commonUtil.getHeight(window, "80%"))
    canvas.pack(side='right')
    return canvas


def drawInnerBorder(canvas):
    height = canvas.winfo_reqheight()
    length = height * 0.8
    unitLength = length / config.mapSize
    startX = height * 0.1
    startY = height * 0.1

    canvas.create_rectangle(startX, startY,
                            startX + length,
                            startY + length,
                            fill='#FFFFFF', outline='#000000', width=2)

    # canvas.create_line(0, 0, height, height, fill='#000000')
    lineWith = unitLength * 0.5
    # for i in range(config.mapSize):
    #     x = startX + i * unitLength + unitLength / 2
    #     canvas.create_line(x, startY, x, startY - lineWith, fill='#000000')

    for i in range(config.mapSize):
        y = startY + i * unitLength + unitLength / 2
        canvas.create_line(startX, y, startX - lineWith, y, fill='#000000', width=2)
        # 在线段的左边画文字
        canvas.create_text(startX - lineWith - unitLength / 2, y, text=i, fill='#000000', font=('Arial', config.showCanvasNumFontSize))


    # as


    for i in range(config.mapSize):
        x = startX + i * unitLength + unitLength / 2
        y = startY + length
        canvas.create_line(x, y, x, y + lineWith, fill='#000000', width=2)
        # 在线段的下面画文字
        canvas.create_text(x, y + lineWith + unitLength / 2 + 5, text=i, fill='#000000', font=('Arial', config.showCanvasNumFontSize))


def drawNumbers(canvas):
    drawInnerBorder(canvas)
    # canvas.create_text(x, y, text=number, fill='#000000')
